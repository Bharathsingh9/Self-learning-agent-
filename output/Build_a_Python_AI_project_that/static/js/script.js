javascript
// Get the input and output elements
const inputElement = document.getElementById('input');
const outputElement = document.getElementById('output');

// Create a function to make the API call to the Python server
async function callPythonServer(text) {
  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: text })
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
  }
}

// Create a function to get the sentiment analysis results
async function getSentiment(text) {
  const data = await callPythonServer(text);
  const sentimentScore = data['sentiment_score'];
  const label = data['sentiment_label'];

  // Update the UI with the sentiment analysis results
  const result = document.getElementById('result');
  const outputText = document.createElement('p');
  outputText.textContent = `Sentiment Score: ${sentimentScore.toFixed(2)} (${label})`;
  result.appendChild(outputText);

  // Update the sentiment plot if available
  const plot = document.getElementById('plot');
  if (data['sentiment_plot']) {
    const plotElement = document.createElement('img');
    plotElement.src = data['sentiment_plot'];
    plot.appendChild(plotElement);
  }
}

// Add event listener to the submit button to get sentiment analysis on user's input
document.getElementById('submit').addEventListener('click', async () => {
  const text = inputElement.value;
  if (text.trim() !== '') {
    await getSentiment(text);
  }
});
