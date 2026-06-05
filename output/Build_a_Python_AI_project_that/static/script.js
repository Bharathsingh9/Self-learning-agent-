javascript
// static/script.js

function displayResult(result) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerText = result;
}

function displayError(error) {
  const errorDiv = document.getElementById('error');
  errorDiv.innerText = error;
}

function displayStatus(status) {
  const statusDiv = document.getElementById('status');
  statusDiv.innerText = status;
}

document.addEventListener('DOMContentLoaded', () => {
  const inputBox = document.getElementById('input');
  const analyzeButton = document.getElementById('analyze');

  analyzeButton.addEventListener('click', async () => {
    const userInput = inputBox.value.trim();
    if (userInput === '') {
      displayError('Please enter some text');
      return;
    }

    const response = await fetch('/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: userInput }),
    });

    if (!response.ok) {
      displayError('Failed to analyze sentiment');
      return;
    }

    const result = await response.json();
    displayResult(result);
  });
});
