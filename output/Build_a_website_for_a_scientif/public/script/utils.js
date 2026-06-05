javascript
// utils.js

class Utils {
  static renderTemplate(templateId, data = {}) {
    const template = document.getElementById(templateId);
    return template.innerHTML.replace(/{{(.*?)}}/g, (match, key) => {
      return data[key] || '';
    });
  }

  static addEventListeners() {
    const buttons = document.querySelectorAll('#calculator > button');
    buttons.forEach((button, index) => {
      button.onclick = this.buttonClickHandler(index);
    });
  }

  static buttonClickHandler(index) {
    const buttonElement = document.querySelector(`#calculator > button:nth-child(${index + 1})`);
    const text = buttonElement.textContent;

    const display = document.querySelector('#calculator .result');
    switch (text) {
      case '.':
        if (!display.textContent.includes('.')) {
          display.textContent += '.';
        }
        break;
      case 'C':
        display.textContent = '';
        break;
      case '=':
      case '←':
        display.textContent = display.textContent.slice(0, -1);
        break;
      default:
        display.textContent += text;
    }
  }

  static evaluateExpression(expression) {
    try {
      const result = Function('"use strict";return (' + expression + ')')();
      return result;
    } catch (error) {
      alert('Invalid expression');
    }
  }
}

export default Utils;



// index.js
import Utils from './utils.js';

Utils.addEventListeners();

document.querySelector('#calculator-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const input = document.querySelector('#input-expression');
  const result = Utils.evaluateExpression(input.value);
  document.querySelector('.result-2').textContent = result;
  input.value = '';
});
