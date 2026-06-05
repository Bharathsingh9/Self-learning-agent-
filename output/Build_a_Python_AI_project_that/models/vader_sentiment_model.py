python
# models/vader_sentiment_model.py
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

class VaderSentimentModel:
    def __init__(self):
        self.NLTK_DATA_PATH = 'models/nltk_data'
        self.sia = SentimentIntensityAnalyzer()

    def process_text(self, text):
        tokens = word_tokenize(text)
        return self.sia.polarity_scores(' '.join(tokens))

    def analyze_sentiment(self, text):
        scores = self.process_text(text)
        if scores['compound'] > 0.05:
            return 'Positive', scores['compound']
        elif scores['compound'] < -0.05:
            return 'Negative', scores['compound']
        else:
            return 'Neutral', scores['compound']
