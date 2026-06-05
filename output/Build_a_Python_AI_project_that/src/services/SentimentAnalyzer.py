python
# src/services/SentimentAnalyzer.py

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import download

# Download required NLTK data if not already downloaded
download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def extract_sentiments(self, text):
        """
        Analyze sentiment of the input text.

        Args:
        text (str): Input text to be analyzed.

        Returns:
        dict: Dictionary containing sentiment analysis results.
        """
        sentiment_scores = self.sia.polarity_scores(text)
        return sentiment_scores

    def classify_sentiment(self, scores):
        """
        Classify sentiment as positive, negative, or neutral.

        Args:
        scores (dict): Dictionary containing sentiment scores.

        Returns:
        str: Classified sentiment.
        """
        compound = scores['compound']
        if compound >= 0.05:
            return "Positive"
        elif compound <= -0.05:
            return "Negative"
        else:
            return "Neutral"



# src/gui/main.py

import tkinter as tk
from tkinter import messagebox
from src.services import SentimentAnalyzer

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.sa = SentimentAnalyzer()

    def create_widgets(self):
        self.input_label = tk.Label(self)
        self.input_label["text"] = "Enter text:"
        self.input_label.pack(side="top")

        self.input_entry = tk.Text(self, width=50, height=10)
        self.input_entry.pack(side="top")

        self.analyze_button = tk.Button(self)
        self.analyze_button["text"] = "Analyze Sentiment"
        self.analyze_button["command"] = self.analyze_sentiment
        self.analyze_button.pack(side="top")

        self.output_label = tk.Label(self)
        self.output_label["text"] = ""
        self.output_label.pack(side="top")

    def analyze_sentiment(self):
        text = self.input_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter text.")
            return

        scores = self.sa.extract_sentiments(text)
        sentiment = self.sa.classify_sentiment(scores)

        output = f"Text: {text}\n"
        output += f"Positive Score: {scores['pos']}\n"
        output += f"Neutral Score: {scores['neu']}\n"
        output += f"Negative Score: {scores['neg']}\n"
        output += f"Compound Score: {scores['compound']}\n"
        output += f"Sentiment: {sentiment}"

        self.output_label["text"] = output

root = tk.Tk()
app = Application(master=root)
app.mainloop()
