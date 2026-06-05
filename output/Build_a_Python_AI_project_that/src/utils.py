python
# src/utils.py

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import download

import spacy
import en_core_web_sm
import os

class NLPService:
    def __init__(self):
        self.nlp = en_core_web_sm.load()
        self.lema = WordNetLemmatizer()
        self.sia = SentimentIntensityAnalyzer()
        
        if not os.path.exists('vader_lexicon'):
            download('vader_lexicon')
        
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        doc = self.nlp(text)
        tokens = [t.lemma_ for t in doc if t.text.lower() not in self.stop_words]
        return ' '.join(tokens)

    def analyze_sentiment(self, text):
        preprocessed_text = self.preprocess_text(text)
        sentiment_scores = self.sia.polarity_scores(preprocessed_text)
        return sentiment_scores['compound']
