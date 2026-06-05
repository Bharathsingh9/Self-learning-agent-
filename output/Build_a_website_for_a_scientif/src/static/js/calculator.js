javascript
// src/static/js/calculator.js
const expression = document.getElementById('expression');
const result = document.getElementById('result');
const calculateButton = document.getElementById('calculate-button');
const clearButton = document.getElementById('clear-button');

let currentExpression = '';

calculateButton.addEventListener('click', calculate);
clearButton.addEventListener('click', clear);

// Number buttons
document.querySelectorAll('.num-button').forEach(button => {
    button.addEventListener('click', () => {
        currentExpression += button.textContent;
        expression.value = currentExpression;
    });
});

// Trigonometric buttons
document.querySelectorAll('.sin-button, .cos-button, .tan-button').forEach(button => {
    button.addEventListener('click', () => {
        currentExpression += button.textContent;
        expression.value = currentExpression;
    });
});

// Exponent buttons
document.querySelectorAll('.exp-button, .sqrt-button').forEach(button => {
    button.addEventListener('click', () => {
        currentExpression += button.textContent;
        expression.value = currentExpression;
    });
});

// Memory buttons
document.querySelectorAll('.mem-plus-button, .mem-minus-button').forEach(button => {
    button.addEventListener('click', () => {
        currentExpression += button.textContent;
        expression.value = currentExpression;
    });
});

// Memory recall button
document.getElementById('mem-recall-button').addEventListener('click', () => {
    currentExpression += "M";
    expression.value = currentExpression;
});

// Function buttons
document.getElementById('fact-button').addEventListener('click', () => {
    currentExpression += "!"; // not a factorial, since Math.factorial is not possible
    expression.value = currentExpression;
});
document.getElementById('pi-button').addEventListener('click', () => {
    currentExpression += "π";
    expression.value = currentExpression;
});
document.getElementById('e-button').addEventListener('click', () => {
    currentExpression += "e";
    expression.value = currentExpression;
});

// Operator buttons
document.querySelectorAll('.add-button, .subtract-button, .multiply-button, .divide-button').forEach(button => {
    button.addEventListener('click', () => {
        currentExpression += button.textContent;
        expression.value = currentExpression;
    });
});

function calculate() {
    try {
        const result = eval(expression.value);
        updateDisplay(result);
    } catch (error) {
        updateDisplay("Error");
    }
}

function clear() {
    currentExpression = '';
    expression.value = '';
}

function updateDisplay(value) {
    result.textContent = value.toString();
    currentExpression = value.toString();
}



/* src/static/css/style.css */
body {
    font-family: monospace;
}

#calculator-container {
    width: 500px;
    height: 500px;
    border: 1px solid black;
    padding: 20px;
}

#expression {
    width: 100%;
    height: 20px;
    font-size: 24px;
    padding: 10px;
    border: 1px solid black;
}

#result {
    width: 100%;
    height: 40px;
    font-size: 36px;
    padding: 10px;
    border: 1px solid black;
}

#controls {
    margin-top: 20px;
}

.button {
    width: 60px;
    height: 40px;
    font-size: 18px;
    margin: 5px;
}

.button:hover {
    background-color: #ccc;
}



<!-- src/static/js/templates/calculator.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>Scientific Calculator</title>
</head>
<body>
    <div id="calculator-container">
        <input type="text" id="expression" placeholder="Enter equation...">
        <p id="result"></p>
        <div id="controls">
            <button class="button add-button" type="button">+</button>
            <button class="button subtract-button" type="button">-</button>
            <button class="button multiply-button" type="button">*</button>
            <button class="button divide-button" type="button="/">/</button>
            <button class="button" type="button"></button>
            <button class="button" type="button"></button>
            <button class="button" type="button"></button>
            <button class="button" type="button"></button>
            <button class="button fact-button" type="button">!</button>
            <button class="button sin-button" type="button">sin</button>
            <button class="button exp-button" type="button">e^x</button>
            <button class="button sqrt-button" type="button">√</button>
            <button class="button cos-button" type="button">cos</button>
            <button class="button" type="button"></button>
            <button class="button" type="button"></button>
            <button class="button" type="button"></button>
            <button class="button exp-button tan-button" type="button">tan</button>
        </div>
        <div id="memory-controls">
            <button class="button mem-plus-button" type="button">M+</button>
            <button class="button" type="button"> </button>
            <button class="button" type="button"> </button>
            <button class="button" type="button"></button>
            <button class="button" type="button"> </button>
            <button class="button" type="button"> </button>
            <button class="button mem-minus-button" type="button">M-</button>
        </div>
        <button class="button" id="clear-button" type="button">C</button>
        <button class="button" id="calculate-button" type="button">=</button>
        <button class="button" type="button">7</button>
        <button class="button" type="button">8</button>
        <button class="button" type="button">9</button>
        <button class="button" type="button">4</button>
        <button class="button" type="button">5</button>
        <button class="button" type="button">6</button>
        <button class="button" type="button">1</button>
        <button class="button" type="button">2</button>
        <button class="button" type="button">3</button>
        <button class="button" type="button">0</button>
        <button class="button" type="button">.</button>
    </div>
    <script src="{{ url_for('static', filename='js/calculator.js') }}"></script>
</body>
</html>
