python
# Import required libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Initialize NLTK data
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

class SentimentAnalyzer:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
        self.sia = SentimentIntensityAnalyzer()

    def clean_text(self, text):
        tokens = word_tokenize(text)
        tokens = [self.stemmer.stem(word.lower()) for word in tokens if word.isalpha() and word.lower() not in self.stop_words]
        return ' '.join(tokens)

    def analyze_sentiment(self, text):
        clean_text = self.clean_text(text)
        sentiment = self.sia.polarity_scores(clean_text)
        return sentiment

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Sentiment Analyzer')
        self.text_area = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.text_area.pack(padx=10, pady=10)
        self.result_area = scrolledtext.ScrolledText(self.root, width=80, height=5)
        self.result_area.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text='Analyze Sentiment', command=self.analyze_sentiment)
        self.button.pack(padx=10, pady=10)

    def analyze_sentiment(self):
        text = self.text_area.get('1.0', 'end-1c')
        if text.strip():
            analyzer = SentimentAnalyzer()
            sentiment = analyzer.analyze_sentiment(text)
            result = f'Sentiment Analysis: \n'
            result += f'Score: {sentiment["compound"]}\n'
            result += f'Positive: {sentiment["pos"]}\n'
            result += f'Neutral: {sentiment["neu"]}\n'
            result += f'Negative: {sentiment["neg"]}\n'
            self.result_area.delete('1.0', 'end')
            self.result_area.insert('1.0', result)
        else:
            messagebox.showerror('Error', 'Input field cannot be empty')

    def run(self):
        self.root.mainloop()

def main():
    gui = GUI()
    gui.run()

if __name__ == '__main__':
    main()
