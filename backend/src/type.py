from pydantic import BaseModel


class Word(BaseModel):
    chinese: str
    pinyin: str
    translation: str


class Sentence(BaseModel):
    chinese: str
    pinyin: str
    translation: str
    words: list[Word]
