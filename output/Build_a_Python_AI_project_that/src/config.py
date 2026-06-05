python
# src/config.py

import os

class Config:
    DEBUG = False
    TESTING = False

    # Project Paths
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_ROOT = os.path.join(PROJECT_ROOT, 'app')
    DATA_ROOT = os.path.join(PROJECT_ROOT, 'data')
    MODELS_ROOT = os.path.join(PROJECT_ROOT, 'models')

    # NLP Library
    LANGUAGE_MODEL = 'en_core_web_sm'
    SPACY_MODEL_DIRECTORY = f'{PROJECT_ROOT}/models'

    # Text Preprocessing
    STOPWORDS = ['is', 'was', 'were', 'are', 'be', 'been', 'being']
    PUNCTUATIONS = ['.', ',', '?', '!', ':', ';', '-', '(', ')', '[', ']']
    SPECIAL_CHARACTERS = ['@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '~']
