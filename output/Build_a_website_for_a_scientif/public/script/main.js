javascript
// public/script/main.js

let displayValue = "0";
let previousValue = "";
let operators = {
  "+": (a, b) => a + b,
  "-": (a, b) => a - b,
  "*": (a, b) => a * b,
  "/": (a, b) => b !== 0 ? a / b : Number.POSITIVE_INFINITY,
  "sin": (x) => Number(x) ? Math.sin(x) : "Invalid Input",
  "cos": (x) => Number(x) ? Math.cos(x) : "Invalid Input",
  "tan": (x) => Number(x) ? Math.tan(x) : "Invalid Input",
  "ln": (x) => Number(x) ? Math.log(x) : "Invalid Input",
  "sqrt": (x) => Number(x) && x >= 0 ? Math.sqrt(x) : "Invalid Input"
};

document.getElementById("output").innerText = "0";

document.getElementById("buttons").addEventListener("click", (e) => {
  if (e.target.tagName === "BUTTON") {
    let keyValue = e.target.innerText;

    switch (keyValue) {
      case "Clear":
        displayValue = "0";
        break;
      case "=":
        try {
          let result = eval(previousValue + displayValue);
          document.getElementById("output").innerText = result;
          previousValue = "";
          displayValue = result.toString();
        } catch (error) {
          document.getElementById("output").innerText = "Error";
          previousValue = "";
          displayValue = "0";
        }
        break;
      case "Delete":
        if (displayValue !== "0") {
          displayValue = displayValue.slice(0, -1);
          if (displayValue === "") displayValue = "0";
          document.getElementById("output").innerText = displayValue;
        }
        break;
      case "sin":
      case "cos":
      case "tan":
      case "ln":
      case "sqrt":
        document.getElementById("output").innerText = keyValue;
        previousValue = "";
        displayValue = "";
        break;
      case "e":
        document.getElementById("output").innerText = "e";
        previousValue = "";
        displayValue = "";
        break;
      case "pi":
        document.getElementById("output").innerText = "π";
        previousValue = "";
        displayValue = "";
        break;
      case "C":
        previousValue = "";
        displayValue = "0";
        break;
      default:
        if (displayValue === "0" && keyValue !== ".") {
          displayValue = keyValue;
        } else if (keyValue === "." && !displayValue.includes(".")) {
          displayValue += ".";
        } else {
          previousValue += displayValue;
          previousValue += keyValue;
          displayValue = keyValue;
        }
        document.getElementById("output").innerText = displayValue;
    }
  }
});

document.addEventListener("keydown", (e) => {
  if (e.key.length === 1 && (e.key >= "0" && e.key <= "9" || e.key === "." || e.key === "+" || e.key === "-" || e.key === "*" || e.key === "/")) {
    let keyValue = e.key;
    switch (keyValue) {
      case "c":
      case "C":
        displayValue = "0";
        previousValue = "";
        break;
      case "Enter":
        try {
          let result = eval(previousValue + displayValue);
          document.getElementById("output").innerText = result;
          previousValue = "";
          displayValue = result.toString();
        } catch (error) {
          document.getElementById("output").innerText = "Error";
          previousValue = "";
          displayValue = "0";
        }
        break;
      default:
        if (displayValue === "0" && keyValue !== ".") {
          displayValue = keyValue;
        } else if (keyValue === "." && !displayValue.includes(".")) {
          displayValue += ".";
        } else {
          previousValue += displayValue;
          previousValue += keyValue;
          displayValue = keyValue;
        }
        document.getElementById("output").innerText = displayValue;
    }
  } else if (e.key === "Backspace") {
    if (displayValue !== "0") {
      displayValue = displayValue.slice(0, -1);
      if (displayValue === "") displayValue = "0";
    }
    document.getElementById("output").innerText = displayValue;
  }
});
