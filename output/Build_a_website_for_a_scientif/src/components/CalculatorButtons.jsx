javascript
import React, { useState } from 'react';
import mathjs from 'mathjs';

const CalculatorButtons = () => {
    const [result, setResult] = useState('');
    const [equation, setEquation] = useState('');
    const [history, setHistory] = useState([]);
    const [display, setDisplay] = useState('0');

    const clearEquation = () => {
        setResult('');
        setEquation('');
    };

    const clearHistory = () => {
        setHistory([]);
    };

    const handleDigit = (digit) => {
        display === '0' ? setDisplay(digit) : setDisplay(display + digit);
        setEquation(equation + digit);
    };

    const handleOperation = (operation) => {
        setEquation(equation + operation);
        setDisplay(display + operation);
    };

    const calculate = () => {
        const result = mathjs.evaluate(equation);
        setHistory([...history, equation + ' = ' + result]);
        setResult(result.toString());
        setDisplay(result.toString());
    };

    const backspace = () => {
        let currentValue = display.slice(0, -1);
        if (currentValue === '') {
            currentValue = '0';
        }
        setDisplay(currentValue);
        setEquation(equation.slice(0, -1));
    };

    return (
        <div>
            <div className="calculator-screen">
                {result || history[history.length - 1] ? (
                    <p className="result">{result || history[history.length - 1]}</p>
                ) : (
                    <p className="result display">{display}</p>
                )}
            </div>
            <div className="calculator-keys">
                {['7', '8', '9'].map((digit) => (
                    <button key={digit} onClick={() => handleDigit(digit)}>
                        {digit}
                    </button>
                ))}
                <button onClick={() => handleOperation('/')}>/</button>
                {['4', '5', '6'].map((digit) => (
                    <button key={digit} onClick={() => handleDigit(digit)}>
                        {digit}
                    </button>
                ))}
                <button onClick={() => handleOperation('*')}>*</button>
                {['1', '2', '3'].map((digit) => (
                    <button key={digit} onClick={() => handleDigit(digit)}>
                        {digit}
                    </button>
                ))}
                <button onClick={() => handleOperation('-')}>-</button>
                {['0', '.', '+'].map((digit) => (
                    <button key={digit} onClick={() => handleDigit(digit)}>
                        {digit}
                    </button>
                ))}
                <button onClick={() => handleOperation('+')}>+</button>
                <button onClick={backspace}>DEL</button>
                <button onClick={calculate} className="operator">
                    =
                </button>
                <button onClick={clearEquation}>C</button>
                <button onClick={() => setDisplay('')}>+</button>
                <button onClick={clearHistory}>History</button>
            </div>
        </div>
    );
};

export default CalculatorButtons;
