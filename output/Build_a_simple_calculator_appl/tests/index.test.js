javascript
const assert = require('assert');
const { JSDOM } = require('jsdom');

describe('Calculator Application', () => {
  it('displays the result of a basic operation', () => {
    const dom = new JSDOM('<html><body><div id="display">0</div><input type="text" id="expression"></body></html>');
    const document = dom.window.document;
    document.getElementById('display').innerHTML = '0';
    document.getElementById('expression').value = '1 + 2';
    const display = dom.window.document.getElementById('display');
    const expression = dom.window.document.getElementById('expression');
    dom.window.eval(expression.value);
    assert.strictEqual(display.innerHTML, '3');
  });

  it('displays an error for division by zero', () => {
    const dom = new JSDOM('<html><body><div id="display">0</div><input type="text" id="expression"></body></html>');
    const document = dom.window.document;
    document.getElementById('display').innerHTML = '0';
    document.getElementById('expression').value = '1 / 0';
    const display = dom.window.document.getElementById('display');
    const expression = dom.window.document.getElementById('expression');
    dom.window.eval(expression.value);
    assert.strictEqual(display.innerHTML, 'Error: Division by zero');
  });

  it('displays an error for invalid input', () => {
    const dom = new JSDOM('<html><body><div id="display">0</div><input type="text" id="expression"></body></html>');
    const document = dom.window.document;
    document.getElementById('display').innerHTML = '0';
    document.getElementById('expression').value = 'a + b';
    const display = dom.window.document.getElementById('display');
    const expression = dom.window.document.getElementById('expression');
    dom.window.eval(expression.value);
    assert.strictEqual(display.innerHTML, 'Error: Invalid input');
  });

  it('deletes the current input', () => {
    const dom = new JSDOM('<html><body><div id="display">0</div><input type="text" id="expression" value="1 + 2"></body></html>');
    const document = dom.window.document;
    document.getElementById('display').innerHTML = '0';
    const display = dom.window.document.getElementById('display');
    const expression = dom.window.document.getElementById('expression');
    expression.value = '';
    expression.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
    expression.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
    assert.strictEqual(display.innerHTML, '0');
  });

  it('updates the display in real-time as the user types', () => {
    const dom = new JSDOM('<html><body><div id="display">0</div><input type="text" id="expression"></body></html>');
    const document = dom.window.document;
    document.getElementById('display').innerHTML = '0';
    const display = dom.window.document.getElementById('display');
    const expression = dom.window.document.getElementById('expression');
    expression.value = '1 + 2';
    display.innerHTML = '1 + 2';
    expression.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
    expression.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
    assert.strictEqual(display.innerHTML, '3');
  });
});
