import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def ensure_nltk_data():
    """Download the NLTK resources needed for tokenising and lemmatising."""
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

    # Newer NLTK versions may also ask for this tokenizer table.
    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')


ensure_nltk_data()

STOP_WORDS = set(stopwords.words('english'))
LEMMATIZER = WordNetLemmatizer()


def clean_text(text):
    """
    Clean one sentence and return a list of tokens.

    Steps:
    1. Lowercase conversion
    2. Punctuation removal using re
    3. Tokenisation
    4. Stop word removal
    5. Lemmatisation
    """
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in STOP_WORDS]
    tokens = [LEMMATIZER.lemmatize(token) for token in tokens]
    return tokens


def preprocess(text):
    """Alias used by the assignment wording."""
    return clean_text(text)


if __name__ == '__main__':
    example = "I'm SO hyped!!!!"
    print("Original:", example)
    print("Clean tokens:", preprocess(example))
