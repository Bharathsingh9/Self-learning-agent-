javascript
// static/js/script.js

// Function to format numbers with commas
function formatNumber(num) {
  return num.toLocaleString();
}

// Function to convert infix to postfix
function toPostfix(infix) {
  const precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
  };
  const output = [];
  const stack = [];

  for (let i = 0; i < infix.length; i++) {
    const char = infix[i];

    if (char === ' ' || char === '\n') {
      continue;
    }

    if (precedence[char] === undefined) {
      if (char === '.') {
        output.push(char);
      } else {
        output.push(char);
      }
    } else if (stack.length > 0 && precedence[char] <= precedence[stack[stack.length - 1]]) {
      while (stack.length > 0 && precedence[char] <= precedence[stack[stack.length - 1]]) {
        output.push(stack.pop());
      }
      stack.push(char);
    } else {
      stack.push(char);
    }

    while (stack.length > 0 && Number.isNaN(Number(output[output.length - 1])) && Number.isNaN(Number(output[output.length - 2]))) {
      output.pop();
    }
  }

  while (stack.length > 0) {
    output.push(stack.pop());
  }

  return output.join('');
}

class Calculator {
  constructor(inputField, display) {
    this.inputField = inputField;
    this.display = display;
    this.postfix = '';
  }

  updateExpression() {
    this.postfix = toPostfix(this.inputField.value);
  }

  updateDisplay() {
    const expression = this.inputField.value;
    const result = this.evaluatePostfix(this.postfix);
    if (result === 'Error') {
      this.display.value = '';
      this.display.style.color = 'red';
    } else {
      this.display.value = formatNumber(result);
      this.display.style.color = 'black';
    }
  }

  evaluatePostfix(postfix) {
    const operators = '+-*/';
    const output = [];
    const stack = [];

    for (const char of postfix) {
      if (operators.includes(char)) {
        const operand2 = output.pop();
        const operand1 = output.pop();
        if (char === '+') {
          output.push(operand1 + operand2);
        } else if (char === '-') {
          output.push(operand1 - operand2);
        } else if (char === '*') {
          output.push(operand1 * operand2);
        } else if (char === '/') {
          output.push(operand1 / operand2);
        }
      } else if (char === '.') {
        output.push(char);
      } else {
        output.push(parseFloat(char));
      }
    }

    return output[0];
  }

  clear() {
    this.inputField.value = '';
    this.display.value = '';
    this.postfix = '';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const inputField = document.getElementById('input-field');
  const display = document.getElementById('display');
  const calculator = new Calculator(inputField, display);

  // Event listeners for buttons
  document.querySelectorAll('.button').forEach((button) => {
    button.addEventListener('click', () => {
      const text = button.textContent;
      if (['+', '-', '*', '/', '='].includes(text)) {
        calculator.updateExpression();
        calculator.updateDisplay();
      } else if (text === 'Clear') {
        calculator.clear();
      } else {
        inputField.value += text;
      }
      if (inputField.value.includes('=')) {
        const equalIndex = inputField.value.indexOf('=');
        inputField.value = inputField.value.substring(0, equalIndex) + calculator.evaluatePostfix(toPostfix(inputField.value.substring(0, equalIndex))) + '+' + inputField.value.substring(equalIndex + 2);
        calculator.updateExpression();
        calculator.updateDisplay();
      }
    });
  });

  window.onresize = () => {
    const body = document.querySelector('body');
    body.style.fontSize = `${body.parentElement.offsetHeight * 0.02}px`;
  };
});



<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Scientific Calculator</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="calculator">
    <input id="input-field" type="text" />
    <div id="display"></div>
    <div id="buttons">
      <button class="button" id="clear-button">Clear</button>
      <button class="button" id="backspace-button">&larr;</button>
      <button class="button" id="pi-button">π</button>
      <button class="button" id="sin-button">sin</button>
      <button class="button" id="cos-button">cos</button>
      <button class="button" id="tan-button">tan</button>
    </div>
    <div id="number-buttons">
      <button class="button" id="seven-button">7</button>
      <button class="button" id="eight-button">8</button>
      <button class="button" id="nine-button">9</button>
      <button class="button" id="div-button">/</button>
      <button class="button" id="four-button">4</button>
      <button class="button" id="five-button">5</button>
      <button class="button" id="six-button">6</button>
      <button class="button" id="mul-button">*</button>
      <button class="button" id="one-button">1</button>
      <button class="button" id="two-button">2</button>
      <button class="button" id="three-button">3</button>
      <button class="button" id="minus-button">-</button>
      <button class="button" id="zero-button">0</button>
      <button class="button" id="decimal-button">.</button>
      <button class="button" id="plus-button">+</button>
    </div>
    <div id="operator-buttons">
      <button class="button" id="power-button">^</button>
      <button class="button" id="equal-button">=</button>
      <button class="button" id="percent-button">%</button>
      <button class="button" id="sqrt-button">√</button>
      <button class="button" id="log-button">log</button>
    </div>
  </div>

  <script src="script.js"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      font-size: 2rem;
    }

    #calculator {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
    }

    #input-field {
      width: 100%;
      padding: 1rem;
      font-size: 2rem;
      border: none;
      border-radius: 0.5rem;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    #display {
      width: 100%;
      padding: 1rem;
      font-size: 3rem;
      border: none;
      border-radius: 0.5rem;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    #buttons {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-evenly;
      width: 100%;
      margin: 1rem 0;
    }

    .button {
      width: 40%;
      padding: 1rem;
      font-size: 1.5rem;
      border: none;
      border-radius: 0.5rem;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .button:hover {
      cursor: pointer;
      transform: scale(1.1);
      background-color: #f2f2f2;
    }
  </style>
</body>
</html>



/* styles.css */

body {
  /* Your styles here */
}

#calculator {
  /* Your styles here */
}

#input-field {
  /* Your styles here */
}

#display {
  /* Your styles here */
}

#buttons {
  /* Your styles here */
}

.button {
  /* Your styles here */
}

.button:hover {
  /* Your styles here */
}


Please note that some CSS styles are missing in the above code and would need to be added. The styles can be added in the `styles.css` file.