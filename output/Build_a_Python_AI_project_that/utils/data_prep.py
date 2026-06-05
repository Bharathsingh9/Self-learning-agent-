python
# utils/data_prep.py

# Import necessary libraries
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import sqlite3

# Connect to database
conn = sqlite3.connect('sentiment_db.db')
c = conn.cursor()

# Function to preprocess text data
def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

# Function to load and preprocess data
def load_data():
    c.execute("SELECT * FROM text_data")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['text', 'sentiment'])
    df['text'] = df['text'].apply(preprocess_text)
    return df

# Function to split data into training and testing sets
def split_data(df):
    X = df['text']
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Function to train and evaluate Naive Bayes model
def train_naive_bayes(X_train, X_test, y_train, y_test):
    vectorizer = TfidfVectorizer()
    X_train_vectors = vectorizer.fit_transform(X_train)
    X_test_vectors = vectorizer.transform(X_test)
    model = MultinomialNB()
    model.fit(X_train_vectors, y_train)
    accuracy = model.score(X_test_vectors, y_test)
    return model, accuracy

# Function to train and evaluate Logistic Regression model
def train_logistic_regression(X_train, X_test, y_train, y_test):
    vectorizer = TfidfVectorizer()
    X_train_vectors = vectorizer.fit_transform(X_train)
    X_test_vectors = vectorizer.transform(X_test)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vectors, y_train)
    accuracy = model.score(X_test_vectors, y_test)
    return model, accuracy

# Function to train and evaluate VADER model
def train_vader(X_train, X_test, y_train, y_test):
    sia = SentimentIntensityAnalyzer()
    X_train_scores = [sia.polarity_scores(text)['compound'] for text in X_train]
    X_test_scores = [sia.polarity_scores(text)['compound'] for text in X_test]
    model = LogisticRegression(max_iter=1000)
    model.fit(np.array(X_train_scores).reshape(-1, 1), y_train)
    accuracy = model.score(np.array(X_test_scores).reshape(-1, 1), y_test)
    return model, accuracy
