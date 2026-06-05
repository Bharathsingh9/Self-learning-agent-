javascript
// src/js/script.js

// Store the current calculation in a string
let calculation = '';

// Store the result in a variable
let result = 0;

// Function to handle button clicks
function handleButtonClick(value) {
    // If the current calculation is a number, append the new value
    if (!isNaN(calculation) && !isNaN(value)) {
        calculation += value;
        document.getElementById('display').innerHTML = calculation;
    } 
    // If the current calculation is not a number, start a new number
    else {
        calculation = value;
        document.getElementById('display').innerHTML = value;
    }
}

// Function to handle operators
function handleOperator(value) {
    // If the current calculation ends with an operator, do nothing
    if (calculation.slice(-1) === '+' || calculation.slice(-1) === '-' || calculation.slice(-1) === '*' || calculation.slice(-1) === '/'){
        window.alert("Error: Too Many Operators");
        document.getElementById('display').innerHTML = '0';
        return;
    }
    else{
        calculation += value;
        document.getElementById('display').innerHTML = calculation;
    }
}

// Function to calculate the result
function calculateResult() {
    try {
        // Perform the calculation
        result = eval(calculation);
        // Update the display
        document.getElementById('display').innerHTML = result;
    } catch (error) {
        // If there is an error, display it to the user
        window.alert("Error: " + error.message);
        document.getElementById('display').innerHTML = '0';
    }
    calculation = result.toString();
}

// Function to reset the calculator
function resetCalculator() {
    calculation = '';
    result = 0;
    document.getElementById('display').innerHTML = '0';
}

// Get references to the display and buttons
const display = document.getElementById('display');
