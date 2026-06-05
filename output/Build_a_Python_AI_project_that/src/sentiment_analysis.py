python
# src/sentiment_analysis.py

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import scrolledtext

nltk.download('vader_lexicon')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self, width=60, height=10)
        self.text_area.pack(padx=10, pady=10)

        self.input_label = tk.Label(self, text="Text Input:")
        self.input_label.pack(padx=10, pady=10)

        self.input_entry = tk.Entry(self, width=60)
        self.input_entry.pack(padx=10, pady=10)

        self.analyze_button = tk.Button(self)
        self.analyze_button["text"] = "Analyze Sentiment"
        self.analyze_button["command"] = self.analyze_sentiment
        self.analyze_button.pack(padx=10, pady=10)

        self.result_text = tk.Text(self, width=60, height=5)
        self.result_text.pack(padx=10, pady=10)

    def analyze_sentiment(self):
        text = self.input_entry.get()
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        overall_sentiment = self.calculate_overall_sentiment(sentiment)

        self.result_text.delete('1.0', tk.END)
        self.result_text.insert('1.0', f"Sentiment Analysis Results:\n")
        self.result_text.insert('2.0', f"  - Polarity Score: {sentiment['compound']:.4f}\n")
        self.result_text.insert('3.0', f"  - Positive Score: {sentiment['pos']:.4f}\n")
        self.result_text.insert('4.0', f"  - Negative Score: {sentiment['neg']:.4f}\n")
        self.result_text.insert('5.0', f"  - Neutral Score: {sentiment['neu']:.4f}\n")
        self.result_text.insert('6.0', f"  - Overall Sentiment: {overall_sentiment}\n")

    def calculate_overall_sentiment(self, sentiment):
        if sentiment['compound'] > 0.05:
            return "Positive"
        elif sentiment['compound'] < -0.05:
            return "Negative"
        else:
            return "Neutral"

root = tk.Tk()
app = Application(master=root)
app.mainloop()
