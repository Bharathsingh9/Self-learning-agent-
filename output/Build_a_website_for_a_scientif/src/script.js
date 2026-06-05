javascript
// Get the display element
const display = document.getElementById('display');

// Function to update the display
function updateDisplay(operators) {
  document.getElementById('equals').disabled = false;

  let value = parseFloat(display.value);

  let result = operators.join('');

  if (result === 'NaN' || result === '-') {
    result = '';
  }

  display.value = result;

  if (result === 'Error') {
    display.value = result;
  }

  if (result === 'Infinity') {
    display.value = result;
  }

  if (result === 'NaN') {
    display.value = result;
  }
}

// Function to handle operators
function handleOperators(operator) {
  try {
    const value = parseFloat(display.value);

    if (operator === 'C') {
      display.value = '';
      document.getElementById('equals').disabled = true;
    } else if (operator === 'DEL') {
      let text = display.value.slice(0, -1);
      display.value = text === '' ? 0 : text;
    } else if (operator === '-' || operator === '+' || operator === '/' || operator === '*') {
      if (display.value === '' || display.value === '0' && operator !== '+' && operator !== '-') {
        display.value = display.value;
      } else {
        let text = display.value;
        if (display.value.includes('/') && display.value.includes('/') % 1 > 0) {
          if (text.endsWith('/') || (operator === '+' || operator === '-' || operator === '*' || operator === '-' && text.charAt(0) !== '-')) {
            let text = display.value + operator;
            updateDisplay([text]);
          } else if (operator === '/' || operator === '+' || operator === '-' || operator === '*') {
            let text = display.value + operator;
            updateDisplay([text]);
          } else {
            updateDisplay([0]);
          }
        } else if (display.value.includes('/') && display.value.includes('/') % 1 === 0) {
          if (text.endsWith('/') || (operator === '+' || operator === '-' || operator === '*' || operator === '-' && text.charAt(0) !== '-')) {
            let text = display.value + operator;
            updateDisplay([text]);
          } else if (operator === '/' || operator === '+' || operator === '-' || operator === '*') {
            let text = display.value + operator;
            updateDisplay([text]);
          } else {
            updateDisplay([0]);
          }
        } else if (display.value === '0' && operator === '/' || display.value === '0' && operator === '*') {
          let text = display.value + operator;
          updateDisplay([text]);
        } else if (operator === 'C' || operator === '-' || operator === '+' || operator === '/' || operator === '*') {
          if (display.value === '') {
            let text = display.value + 0;
            updateDisplay([-text]);
          } else {
            if (operator === '+' || operator === '-') {
              let text = '-' + display.value;
              updateDisplay([text]);
            } else {
              let text = display.value + operator;
              updateDisplay([text]);
            }
          }
        } else if (operator === '(') {
          display.value = display.value + '(';
        } else if (operator === ')') {
          let text = display.value;
          let count = 0;
          for (let i = 0; i < text.length; i++) {
            if (text[i] === '(') {
              count++;
            } else if (text[i] === ')' && (display.value !== '' && count === 0)) {
              count--;
              if (count === -1) {
                display.value = text.slice(0, -1);
                break;
              }
            }
          }
        } else if (operator === '*' || operator === '/') {
          if (operator === '*') {
            let text = display.value + operator;
            updateDisplay([text]);
          } else if (operator === '/') {
            let text = display.value + operator;
            updateDisplay([text]);
          }
        } else if (operator === '-') {
          if (display.value === '0') {
            display.value = '-';
          } else {
            let text = display.value + operator;
            updateDisplay([text]);
          }
        } else if (operator === '+') {
          let text = display.value + operator;
          updateDisplay([text]);
        }
        display.value = parseFloat(display.value);
      }
    } else {
      let value = parseFloat(display.value);
      switch (operator) {
        case '√':
          value = Math.sqrt(value);
          display.value = value;
          break;
        case 'sin':
          value = Math.sin(Math.PI * (value / 180));
          display.value = value;
          break;
        case 'cos':
          value = Math.cos(Math.PI * (value / 180));
          display.value = value;
          break;
        case 'tan':
          value = Math.tan(Math.PI * (value / 180));
          display.value = value;
          break;
        default:
          updateDisplay([value]);
      }
    }
  } catch (error) {
    updateDisplay('Error');
  }
}

// Function to handle equals
function handleEquals() {
  try {
    const value = parseFloat(display.value);
    if (value === NaN) {
      updateDisplay('Error');
    } else {
      let text = display.value;
      let result = eval(text);
      display.value = result;
      document.getElementById('equals').disabled = true;
    }
  } catch (error) {
    updateDisplay('Error');
  }
}

// Add event listeners to operators
document.getElementById('button0').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '0';
  }
});

document.getElementById('button1').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '1';
  }
});

document.getElementById('button2').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '2';
  }
});

document.getElementById('button3').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '3';
  }
});

document.getElementById('button4').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '4';
  }
});

document.getElementById('button5').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '5';
  }
});

document.getElementById('button6').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '6';
  }
});

document.getElementById('button7').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '7';
  }
});

document.getElementById('button8').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '8';
  }
});

document.getElementById('button9').addEventListener('click', () => {
  if (display.value === 'Error') {
    display.value = '';
  } else {
    display.value += '9';
  }
});

document.getElementById('equals').addEventListener('click', handleEquals);

document.getElementById('clear').addEventListener('click', () => {
  document.getElementById('equals').disabled = true;
  display.value = '';
});

document.getElementById('negative').addEventListener('click', () => {
  let value = parseFloat(display.value);
  display.value = -value;
});

document.getElementById('multiply').addEventListener('click', () => {
  handleOperators('*');
});

document.getElementById('divide').addEventListener('click', () => {
  handleOperators('/');
});

document.getElementById('subtract').addEventListener('click', () => {
  handleOperators('-');
});

document.getElementById('add').addEventListener('click', () => {
  handleOperators('+');
});

document.getElementById('percent').addEventListener('click', () => {
  let value = parseFloat(display.value);
  value = value / 100;
  if (Object.is(value, NaN) || Object.is(value, -Infinity) || Object.is(value, Infinity)) {
    display.value = 'Error';
  } else {
    display.value = value;
  }
});

document.getElementById('exp').addEventListener('click', () => {
  let value = parseFloat(display.value);
  let result = Math.pow(value, value);
  display.value = result;
});

document.getElementById('sin').addEventListener('click', () => {
  let value = parseFloat(display.value);
  let result = Math.sin(Math.PI * (value / 180));
  display.value = result;
});

document.getElementById('cos').addEventListener('click', () => {
  let value = parseFloat(display.value);
  let result = Math.cos(Math.PI * (value / 180));
  display.value = result;
});

document.getElementById('tan').addEventListener('click', () => {
  let value = parseFloat(display.value);
  let result = Math.tan(Math.PI * (value / 180));
  display.value = result;
});

document.getElementById('sqrt').addEventListener('click', () => {
  let value = parseFloat(display.value);
  let result = Math.sqrt(value);
  display.value = result;
});

document.getElementById('log').addEventListener('click', () => {
  let value = parseFloat(display.value);
  let result = Math.log10(value);
  display.value