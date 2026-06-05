bash
#!/bin/bash

# Install necessary NLTK data using the required NLTK packages downloaded via Python
python -m nltk.downloader vader_lexicon
python -m nltk.downloader sentiwordnet
python -m nltk.downloader wordnet

# Download spacy English model
python -m spacy download en_core_web_sm
