python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize NLTK data
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sentiment Analyzer")
        self.root.geometry("400x200")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.text_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.text_frame, text="Text Input")

        self.result_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.result_frame, text="Result")

        # Create text input frame
        self.text_label = ttk.Label(self.text_frame, text="Enter text:")
        self.text_label.pack(pady=10)
        self.text_entry = tk.Text(self.text_frame, height=10, width=40)
        self.text_entry.pack(pady=10)

        self.analyze_button = ttk.Button(self.text_frame, text="Analyze", command=self.analyze_text)
        self.analyze_button.pack(pady=10)

        # Create text label and result label
        self.result_text = tk.Text(self.result_frame, height=10, width=40)
        self.result_text.pack(pady=10)

    def analyze_text(self):
        text = self.text_entry.get('1.0', 'end-1c')
        sentiment = SentimentIntensityAnalyzer()
        scores = sentiment.polarity_scores(text)
        result = f"Positive: {scores['pos']:.2f}\nNegative: {scores['neg']:.2f}\nNeutral: {scores['neu']:.2f}\nCompound: {scores['compound']:.2f}"
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert('1.0', result)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    analyzer.run()
