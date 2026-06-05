from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculator(operation, num1, num2=0):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2 if num2 != 0 else 'Error: Division by zero'
    elif operation == 'sin':
        return math.sin(math.radians(num1))
    elif operation == 'cos':
        return math.cos(math.radians(num1))
    elif operation == 'tan':
        return math.tan(math.radians(num1))
    return "Invalid Operation"

@app.route('/')
def home():
    # Attempt to render index.html if home.html doesn't exist
    try:
        return render_template('index.html')
    except:
        return "Calculator Home (index.html missing)"

@app.route('/calculator', methods=['GET', 'POST'])
def calculator_page():
    result = None
    if request.method == 'POST':
        try:
            operation = request.form.get('operation')
            num1 = float(request.form.get('num1', 0))
            num2 = float(request.form.get('num2', 0))
            result = calculator(operation, num1, num2)
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=8002)
