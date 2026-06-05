# import necessary libraries
from tkinter import *
from tkinter import ttk
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import filedialog
import os

# Download required NLTK data
nltk.download('vader_lexicon')

# Create the main window
root = Tk()
root.title('Sentiment Analyzer')

# Create a frame for the input field
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill="both", expand=True)

# Create input field
input_text = tk.Text(input_frame, height=5, width=60)
input_text.pack(side=tk.LEFT, padx=10, pady=10)
input_button = ttk.Button(input_frame, text="Analyze Text", command=lambda: analyze_text(input_text.get('1.0', 'end-1c')))
input_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a frame for the output field
output_frame = ttk.Frame(root, padding="10")
output_frame.pack(fill="both", expand=True)

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_text(text):
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        sentiment_label = "Positive"
    elif compound_score <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    sentiment_label_value = f"Compound Score: {round(compound_score, 2)}\nSentiment: {sentiment_label}"
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, sentiment_label_value)

# Create output field
output_text = tk.Text(output_frame, height=5, width=60)
output_text.pack(side=tk.LEFT, padx=10, pady=10)

# Create a frame for the file input
file_frame = ttk.Frame(root, padding="10")
file_frame.pack(fill="both", expand=True)

# Create file input field and button
file_label = tk.Label(file_frame, text="Or, you can upload a text file:")
file_label.pack(side=tk.LEFT, padx=10, pady=10)
file_button = ttk.Button(file_frame, text="Browse File", command=lambda: open_file(input_text))
file_button.pack(side=tk.LEFT, padx=10, pady=10)

def open_file(text_field):
    filename = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
    if filename:
        file_content = open(filename, 'r').read()
        text_field.delete('1.0', tk.END)
        text_field.insert(tk.END, file_content)
        analyze_text(file_content)

# Run the main loop
root.mainloop()

# Note: This code assumes that you have the necessary NLTK data downloaded by running `nltk.download('vader_lexicon')`. 
# The Flask, PyQt and Tkinter are not required for the UI in this project, but you may use them if you prefer other UI frameworks.