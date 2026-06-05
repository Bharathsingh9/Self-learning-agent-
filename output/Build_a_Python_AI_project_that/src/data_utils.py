python
import spacy
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# Initialize spaCy model
nlp = spacy.load("en_core_web_sm")

class DataUtils:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        nltk.download('wordnet')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        text = text.lower()
        doc = nlp(text)

        tokens = []
        for token in doc:
            if not token.is_punct and not token.is_space and not token.like_num:
                if not token.is_stop:
                    if token.pos_ in ['PROPN', 'NOUN', 'VERB', 'ADJ']:
                        tokens.append(tokenlemma_)
                    else:
                        tokens.append(self.lemmatizer.lemmatize(token.text))
                    tokens.append(token.text)

        text = ' '.join(tokens).strip()
        text = re.sub(r'[^\w\s]', '', text)
        return text
