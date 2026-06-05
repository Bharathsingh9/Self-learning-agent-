python
from flask import Flask, request, jsonify
from routes.sentiment import Sentiment
from routes.utils import extract_text
import json

app = Flask(__name__)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_text():
    text = request.args.get('text') or request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    sentiment_result = Sentiment().analyze(extract_text(text))
    
    return jsonify({
        'positive': sentiment_result['positive'],
        'negative': sentiment_result['negative'],
        'neutral': sentiment_result['neutral'],
        'compound': sentiment_result['compound']
    })

if __name__ == '__main__':
    app.run(debug=True)
