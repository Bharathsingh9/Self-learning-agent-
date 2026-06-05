python
# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import json

# Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('punkt')

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

class SentimentAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Sentiment Analysis')
        self.text_label = tk.Label(root, text='Enter text to analyze:', font=('Arial', 14))
        self.text_label.pack(padx=10, pady=10)
        self.text_entry = tk.Text(root, width=50, height=10, font=('Arial', 14))
        self.text_entry.pack(padx=10, pady=10)
        self.button = tk.Button(root, text='Analyze Sentiment', command=self.analyze_sentiment, bg='green', fg='white')
        self.button.pack(padx=10, pady=10)
        self.output_label = tk.Label(root, text='', font=('Arial', 14))
        self.output_label.pack(padx=10, pady=10)

    def analyze_sentiment(self):
        text = self.text_entry.get('1.0', tk.END)
        sentiment_scores = sia.polarity_scores(text)
        compound_score = sentiment_scores['compound']
        if compound_score >= 0.05:
            result = 'Positive'
        elif compound_score <= -0.05:
            result = 'Negative'
        else:
            result = 'Neutral'
        self.output_label.config(text=f'Sentiment Result: {result}\n\nScore: {sentiment_scores}')

if __name__ == '__main__':
    root = tk.Tk()
    app = SentimentAnalysisApp(root)
    root.mainloop()


**Note:** Make sure you run this script in an environment where it has permission to download NLTK data.