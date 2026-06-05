javascript
const path = require('path');
const chai = require('chai');
const assert = chai.assert;
const { JSDOM } = require('jsdom');
const fs = require('fs');

describe('Calculator', () => {
  it('should display the initial value on the calculator', () => {
    const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
    const dom = new JSDOM(html);
    const display = dom.window.document.getElementById('display');
    const result = dom.window.eval("(function(){})()");
    display.value = '';
    dom.window.eval("display.value=getDisplayValue(operand)");
    assert.equal(display.value, '');
  });

  it('should add two numbers correctly', () => {
    const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
    const dom = new JSDOM(html);
    const display = dom.window.document.getElementById('display');
    const result = dom.window.eval("(function(){})()");
    display.value = '5';
    dom.window.eval('add(display.value)');
    assert.equal(display.value, 10);
  });

  it('should subtract two numbers correctly', () => {
    const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
    const dom = new JSDOM(html);
    const display = dom.window.document.getElementById('display');
    const result = dom.window.eval("(function(){})()");
    display.value = '5';
    dom.window.eval('subtract(display.value)');
    assert.equal(display.value, 0);
  });

  it('should multiply two numbers correctly', () => {
    const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
    const dom = new JSDOM(html);
    const display = dom.window.document.getElementById('display');
    const result = dom.window.eval("(function(){})()");
    display.value = '5';
    dom.window.eval('multiply(display.value)');
    assert.equal(display.value, 25);
  });

  it('should divide two numbers correctly', () => {
    const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
    const dom = new JSDOM(html);
    const display = dom.window.document.getElementById('display');
    const result = dom.window.eval("(function(){})()");
    display.value = '10';
    dom.window.eval('divide(display.value)');
    assert.equal(display.value, 0.5);
  });

  it('should handle division by zero correctly', () => {
    const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
    const dom = new JSDOM(html);
    const display = dom.window.document.getElementById('display');
    const result = dom.window.eval("(function(){})()");
    display.value = '10';
    dom.window.eval("display.value=divide(display.value, 0)");
    assert.equal(display.value, "Error: Division by zero");
  });
});
