python
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sentiment_analysis",
    version="1.0",
    packages=find_packages(),
    url="https://github.com/your-github-username/sentiment-analysis",
    license="MIT",
    author="Your Name",
    author_email="your@email.com",
    description="A simple sentiment analysis project using NLP and machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "nltk",
        "pandas",
        "numpy",
        "sklearn",
        "matplotlib",
        "tornado",
        "flask",
        "vaderSentiment"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires=">=3.8",
)
