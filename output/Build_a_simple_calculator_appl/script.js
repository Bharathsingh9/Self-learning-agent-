javascript
// script.js

document.addEventListener("keydown", function(e) {
    if (e.key === 'Escape') {
        clearDisplay();
    }
});

document.addEventListener("keydown", function(e) {
    if (e.key === 'Backspace') {
        backspace();
    }
});

let displayValue = "";
let previousValue = "";
let operator = "";

function updateDisplay(value) {
    displayValue += value.target.innerText;
    document.getElementById("display").innerText = displayValue;
}

function calculate() {
    let value = eval(displayValue);
    displayValue = value.toString();
    document.getElementById("display").innerText = displayValue;
    previousValue = displayValue;
    displayValue = "";
}

function add() {
    previousValue = parseFloat(displayValue);
    displayValue = "";
    operator = "add";
}

function subtract() {
    previousValue = parseFloat(displayValue);
    displayValue = "";
    operator = "subtract";
}

function multiply() {
    previousValue = parseFloat(displayValue);
    displayValue = "";
    operator = "multiply";
}

function divide() {
    previousValue = parseFloat(displayValue);
    displayValue = "";
    operator = "divide";
}

function clearDisplay() {
    displayValue = "";
    document.getElementById("display").innerText = "";
    previousValue = "";
    operator = "";
}

function backspace() {
    displayValue = displayValue.slice(0, -1);
    document.getElementById("display").innerText = displayValue;
}

function equals() {
    let value = eval(displayValue);
    displayValue = value.toString();
    document.getElementById("display").innerText = displayValue;
    previousValue = displayValue;
    displayValue = "";
}

window.addEventListener("load", function() {
    document.getElementById("add").addEventListener("click", add);
    document.getElementById("subtract").addEventListener("click", subtract);
    document.getElementById("multiply").addEventListener("click", multiply);
    document.getElementById("divide").addEventListener("click", divide);
    document.getElementById("equals").addEventListener("click", equals);
    document.getElementById("clear").addEventListener("click", clearDisplay);
    document.getElementById("backspace").addEventListener("click", backspace);
    document.getElementById("0").addEventListener("click", updateDisplay);
    document.getElementById("1").addEventListener("click", updateDisplay);
    document.getElementById("2").addEventListener("click", updateDisplay);
    document.getElementById("3").addEventListener("click", updateDisplay);
    document.getElementById("4").addEventListener("click", updateDisplay);
    document.getElementById("5").addEventListener("click", updateDisplay);
    document.getElementById("6").addEventListener("click", updateDisplay);
    document.getElementById("7").addEventListener("click", updateDisplay);
    document.getElementById("8").addEventListener("click", updateDisplay);
    document.getElementById("9").addEventListener("click", updateDisplay);
    document.getElementById("decimal").addEventListener("click", updateDisplay);
});
