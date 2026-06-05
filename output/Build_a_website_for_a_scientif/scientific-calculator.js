javascript
// scientific-calculator.js
class ScientificCalculator {
  constructor(rootElement) {
    this.rootElement = rootElement;
    this.elements = this.initializeUI();
  }

  initializeUI() {
    return {
      buttons: [
        {
          text: "7",
          class: "digit-button"
        },
        {
          text: "8",
          class: "digit-button"
        },
        {
          text: "9",
          class: "digit-button"
        },
        {
          text: "/",
          class: "operator-button"
        },
        {
          text: "4",
          class: "digit-button"
        },
        {
          text: "5",
          class: "digit-button"
        },
        {
          text: "6",
          class: "digit-button"
        },
        {
          text: "*",
          class: "operator-button"
        },
        {
          text: "1",
          class: "digit-button"
        },
        {
          text: "2",
          class: "digit-button"
        },
        {
          text: "3",
          class: "digit-button"
        },
        {
          text: "-",
          class: "operator-button"
        },
        {
          text: "0",
          class: "digit-button"
        },
        {
          text: ".",
          class: "digit-button"
        },
        {
          text: "=",
          class: "operator-button"
        },
        {
          text: "+",
          class: "operator-button"
        }
      ],
      display: document.createElement("div"),
      equalsButton: {
        element: document.createElement("button"),
        text: "="
      },
      clearButton: {
        element: document.createElement("button"),
        text: "C"
      }
    };
  }

  render() {
    this.rootElement.appendChild(this.elements.display);
    const buttonContainer = document.createElement("div");
    this.elements.buttons.forEach((button) => {
      const buttonElement = document.createElement("button");
      buttonElement.textContent = button.text;
      buttonElement.classList.add(button.class);
      buttonContainer.appendChild(buttonElement);
    });
    this.rootElement.appendChild(buttonContainer);
    this.rootElement.appendChild(this.elements.equalsButton.element);
    this.rootElement.appendChild(this.elements.clearButton.element);
    this.updateDisplay("");
  }

  updateDisplay(text) {
    this.elements.display.textContent = text;
  }

  handleButtonClick(button) {
    switch (button) {
      case "C":
        this.updateDisplay("");
        break;
      case "=":
        try {
          const result = eval(this.elements.display.textContent);
          this.updateDisplay(result.toString());
        } catch (error) {
          this.updateDisplay("Error");
        }
        break;
      default:
        this.updateDisplay(this.elements.display.textContent + button);
        break;
    }
  }
}

const rootElement = document.getElementById("calculator");
const calculator = new ScientificCalculator(rootElement);
calculator.render();

rootElement.addEventListener("click", (event) => {
  if (
    event.target.tagName === "BUTTON" &&
    ["digit-button", "operator-button"].includes(event.target.classList[0])
  ) {
    const button = event.target.textContent;
    calculator.handleButtonClick(button);
  }
});
