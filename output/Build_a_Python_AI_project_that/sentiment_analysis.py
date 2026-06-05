python
# File: sentiment_analysis.py

# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import nltk
import numpy as np

# Train the Naive Bayes model
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
# Train the Logistic Regression model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
# Load the VADER lexicon
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# Define the SentimentAnalysis class
class SentimentAnalysis:
    def __init__(self, root):
        self.root = root
        self.root.title('Sentiment Analysis')
        self.label = ttk.Label(root, text='Enter a review:')
        self.label.pack()
        self.entry = ttk.Entry(root, width=100)
        self.entry.pack()
        self.button = ttk.Button(root, text='Analyze sentiment', command=self.analyze_sentiment)
        self.button.pack()
        self.text_area = tk.Text(root, height=10, width=100)
        self.text_area.pack()
        self.sentiment_model = self.load_model()

    # Load a model (currently supports Naive Bayes, Logistic Regression, and VADER)
    def load_model(self):
        model = None
        choice = input("Choose a model: Naive Bayes (nb), Logistic Regression (lr), VADER (vader): ")
        if choice.lower() == 'nb':
            model = MultinomialNB()
            model.fit(self.load_dataset('nb'))
        elif choice.lower() == 'lr':
            model = LogisticRegression()
            model.fit(self.load_dataset('lr'))
        elif choice.lower() == 'vader':
            model = SentimentIntensityAnalyzer()
        return model

    # Load a dataset (currently supports NLTK's VADER and IMDB datasets)
    def load_dataset(self, dataset):
        if dataset == 'nb':
            from sklearn.datasets import fetch_20newsgroups
            dataset = fetch_20newsgroups(subset='train', categories=['rec.sport.baseball'])
        elif dataset == 'lr':
            from sklearn.datasets import fetch_20newsgroups
            dataset = fetch_20newsgroups(subset='train', categories=['sci.electronics'])
        return dataset.data

    # Preprocess the input text
    def preprocess_text(self, text):
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english'))
        translator = str.maketrans('', '', string.punctuation)
        tokens = word_tokenize(text.lower())
        tokens = [t for t in tokens if t not in stop_words]
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
        tokens = [t for t in tokens if t]
        text = ' '.join(tokens)
        return text.translate(translator)

    # Analyze the sentiment of the input text
    def analyze_sentiment(self):
        text = self.entry.get()
        text = self.preprocess_text(text)
        if hasattr(self.sentiment_model, 'lexicon'):
            results = self.sentiment_model.polarity_scores(text)
        else:
            results = self.sentiment_model.predict(np.array([text]))
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, str(results))

# Create the main application window
root = tk.Tk()
app = SentimentAnalysis(root)
root.mainloop()

This code uses the following libraries:

*   `nltk` for natural language processing tasks
*   `tkinter` for creating a simple UI
*   `sklearn` for training machine learning models
*   `numpy` for numerical computations