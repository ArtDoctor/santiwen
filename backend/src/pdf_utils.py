import PyPDF2


def load_pdf(file_path):
    """
    Load text from a PDF file.
    :param file_path: Path to the PDF file.
    :return: Extracted text as a single string.
    """
    text = ""
    try:
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    text = text.replace("\n", " ")
    text = text.replace("  ", "")
    with open(file_path.replace(".pdf", ".txt"), "w", encoding="utf-8") as text_file:
        text_file.write(text)
    return text


def split_into_sentences(text):
    """
    Split text into sentences, using Chinese-specific sentence delimiters.
    :param text: Text to split.
    :return: List of sentences.
    """
    delimiters = '。！？!?'
    sentences = []
    sentence = []
    for char in text:
        sentence.append(char)
        if char in delimiters:
            sentences.append("".join(sentence))
            sentence = []
    # Add any remaining text as a sentence
    if sentence:
        sentences.append("".join(sentence))
    return sentences
