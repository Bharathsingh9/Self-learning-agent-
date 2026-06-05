python
# models/lg_sentiment_model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.exceptions import ConvergenceWarning
import pandas as pd
import numpy as np

class SentimentModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression(max_iter=1000)
        self.trained = False

    def train(self, data):
        x = self.vectorizer.fit_transform(data['text'])
        y = data['sentiment'].map({'positive': 1, 'negative': 0})
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        
        with np.errstate(invalid='warn', divide='warn', over='warn', under='warn', ignore='none'):
            try:
                self.model.fit(x_train, y_train)
            except Warning as e:
                if str(e).startswith('convergence_warning'):
                    pass  # ignore convergence warning
                else:
                    raise e

        self.trained = True

    def predict(self, text):
        input_vector = self.vectorizer.transform([text])
        prediction = self.model.predict(input_vector)
        return prediction[0]

    def get_accuracy(self, data):
        x = self.vectorizer.transform(data['text'])
        y = data['sentiment'].map({'positive': 1, 'negative': 0})
        predictions = self.model.predict(x)
        accuracy = accuracy_score(y, predictions)
        return accuracy

# Example usage:
if __name__ == "__main__":
    # Load the IMDB dataset
    from sklearn.datasets import fetch_20newsgroups
    from sklearn.datasets import fetch_20newsgroups_vectorized as newsgroups_vectorized

    # Load the IMDB dataset
    data = fetch_20newsgroups_vectorized(subset='train', categories=['alt.atheism', 'sci.space'])

    # Extract the text and sentiment from the dataset
    texts = data.data
    sentiments = ['positive' if target>0 else 'negative' for target in data.target]

    # Create a DataFrame
    df = pd.DataFrame({'text': texts, 'sentiment': sentiments})

    # Train the model
    model = SentimentModel()
    model.train(df)

    # Test the model
    prediction = model.predict('This is a great product!')
    print(prediction)
