shell
#!/bin/bash

# Install Python and pip packages
pip install pip --upgrade
pip install -U nltk spacy

# Download required NLTK data
python -m nltk.downloader vader_lexicon
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md

# Confirm the installations
echo "NLTK and vader_lexicon installed successfully."
echo "spaCy and English models installed successfully."
