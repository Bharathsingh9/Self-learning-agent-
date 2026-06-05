jsx
import React, { useState, useEffect } from 'react';
import {
  MathJax,
  MathJaxContext,
} from 'better-react-mathjax';
import mathJs from 'mathjs';

function ResultDisplay({ expression, value, isFunction, showExpression, isResultValid }) {
  const [output, setOutput] = useState('');

  useEffect(() => {
    if (expression && showExpression) {
      calculateExpression();
    }
    if (value && !isFunction) {
      calculateValue();
    }
  }, [expression, showExpression, value]);

  useEffect(() => {
    const mathjaxConfig = {
      extensions: ['tex2jax.js'],
      tex2jax: {
        inlineMath: [['$', '$'], ['`', `'`,]],
        displayMath: [['$$', '$$'], ['$*', '$*']],
      },
      'HTML-CSS': {
        // options
        availableFonts: ['TeX'],
        imageFontDir: '../mathjax/fonts/',
      },
    };
    MathJax = MathJaxContext.create({
      options: mathjaxConfig,
    });
  }, []);

  const calculateExpression = () => {
    try {
      const result = mathJs.evaluate(expression);
      if (result.type === 'Function') {
        setOutput(`${MathJax.tex2svg(result.toString())} (x)`);
      } else {
        setOutput(MathJax.tex2svg(`${expression} = ${result.toTex()}`));
      }
    } catch (error) {
      setOutput(`Invalid: ${(error.message)}`);
    }
  };

  const calculateValue = () => {
    try {
      const result = mathJs.evaluate(expression);
      setOutput(MathJax.tex2svg(`${expression} = ${result.toTex()}`));
    } catch (error) {
      setOutput(`Invalid: ${(error.message)}`);
    }
  };

  return (
    <div id="math-output">
      {output}
      {isResultValid ? (
        ''
      ) : (
        <span style={{ color: 'red' }}>* Invalid input * </span>
      )}
    </div>
  );
}

export default ResultDisplay;
