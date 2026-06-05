python
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tkinter import Tk, Label, Entry, Button, Text, END
from tkinter import ttk

# Download required NLTK data
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self, text_area):
        self.text_area = text_area
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self):
        text = self.text_area.get('1.0', END)
        sentiment_scores = self.sia.polarity_scores(text)
        overall_score = (sentiment_scores['pos'] - sentiment_scores['neg']) + sentiment_scores['compound']
        if overall_score > 0.05:
            overall_label.config(text="Positive")
        elif overall_score < -0.05:
            overall_label.config(text="Negative")
        else:
            overall_label.config(text="Neutral")

        # Display sentiment scores
        scores_text.delete(1.0, END)
        scores_text.insert(END, f"Polarity: {sentiment_scores['compound']}\n"
                            f"Subjectivity: {sentiment_scores['subjectivity']}\n"
                            f"Positive: {sentiment_scores['pos']:.2f}\n"
                            f"Negative: {sentiment_scores['neg']:.2f}")

def main():
    global text_area, scores_text, overall_label
    root = Tk()
    root.title("Sentiment Analyzer")

    label = Label(root, text="Text Input")
    label.pack()

    text_area = Text(root, height=10, width=50)
    text_area.pack()

    button = Button(root, text="Analyze Sentiment", command=lambda: analyzer.analyze_sentiment())
    button.pack()

    scores_label = Label(root, text="Sentiment Scores")
    scores_label.pack()

    scores_text = Text(root, height=5, width=50)
    scores_text.pack()

    overall_label = Label(root, text="")
    overall_label.pack()

    analyzer = SentimentAnalyzer(text_area)
    root.mainloop()

if __name__ == "__main__":
    main()
