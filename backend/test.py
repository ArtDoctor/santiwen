from src.pdf_utils import load_pdf, split_into_sentences
from src.zhongwen_utils import segment_words, find_meanings


def display_sentences(sentences):
    """
    Display sentences one by one.
    :param sentences: List of sentences.
    """
    for i, sentence in enumerate(sentences, start=1):
        print(f"Sentence {i}: {sentence}")
        words = segment_words(sentence)
        meanings = find_meanings(words)
        for word, meaning in zip(words, meanings):
            if meaning != "Symbol":
                print(f"{word}: {meaning}")
        input("Press Enter to continue.")


if __name__ == "__main__":
    pdf_path = "/home/ash/santiwen/backend/三体中国.pdf"  # Replace with your PDF file path
    text = load_pdf(pdf_path)
    if text:
        sentences = split_into_sentences(text)
        display_sentences(sentences)
    else:
        print("No text could be extracted from the PDF.")
