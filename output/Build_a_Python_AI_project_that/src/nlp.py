python
# src/nlp.py

import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
nltk.download('vader_lexicon')

class NLPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Analyzer")
        self.root.geometry("500x300")

        # Create GUI components
        self.label = tk.Label(root, text="Enter text to analyze:")
        self.label.pack()

        self.text_box = tk.Text(root, width=60, height=10)
        self.text_box.pack()

        self.button = tk.Button(root, text="Analyze", command=self.analyze)
        self.button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.result_text = tk.Label(root, text="", wraplength=400)
        self.result_text.pack()

    def analyze(self):
        text = self.text_box.get("1.0", tk.END)
        sia = SentimentIntensityAnalyzer()

        sentiment = sia.polarity_scores(text)

        polarity = sentiment['compound']

        if polarity > 0.05:
            self.result_label.config(text="Overall sentiment: Positive")
        elif polarity < -0.05:
            self.result_label.config(text="Overall sentiment: Negative")
        else:
            self.result_label.config(text="Overall sentiment: Neutral")

        words = word_tokenize(text)
        positive_count = 0
        negative_count = 0
        for word in words:
            if sia.polarity_scores(word)['compound'] > 0.05:
                positive_count += 1
            elif sia.polarity_scores(word)['compound'] < -0.05:
                negative_count += 1

        self.result_text.config(text=f"Positive words: {positive_count}\n"
                                    f"Negative words: {negative_count}\n"
                                    f"Polarity: {polarity}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NLPApp(root)
    root.mainloop()
