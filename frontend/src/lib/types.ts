export interface Sentence {
  chinese: string;
  pinyin: string;
  translation: string;
  words: {
    chinese: string;
    pinyin: string;
    translation: string;
  }[];
}