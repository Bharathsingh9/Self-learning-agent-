python
# src/nlp_modules.py

import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk
from nltk import pos_tag
from string import punctuation

nltk.download('wordnet')
nltk.download('averaged_perception_tagger')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')

class TextPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def _remove_special_chars(self, text):
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)

    def _remove_stopwords(self, tokens):
        stopwords_set = set(stopwords.words('english'))
        return [token for token in tokens if token.lower() not in stopwords_set]

    def _stem_tokens(self, tokens):
        return [self.stemmer.stem(token) for token in tokens]

    def _lemmatize_tokens(self, tokens):
        tags = pos_tag(tokens)
        return [self.lemmatizer.lemmatize(token, tag.lower()[:2] if tag.lower()[:2] in ['n', 'v'] else None) for (token, tag) in tags]

    def preprocess_text(self, text):
        text = text.lower()
        text = self._remove_special_chars(text)
        tokens = word_tokenize(text)
        tokens = self._remove_stopwords(tokens)
        tokens = self._stem_tokens(tokens)
        tokens = self._lemmatize_tokens(tokens)
        return ' '.join(tokens)
