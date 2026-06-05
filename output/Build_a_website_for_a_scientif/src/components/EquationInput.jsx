javascript
import React, { useState } from 'react';
import { Equation } from 'mathjs';

const EquationInput = () => {
  const [inputEquation, setInputEquation] = useState('');
  const [result, setResult] = useState('');

  const handleInput = (e) => {
    setInputEquation(e.target.value);
  };

  const handleCalculate = () => {
    try {
      const mathEquation = new Equation(inputEquation);
      const solve = mathEquation.solve();
      const result = solve.toTex();
      setResult(`The final answer is: ${result}`);
      document.getElementById('result').focus();
    } catch (error) {
      if (error instanceof Error) {
        if (error.message.includes('undefined')) {
          setResult('Undefined variable in equation');
        } else {
          setResult(`An error occurred: ${error.message}`);
        }
        document.getElementById('error-message').focus();
      }
    }
  };

  return (
    <div className="equation-input">
      <h2>Scientific Calculator</h2>
      <div className="input-panel">
        <input
          type="text"
          className="equation"
          id="equation-input"
          value={inputEquation}
          onChange={handleInput}
          placeholder="Enter your equation here..."
          onKeyPress={(e) => {
            if (e.key === 'Enter') {
              handleCalculate();
            }
          }}
        />
        <button className="calculate" onClick={handleCalculate}>
          Calculate
        </button>
      </div>
      <div className="output-panel">
        <h3>Result:</h3>
        <p id="result"></p>
        <p id="error-message"></p>
      </div>
      <div className="help-panel">
        <p>Supported functions: sin, cos, tan, log, exp, sqrt, pow</p>
        <p>Supported symbols: x, y, pi, e</p>
        <h3>Examples:</h3>
        <ul>
          <li>sin(x)</li>
          <li>cos(x)^2 + sin(x)^2</li>
          <li>e^(x^2)</li>
          <li>ln(x)</li>
        </ul>
      </div>
    </div>
  );
};

export default EquationInput;


Note: This code assumes you have already set up a React environment and have included the Math.js library.