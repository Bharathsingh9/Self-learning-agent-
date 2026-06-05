javascript
// src/js/math.js
class Calculator {
  constructor() {
    this.memory = 0;
    this.lastOperation = '';
  }

  add(num1, num2) {
    return num1 + num2;
  }

  subtract(num1, num2) {
    return num1 - num2;
  }

  multiply(num1, num2) {
    return num1 * num2;
  }

  divide(num1, num2) {
    if (num2 === 0) {
      return 'Error: Division by zero is not allowed';
    }
    return num1 / num2;
  }

  operate(oper, num1, num2) {
    switch (oper) {
      case '+':
        return this.add(num1, num2);
      case '-':
        return this.subtract(num1, num2);
      case '*':
        return this.multiply(num1, num2);
      case '/':
        return this.divide(num1, num2);
      default:
        return 'Error: Invalid operation';
    }
  }
}

const calculator = new Calculator();

export default calculator;
