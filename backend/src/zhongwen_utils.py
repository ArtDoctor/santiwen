import jieba

# load text file (takes 0.23 seconds)
chinese_meanings_text = ""
with open('./resources/cedict_ts.u8', "r", encoding="utf-8") as text_file:
    chinese_meanings_text = text_file.read()
chinese_meanings = chinese_meanings_text.split("\n")
chinese_meanings = [meaning.split(" ") for meaning in chinese_meanings]
chinese_simplified_meanings = {}
for meaning in chinese_meanings:
    if meaning[1] not in chinese_simplified_meanings:
        chinese_simplified_meanings[meaning[1]] = ' '.join(meaning[2:])
    else:
        chinese_simplified_meanings[meaning[1]] += ' ' + ' '.join(meaning[2:])


skip_symbols = '．。！？!? ；;：:，,、“”‘’"\'（）()【】[]《》<>…—／'
skip_symbols += '0123456789'
skip_symbols += 'abcdefghijklmnopqrstuvwxyz'
skip_symbols += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def segment_words(sentence: str) -> list[str]:
    return jieba.lcut(sentence)


def get_meanings_pingyin(words: list[str]) -> tuple[list[str], list[str], list[str]]:
    words_new = []
    meanings = []
    pingyins = []
    for word in words:
        if word not in skip_symbols:
            if word in chinese_simplified_meanings:
                pingyin = chinese_simplified_meanings[word].split(']')[0].replace('[', '')
                meaning = ''.join(chinese_simplified_meanings[word].split(']')[1:])
                words_new.append(word)
                meanings.append(meaning)
                pingyins.append(pingyin)
            else:
                # try to split into characters
                for subword in word:
                    if subword in chinese_simplified_meanings:
                        pingyin = chinese_simplified_meanings[subword].split(']')[0].replace('[', '')
                        meaning = ''.join(chinese_simplified_meanings[subword].split(']')[1:])
                        meanings.append(meaning)
                        pingyins.append(pingyin)
                        words_new.append(subword)
                    else:
                        words_new.append(subword)
                        meanings.append("Meaning not found.")
                        pingyins.append("[Pingyin not found.]")
        else:
            words_new.append(word)
            meanings.append("Symbol")
            pingyins.append("Symbol")
    return words_new, meanings, pingyins


def convert_pinyin(pinyin):
    tone_vowels = {
        'a': 'āáǎà',
        'e': 'ēéěè',
        'i': 'īíǐì',
        'o': 'ōóǒò',
        'u': 'ūúǔù',
        'ü': 'ǖǘǚǜ',
    }

    vowels = 'aeiouü'
    result = []

    for word in pinyin.split():
        if word[-1].isdigit():  # Check if the last character is a tone number
            tone = int(word[-1])  # Extract the tone number
            base_word = word[:-1]  # Remove the tone number from the word

            # Handle neutral tone (5 or invalid)
            if tone == 5 or tone < 1 or tone > 4:
                result.append(base_word)  # Append as is for neutral tones
                continue

            # Find the vowel to apply the tone
            for i, char in enumerate(base_word):
                if char in vowels:
                    # Handle compound vowels (e.g., "iao" -> tone goes to 'a')
                    if char == 'i' and 'a' in base_word:
                        continue
                    if char == 'u' and ('a' in base_word or 'o' in base_word):
                        continue

                    # Replace the vowel with the tone mark
                    if char in tone_vowels:
                        marked_char = tone_vowels[char][tone - 1]
                        base_word = base_word[:i] + marked_char + base_word[i+1:]
                        break

            result.append(base_word)
        else:
            result.append(word)

    return ' '.join(result)


# Example usage
# pinyin_with_numbers = "dan4 ni3 hao3 ma1"
# pinyin_with_tones = convert_pinyin(pinyin_with_numbers)
# print(pinyin_with_tones)  # Output: "dàn nǐ hǎo mā"
