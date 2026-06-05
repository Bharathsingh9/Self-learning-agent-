python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scientific_calculator.db'
db = SQLAlchemy(app)


class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equation = db.Column(db.String(128), nullable=False)
    result = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.DateTime.now)

    def __repr__(self):
        return f'<Calculation id={self.id} equation={self.equation} result={self.result}>'


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print('Database created successfully!')
