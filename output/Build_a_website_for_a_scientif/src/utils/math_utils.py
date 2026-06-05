python
import sqlite3
from datetime import datetime

class MathUtils:
    def __init__(self):
        self.conn = sqlite3.connect('history.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expression text,
                result text,
                timestamp TEXT
            )
        """)
        self.conn.commit()

    def execute_calculation(self, expression):
        try:
            return eval(expression)
        except Exception as e:
            return f"Error: {str(e)}"

    def store_history(self, expression, result):
        self.cursor.execute("""
            INSERT INTO history (expression, result, timestamp)
            VALUES (?, ?, ?)
        """, (expression, str(result), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.conn.commit()

    def get_history(self):
        self.cursor.execute("SELECT * FROM history ORDER BY id DESC")
        return self.cursor.fetchall()

    def get_last_calculation(self):
        self.cursor.execute("SELECT * FROM history ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()

    def delete_history(self, id):
        self.cursor.execute("DELETE FROM history WHERE id = ?", (id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


And here's a simplified example of how you could interact with this class in a Flask server:


from flask import Flask, request, jsonify
from sqlite3 import Error

app = Flask(__name__)
math_utils = MathUtils()

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data['expression']
    result = math_utils.execute_calculation(expression)
    math_utils.store_history(expression, result)
    return jsonify({'result': result})

@app.route('/history', methods=['GET'])
def history():
    history = math_utils.get_history()
    return jsonify({'history': history})

@app.route('/last_calculation', methods=['GET'])
def last_calculation():
    calc = math_utils.get_last_calculation()
    return jsonify({'calc': calc})

@app.route('/delete_calculation', methods=['POST'])
def delete_calculation():
    data = request.json
    id = data['id']
    math_utils.delete_history(id)
    return jsonify({'message': 'Calculation deleted'})

if __name__ == '__main__':
    app.run(debug=True)

Remember to handle errors properly in a real-world application, this is a simplified example for illustration purposes.