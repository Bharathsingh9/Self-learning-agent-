python
# src/tokenizer.py
import spacy
from spacy import displacy
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    # Lemmatization
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Remove punctuations and special characters
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]

    # Remove empty strings
    tokens = [token for token in tokens if token]

    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    return ' '.join(tokens)

def tokenize_text(text):
    return word_tokenize(text)

def main():
    text = input("Enter text: ")
    print("Preprocessed Text:", preprocess_text(text))
    print("Tokenized Text:", tokenize_text(text))

if __name__ == "__main__":
    main()
