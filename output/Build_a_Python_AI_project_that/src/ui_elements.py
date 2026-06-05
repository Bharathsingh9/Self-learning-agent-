python
# src/ui_elements.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

class UIElements:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Analysis")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        # Input frame
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(pady=20, padx=20)

        self.input_label = ttk.Label(self.input_frame, text="Enter text:")
        self.input_label.pack(pady=10)

        self.input_entry = ttk.Entry(self.input_frame, width=50)
        self.input_entry.pack(pady=10)

        # Button frame
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=20, padx=20)

        self.analyze_button = ttk.Button(self.button_frame, text="Analyze", command=self.analyze_text)
        self.analyze_button.pack(pady=10)

        # Result frame
        self.result_frame = ttk.Frame(self.root)
        self.result_frame.pack(pady=20, padx=20)

        self.result_label = ttk.Label(self.result_frame, text="")
        self.result_label.pack(pady=10)

        self.sentiment_frame = ttk.Frame(self.result_frame)
        self.sentiment_frame.pack(pady=10)

        self.positive_label = ttk.Label(self.sentiment_frame, text="Positive: 0%")
        self.positive_label.pack(side=tk.LEFT, padx=10)

        self.neutral_label = ttk.Label(self.sentiment_frame, text="Neutral: 0%")
        self.neutral_label.pack(side=tk.LEFT, padx=10)

        self.negative_label = ttk.Label(self.sentiment_frame, text="Negative: 0%")
        self.negative_label.pack(side=tk.LEFT, padx=10)

    def analyze_text(self):
        text = self.input_entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter some text")
            return

        sia = SentimentIntensityAnalyzer()

        # Tokenize text
        tokens = word_tokenize(text)
        tokens = [token.lower() for token in tokens]

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]

        # Get sentiments
        sentiment_scores = sia.polarity_scores(text)
        positive = sentiment_scores['pos'] * 100
        neutral = sentiment_scores['neu'] * 100
        negative = sentiment_scores['neg'] * 100

        # Update labels
        self.result_label['text'] = "Sentiment Analysis:"
        self.positive_label['text'] = f"Positive: {positive:.2f}%"
        self.neutral_label['text'] = f"Neutral: {neutral:.2f}%"
        self.negative_label['text'] = f"Negative: {negative:.2f}%"
