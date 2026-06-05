python
# src/preprocess_text.py

import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import download

download("punkt")
download("stopwords")

def remove_punctuation(text):
    """Remove punctuation from text."""
    return re.sub(r'[^\w\s]', '', text)

def remove_whitespace(text):
    """Remove extra whitespace from text."""
    return re.sub(r'\s+', ' ', text)

def convert_to_lowercase(text):
    """Convert all text to lowercase."""
    return text.lower()

def tokenize_text(text):
    """Tokenize text into individual words."""
    return word_tokenize(text)

def remove_stopwords(words):
    """Remove common stopwords from text."""
    stop_words = set(stopwords.words('english'))
    return [word for word in words if word not in stop_words]

def stemming_text(words):
    """Apply stemming to text."""
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in words]

def preprocess_text(text):
    """Preprocess text by cleaning, tokenizing, removing stopwords, and applying stemming."""
    text = remove_punctuation(text)
    text = remove_whitespace(text)
    text = convert_to_lowercase(text)
    words = tokenize_text(text)
    words = remove_stopwords(words)
    words = stemming_text(words)
    return ' '.join(words)

if __name__ == "__main__":
    text = "This is a sample text. It has multiple words. The text is interesting."
    preprocessed_text = preprocess_text(text)
    print("Preprocessed Text:", preprocessed_text)
