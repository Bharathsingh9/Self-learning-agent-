python
# utils/data_loader.py

import pandas as pd
from sklearn.model_selection import train_test_split
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Sentiment analysis class
class SentimentAnalysis:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.stemmer = PorterStemmer()

    # Preprocess text data
    def preprocess_text(self, text):
        tokens = word_tokenize(text)
        tokens = [self.stemmer.stem(token) for token in tokens if token.isalpha()]
        return ' '.join(tokens)

    # Load dataset
    def load_dataset(self, file_path):
        return pd.read_csv(file_path)

    # Split dataset into training and testing sets
    def split_dataset(self, dataset, test_size=0.2, random_state=42):
        return train_test_split(dataset['text'], dataset['label'], test_size=test_size, random_state=random_state)

    # Get sentiment scores
    def get_sentiment_scores(self, text):
        return self.sia.polarity_scores(text)

    # Convert sentiment scores to sentiment labels
    def convert_scores_to_labels(self, scores):
        if scores['compound'] > 0.05:
            return 'Positive'
        elif scores['compound'] < -0.05:
            return 'Negative'
        else:
            return 'Neutral'

# Main object
sentiment_analysis = SentimentAnalysis()
