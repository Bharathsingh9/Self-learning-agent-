javascript
// operator-keys.js
const keys = document.getElementById('keys');

// Define the keys for the scientific calculator
const operators = [
  {key: '+', html: '+', css: 'btn-operator'},
  {key: '*', html: '*', css: 'btn-operator'},
  {key: '-', html: '-', css: 'btn-operator'},
  {key: '/', html: '/', css: 'btn-operator'},
  {key: 'π', html: 'π', css: 'btn-operator'},
  {key: 'sin', html: 'sin', css: 'btn-operator'},
  {key: 'cos', html: 'cos', css: 'btn-operator'},
  {key: 'tan', html: 'tan', css: 'btn-operator'},
  {key: '*', html: 'exp', css: 'btn-operator'},
  {key: '^', html: '^', css: 'btn-operator'},
  {key: '(', html: '(', css: 'btn-operator'},
  {key: ')', html: ')', css: 'btn-operator'},
];

const numbers = [
  {key: 1, html: 1, css: 'btn-number'},
  {key: 2, html: 2, css: 'btn-number'},
  {key: 3, html: 3, css: 'btn-number'},
  {key: 4, html: 4, css: 'btn-number'},
  {key: 5, html: 5, css: 'btn-number'},
  {key: 6, html: 6, css: 'btn-number'},
  {key: 7, html: 7, css: 'btn-number'},
  {key: 8, html: 8, css: 'btn-number'},
  {key: 9, html: 9, css: 'btn-number'},
  {key: 0, html: 0, css: 'btn-number'},
];

const specialKeys = [
  {key: '.', html: '.', css: 'btn-number'},
  {key: '=', html: '=', css: 'btn-equal'},
  {key: 'C', html: 'C', css: 'btn-clear'},
  {key: 'DEL', html: 'DEL', css: 'btn-delete'},
];

// Create buttons for the scientific calculator
for (let i = 0; i < operators.length; i++) {
  const button = document.createElement('button');
  button.innerHTML = operators[i].html;
  button.classList.add(operators[i].css);
  button.addEventListener('click', () => {eval(operators[i].key)});
  keys.appendChild(button);
}

for (let i = 0; i < numbers.length; i++) {
  const button = document.createElement('button');
  button.innerHTML = numbers[i].html;
  button.classList.add(numbers[i].css);
  button.addEventListener('click', () => appendNumber(numbers[i].key));
  keys.appendChild(button);
}

for (let i = 0; i < specialKeys.length; i++) {
  const button = document.createElement('button');
  button.innerHTML = specialKeys[i].html;
  button.classList.add(specialKeys[i].css);
  button.addEventListener('click', () => handleSpecialKey(specialKeys[i].key));
  keys.appendChild(button);
}

function appendNumber(number) {
  const expression = document.getElementById('expression').textContent;
  const newExpression = expression + number;
  document.getElementById('expression').textContent = newExpression;
}

function handleSpecialKey(key) {
  switch (key) {
    case '=':
      calculate();
      break;
    case 'C':
      clearExpression();
      break;
    case 'DEL':
      deleteDigit();
      break;
  }
}

function calculate() {
  const expression = document.getElementById('expression').textContent;
  const result = eval(expression);
  document.getElementById('expression').textContent = result;
  document.getElementById('result').textContent = 'Result: ' + result;
}

function clearExpression() {
  document.getElementById('expression').textContent = '';
  document.getElementById('result').textContent = '';
}

function deleteDigit() {
  const expression = document.getElementById('expression').textContent;
  const newExpression = expression.slice(0, -1);
  document.getElementById('expression').textContent = newExpression;
}
