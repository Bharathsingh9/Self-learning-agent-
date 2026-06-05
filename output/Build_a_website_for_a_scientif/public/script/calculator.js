javascript
// Public/script/calculator.js
let currentExpression = '';
let output = '';
let numbers = document.querySelectorAll('.number');
let operators = document.querySelectorAll('.operator');
let equals = document.querySelector('.equals');
let clear = document.querySelector('.clear');
let decimal = document.querySelector('.decimal');
let outputScreen = document.querySelector('.output-screen');

// Event listeners for numbers
numbers.forEach(button => {
  button.addEventListener('click', e => {
    let value = e.target.textContent;
    currentExpression += value;
    output = value;
    outputScreen.textContent = currentExpression;
  });
});

// Event listeners for operators
operators.forEach(button => {
  button.addEventListener('click', e => {
    let value = e.target.textContent;
    currentExpression += value;
    output += ' ' + value + ' ';
    outputScreen.textContent = output;
  });
});

// Event listener for equals
equals.addEventListener('click', () => {
  try {
    output = eval(currentExpression);
    outputScreen.textContent = output;
  } catch (error) {
    outputScreen.textContent = 'Error';
    currentExpression = '';
  }
});

// Event listener for clear
clear.addEventListener('click', () => {
  currentExpression = '';
  output = '';
  outputScreen.textContent = '';
});

// Event listener for decimal
decimal.addEventListener('click', () => {
  let current = currentExpression;
  if (current.includes('.')) {
    return;
  } else {
    currentExpression += '.';
    output += '.';
    outputScreen.textContent = currentExpression;
  }
});
