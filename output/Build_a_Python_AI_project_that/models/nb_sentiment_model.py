python
# models/nb_sentiment_model.py

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)
nltk.download('vader_lexicon')

class NB SentimentModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = MultinomialNB()

    def train(self, X_train, y_train):
        self.vectorizer.fit(X_train)
        X_train_vectorized = self.vectorizer.transform(X_train)
        self.model.fit(X_train_vectorized, y_train)

    def predict(self, X_test):
        X_test_vectorized = self.vectorizer.transform(X_test)
        predictions = self.model.predict(X_test_vectorized)
        return predictions

    def evaluate(self, y_test, predictions):
        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions)
        return accuracy, report

class VaderSentimentModel:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze_text(self, text):
        sentiment = self.sia.polarity_scores(text)
        compound_score = sentiment['compound']
        if compound_score >= 0.05:
            return 'positive'
        elif compound_score <= -0.05:
            return 'negative'
        else:
            return 'neutral'
