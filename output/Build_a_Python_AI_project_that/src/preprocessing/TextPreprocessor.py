python
# File: src/preprocessing/TextPreprocessor.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

class TextPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def tokenize_text(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokens):
        return [token for token in tokens if token.lower() not in self.stop_words]

    def remove_punctuation(self, tokens):
        return [token for token in tokens if token not in string.punctuation]

    def lemmatize_text(self, tokens):
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def remove_empty_str(self, tokens):
        return [token for token in tokens if token != '']

    def clean_text(self, text):
        tokens = self.tokenize_text(text)
        tokens = self.remove_stopwords(tokens)
        tokens = self.remove_punctuation(tokens)
        tokens = self.lemmatize_text(tokens)
        tokens = self.remove_empty_str(tokens)
        return ' '.join(tokens)

    def preprocess_text(self, text):
        text = text.lower()
        text = self.clean_text(text)
        return text
