python
# src/settings.py

import tkinter as tk
from tkinter import ttk
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize NLTK
nltk.download('vader_lexicon')

class Settings:
    def __init__(self, master):
        self.master = master
        self.settings = tk.Frame(self.master)
        self.init_settings()

    def init_settings(self):
        self.frame_title = tk.Frame(self.settings)
        self.frame_title.pack(pady=10)

        self.title = tk.Label(self.frame_title, text="Sentiment Analysis", font=('Arial', 24))
        self.title.pack()

        self.frame_input = tk.Frame(self.settings)
        self.frame_input.pack(pady=10)

        self.label_input = tk.Label(self.frame_input, text="Enter text:")
        self.label_input.pack(side=tk.LEFT, padx=5, pady=5)

        self.input_text = tk.Text(self.frame_input, width=50, height=10)
        self.input_text.pack(side=tk.LEFT, padx=5, pady=5)

        self.button_analyze = tk.Button(self.frame_input, text="Analyze", command=self.analyze_text)
        self.button_analyze.pack(side=tk.LEFT, padx=5, pady=5)

    def analyze_text(self):
        self.settings.destroy()
        self.master.destroy()

        import src.main

class Main:
    def __init__(self, master):
        self.master = master
        self.main = tk.Frame(self.master)
        self.init_main()

    def init_main(self):
        self.sia = SentimentIntensityAnalyzer()
        self.text_to_analyze = ""
        self.results = ""

        self.frame_title = tk.Frame(self.main)
        self.frame_title.pack(pady=10)

        self.title = tk.Label(self.frame_title, text="Sentiment Analysis Results", font=('Arial', 24))
        self.title.pack()

        self.frame_results = tk.Frame(self.main)
        self.frame_results.pack(pady=10)

        self.text_to_analyze = tk.Text(self.frame_results, width=50, height=10)
        self.text_to_analyze.pack(side=tk.LEFT, padx=5, pady=5)

        self.results_label = tk.Label(self.frame_results, text="Results:")
        self.results_label.pack(side=tk.LEFT, padx=5, pady=5)

        self.results_text = tk.Text(self.frame_results, width=50, height=10)
        self.results_text.pack(side=tk.LEFT, padx=5, pady=5)

    def analyze_text(self):
        text = self.input_text.get("1.0", tk.END)
        sentiment_scores = self.sia.polarity_scores(text)
        self.results_text.delete('1.0', tk.END)
        self.results_text.insert(tk.END, str(sentiment_scores))

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.app = Settings(self)
        self.app.settings.pack()

def start_app():
    app = Application()
    app.mainloop()

if __name__ == '__main__':
    start_app()



# src/main.py

import src.settings.main



# src/main.py

# src/main.py is empty
# We don't need any code here because we're already analyzing text in src/settings.py
