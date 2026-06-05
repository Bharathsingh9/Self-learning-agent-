python
# src/models.py

import spacy
from spacy import displacy
import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt

# Load English language model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define a function to perform text preprocessing using spaCy
def preprocess_text(input_text):
    # Process the text using spaCy
    doc = nlp(input_text)
    
    # Extract the text without SpaCy markup
    text = [token.text for token in doc]
    
    # Tokenize the text
    tokens = nlp(input_text)
    
    # Perform part-of-speech tagging for each token
    pos_tags = [(token.text, token.pos_) for token in tokens]
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', input_text)
    
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', input_text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    text = [word for word in text.split() if word.lower() not in stop_words]
    
    # Perform stemming using PorterStemmer
    stemmer = PorterStemmer()
    text = [stemmer.stem(word) for word in text]
    
    # Perform lemmatization using WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    text = [lemmatizer.lemmatize(word) for word in text]
    
    # Join the processed text back into a string
    text = ' '.join(text)
    
    return text

# Define a function to perform sentiment analysis using spaCy
def sentiment_analysis(input_text):
    # Process the text using spaCy
    doc = nlp(input_text)
    
    # Return the sentiment intensity scores for each token
    return [(token.text, token.sentiment) for token in doc]

# Test the functions
if __name__ == "__main__":
    input_text = "I love this hotel!"
    preprocessed_text = preprocess_text(input_text)
    print(preprocessed_text)
    
    sentiment_results = sentiment_analysis(input_text)
    for result in sentiment_results:
        print(result)

This code assumes that spaCy and its models are installed, along with the necessary NLTK data packages. If not, you can install them using pip and nltk:

bash
pip install spacy
python -m spacy download en_core_web_sm
pip install nltk
python -m nltk.downloader stopwords
python -m nltk.downloader wordnet
python -m nltk.downloader punkt
