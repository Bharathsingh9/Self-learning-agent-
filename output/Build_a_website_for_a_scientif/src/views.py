python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "description": "Scientific Calculator Website",
        "routes": [
            "/calculator",
            "/help"
        ]
    }

@app.get("/calculator")
def calculator_page():
    html_content = """
    <html>
    <body>
        <h1>Scientific Calculator</h1>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <div style="background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;">
                <input type="text" id="display" style="width: 100%; height: 40px; font-size: 24px;" disabled>
            </div>
            <div style="background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;">
                <button id="clear" style="width: 20%; height: 40px; font-size: 18px;">Clear</button>
                <button id="backspace" style="width: 20%; height: 40px; font-size: 18px;">Backspace</button>
                <button id="delete" style="width: 20%; height: 40px; font-size: 18px;">Delete</button>
            </div>
            <div style="background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;">
                <button id="7" style="width: 20%; height: 40px; font-size: 18px;">7</button>
                <button id="8" style="width: 20%; height: 40px; font-size: 18px;">8</button>
                <button id="9" style="width: 20%; height: 40px; font-size: 18px;">9</button>
                <button id="divide" style="width: 20%; height: 40px; font-size: 18px;">/</button>
            </div>
            <div style="background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;">
                <button id="4" style="width: 20%; height: 40px; font-size: 18px;">4</button>
                <button id="5" style="width: 20%; height: 40px; font-size: 18px;">5</button>
                <button id="6" style="width: 20%; height: 40px; font-size: 18px;">6</button>
                <button id="multiply" style="width: 20%; height: 40px; font-size: 18px;">*</button>
            </div>
            <div style="background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;">
                <button id="1" style="width: 20%; height: 40px; font-size: 18px;">1</button>
                <button id="2" style="width: 20%; height: 40px; font-size: 18px;">2</button>
                <button id="3" style="width: 20%; height: 40px; font-size: 18px;">3</button>
                <button id="subtract" style="width: 20%; height: 40px; font-size: 18px;">-</button>
            </div>
            <div style="background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;">
                <button id="0" style="width: 20%; height: 40px; font-size: 18px;">0</button>
                <button id="point" style="width: 20%; height: 40px; font-size: 18px;">.</button>
                <button id="equal" style="width: 20%; height: 40px; font-size: 18px;">=</button>
                <button id="add" style="width: 20%; height: 40px; font-size: 18px;">+</button>
            </div>
            <div style="background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;">
                <button id="square" style="width: 100%; height: 40px; font-size: 18px;">Square</button>
                <button id="sqrt" style="width: 100%; height: 40px; font-size: 18px;">Sqrt</button>
                <button id="power" style="width: 100%; height: 40px; font-size: 18px;">Power</button>
                <button id="sin" style="width: 100%; height: 40px; font-size: 18px;">Sin</button>
            </div>
        </div>
        <script>
        document.getElementById("clear").addEventListener("click", function() {
            document.getElementById("display").value = "";
        });
        document.getElementById("backspace").addEventListener("click", function() {
            var value = document.getElementById("display").value;
            document.getElementById("display").value = value.substring(0, value.length - 1);
        });
        document.getElementById("delete").addEventListener("click", function() {
            document.getElementById("display").value = "";
        });
        var buttons = document.querySelectorAll("button");
        buttons.forEach(function(button) {
            button.addEventListener("click", function() {
                if (button.id == "equal") {
                    var value = eval(document.getElementById("display").value);
                    document.getElementById("display").value = value;
                } else {
                    document.getElementById("display").value += button.innerText;
                }
            });
        });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
