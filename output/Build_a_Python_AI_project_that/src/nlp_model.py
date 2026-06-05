python
# src/nlp_model.py
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import spacy
import streamlit as st
import pickle

# Initialize spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load pre-trained VADER model
sia = SentimentIntensityAnalyzer()

def analyze_text(text):
    """
    Analyze sentiment and extract entities from the input text.
    """
    # Process the input text using spaCy's English model
    doc = nlp(text)
    
    # Initialize a dictionary to store sentiment and entity results
    results = {
        "sentiment": None,
        "entities": []
    }
    
    # Analyze sentiment using VADER
    sentiment_scores = sia.polarity_scores(text)
    results["sentiment"] = "Positive" if sentiment_scores["compound"] > 0 else "Negative" if sentiment_scores["compound"] < 0 else "Neutral"
    
    # Extract entities from the input text
    for ent in doc.ents:
        results["entities"].append({
            "text": ent.text,
            "label": ent.label_
        })
    
    return results

def save_model(model):
    """
    Save the NLP model to a file using pickle.
    """
    with open("nlp_model.pkl", "wb") as file:
        pickle.dump(model, file)

def load_model():
    """
    Load a saved NLP model from a file using pickle.
    """
    with open("nlp_model.pkl", "rb") as file:
        return pickle.load(file)
