python
# static/lib/Flask.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pickle
import sqlite3

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class SentimentAnalyzer(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()
        self.input_label = tk.Label(root, text='Enter text:')
        self.input_label.pack()
        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack()
        self.button = tk.Button(root, text='Analyse sentiment', command=self.send_input)
        self.button.pack()
        self.output_label = tk.Label(root, text='')
        self.output_label.pack()
        self.root.mainloop()

    def send_input(self):
        input_text = self.input_entry.get()
        self.sentiment_result(input_text)

    def sentiment_result(self, text):
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(text)
        tokens = [token.lower() for token in tokens]
        tokens = [token for token in tokens if token.isalpha()]
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords.words('english')]
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(' '.join(tokens))
        if sentiment_scores['compound'] >= 0.05:
            result = 'Positive'
        elif sentiment_scores['compound'] <= -0.05:
            result = 'Negative'
        else:
            result = 'Neutral'
        output_text = f'Sentiment Analysis:\n\n{result}.\nScore: {sentiment_scores["compound"].round(3)}'
        self.output_label['text'] = output_text
