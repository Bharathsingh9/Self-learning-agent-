python
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, Optional

class CalculatorForm(FlaskForm):
    num1 = DecimalField('Number 1', validators=[DataRequired()])
    num2 = DecimalField('Number 2', validators=[DataRequired()])
    operator = SelectField('Operator', choices=[
        ('add', '+'),
        ('subtract', '-'),
        ('multiply', '*'),
        ('divide', '/')
    ], coerce=str, validators=[DataRequired()])
    result = DecimalField('Result', render_kw={'readonly': True})
    submit = SubmitField('Calculate')

class HistoryForm(FlaskForm):
    page = IntegerField('Page', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Get History')

class SearchForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()])
    submit = SubmitField('Search')

class NewForm(FlaskForm):
    num1 = DecimalField('Number 1', validators=[DataRequired()])
    num2 = DecimalField('Number 2', validators=[DataRequired()])
    operator = SelectField('Operator', choices=[
        ('add', '+'),
        ('subtract', '-'),
        ('multiply', '*'),
        ('divide', '/')
    ], coerce=str, validators=[DataRequired()])
    submit = SubmitField('New Calculation')
