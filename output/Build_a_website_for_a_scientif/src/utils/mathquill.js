javascript
import MathQuill from 'mathquill/src/mathquill';

// Configuration for MathQuill
const config = {
    // Allow for custom font settings
    mathjaxConfig: {
        // Use MathJax 2.7 configuration
        TeX: {
            extensions: ['color.js'],
            TagSide: 'right',
            TagLineBelow: 'true',
            tags: 'inputs',
            equationNumbers: {
                autoNumber: 'AMS',
            },
        },
    },
    // Allow for hover highlighting
    render: {
        // Render math elements as SVGs
        // Use MathJax to convert equations into SVGs
        mathMLWithSVG: true,
        mhchem: {}
    },
    // Enable or disable specific options
    options: {
        // Enable or disable rendering mathJax
        mathJax: true,
        // Enable or disable rendering mathML
        mathML: true,
        // Enable or disable rendering inline math
        inlineMath: true,
    }
};

// Create MathQuill instance
const mathQuill = MathQuill.init(config);

// Export the MathQuill instance
export default mathQuill;



// src/index.js
import mathQuill from './utils/mathquill';

// Initialize MathQuill on the HTML body element
document.addEventListener('DOMContentLoaded', () => {
    const body = document.querySelector('body');
    MathQuill.Hub.config=config;
    mathQuill.Hub.bind(body);
});

import React from 'react';
import ReactDOM from 'react-dom';

// Create a React app to render MathQuill input field
function App() {
    const [math, setMath] = React.useState('');

    // Handle math input change
    const onChangeHandler = (newMath) => {
        setMath(newMath);
    };

    return (
        <div>
            <MathQuill.Input
                className="math-input"
                math={math}
                onChange={onChangeHandler}
            />
            <div className="math-container">
                <MathQuill.Field
                    className="math-field"
                    math={math}
                />
            </div>
        </div>
    );
}

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);



// package.json
{
  "name": "scientific-calculator",
  "version": "1.0.0",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test"
  },
  "dependencies": {
    "mathquill": "^0.15.0",
    "mathjax": "^2.7.9",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  }
}
