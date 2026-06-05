python
# src/sentiment_analyzer.py
import tkinter as tk
from tkinter import ttk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title('Sentiment Analyzer')
        self.root.geometry('300x200')

        self.label = ttk.Label(self.root, text='Enter your text:')
        self.label.pack(pady=10)

        self.text_box = tk.Text(self.root, height=10, width=40)
        self.text_box.pack(pady=10)

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.analyze_button = ttk.Button(self.button_frame, text='Analyze', command=self.analyze_sentiment)
        self.analyze_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = ttk.Button(self.button_frame, text='Reset', command=self.reset_text)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.result_label = ttk.Label(self.root, text='')
        self.result_label.pack(pady=10)

        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self):
        text = self.text_box.get('1.0', tk.END)
        sentiment = self.sia.polarity_scores(text)
        self.display_result(sentiment)

    def reset_text(self):
        self.text_box.delete('1.0', tk.END)
        self.result_label['text'] = ''

    def display_result(self, sentiment):
        self.result_label['text'] = f'Sentiment Score: {sentiment["compound"]}\nPositive: {(sentiment["pos"]) * 100}%\nNegative: {(sentiment["neg"]) * 100}%\nNeutral: {(sentiment["neu"]) * 100}%'


root = tk.Tk()
app = SentimentAnalyzer(root)
root.mainloop()
