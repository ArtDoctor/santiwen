from fastapi import FastAPI, HTTPException
from src.zhongwen_utils import segment_words, get_meanings_pingyin, convert_pinyin
from src.pdf_utils import load_pdf, split_into_sentences
from fastapi.middleware.cors import CORSMiddleware
from src.type import Sentence, Word

pdf_path = "/home/ash/santiwen/backend/三体中国.pdf"
text = load_pdf(pdf_path)
sentences = split_into_sentences(text)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI sample app!"}


@app.get("/sentences/{sentence_id}", response_model=Sentence)
def get_sentence(sentence_id: int):
    if 0 <= sentence_id < len(sentences):
        sentence_chinese = sentences[sentence_id].replace(' ', '')
        words = segment_words(sentence_chinese)
        words_new, meanings, pingyings = get_meanings_pingyin(words)
        translation = ''
        sentence_pingyin = ''
        for pin, word_new in zip(pingyings, words_new):
            if pin != 'Symbol':
                sentence_pingyin += pin + ' '
            else:
                sentence_pingyin += word_new
        sentence = Sentence(
            chinese=sentence_chinese,
            pinyin=convert_pinyin(sentence_pingyin),
            translation=translation,
            words=[
                Word(
                    chinese=word,
                    pinyin=convert_pinyin(pingyin),
                    translation=meaning
                ) for word, pingyin, meaning in zip(words_new, pingyings, meanings) if meaning != "Symbol"
            ]
        )
        return sentence
    raise HTTPException(status_code=404, detail="Item not found")
