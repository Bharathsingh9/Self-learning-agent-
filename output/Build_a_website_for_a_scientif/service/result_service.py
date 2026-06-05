python
# result_service.py
from typing import List
from db import db

class Formula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

class CalculationMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formula_id = db.Column(db.Integer, db.ForeignKey('formula.id'), nullable=False)
    formula = db.relationship('Formula', backref=db.backref('calculation_methods', lazy=True))
    method_type = db.Column(db.String(50), nullable=False)
    method_details = db.Column(db.String(200), nullable=False)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calculation_method_id = db.Column(db.Integer, db.ForeignKey('calculation_method.id'), nullable=False)
    calculation_method = db.relationship('CalculationMethod', backref=db.backref('results', lazy=True))
    input_values = db.Column(db.String(100), nullable=False)
    output_value = db.Column(db.String(50), nullable=False)
    output_units = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

class ResultService:
    def __init__(self):
        self.formulas = Formula.query.all()
        self.ccalculationMethods = CalculationMethod.query.all()
        self.results = Result.query.all()

    def get_formulas(self) -> List[Formula]:
        return self.formulas

    def get_calculation_methods(self, formula_id: int) -> List[CalculationMethod]:
        return [cm for cm in self.ccalculationMethods if cm.formula_id == formula_id]

    def get_results(self, calculation_method_id: int) -> List[Result]:
        return [r for r in self.results if r.calculation_method_id == calculation_method_id]

    def get_result(self, id: int) -> Result:
        return Result.query.get(id)

    def create_formula(self, title: str, description: str) -> Formula:
        formula = Formula(title=title, description=description)
        db.session.add(formula)
        db.session.commit()
        return formula

    def delete_formula(self, id: int):
        formula = Formula.query.get(id)
        db.session.delete(formula)
        db.session.commit()

    def update_formula(self, id: int, title: str, description: str) -> Formula:
        formula = Formula.query.get(id)
        formula.title = title
        formula.description = description
        db.session.commit()
        return formula

    def create_calculation_method(self, formula_id: int, method_type: str, method_details: str) -> CalculationMethod:
        calculation_method = CalculationMethod(formula_id=formula_id, method_type=method_type, method_details=method_details)
        db.session.add(calculation_method)
        db.session.commit()
        return calculation_method

    def delete_calculation_method(self, id: int):
        calculation_method = CalculationMethod.query.get(id)
        db.session.delete(calculation_method)
        db.session.commit()

    def update_calculation_method(self, id: int, method_type: str, method_details: str) -> CalculationMethod:
        calculation_method = CalculationMethod.query.get(id)
        calculation_method.method_type = method_type
        calculation_method.method_details = method_details
        db.session.commit()
        return calculation_method

    def create_result(self, calculation_method_id: int, input_values: str, output_value: str, output_units: str) -> Result:
        result = Result(calculation_method_id=calculation_method_id, input_values=input_values, output_value=output_value, output_units=output_units)
        db.session.add(result)
        db.session.commit()
        return result

    def delete_result(self, id: int):
        result = Result.query.get(id)
        db.session.delete(result)
        db.session.commit()


# Example usage:
if __name__ == "__main__":
    from service import result_service

    # Create formulas
    formula_service = result_service.ResultService()
    formula1 = formula_service.create_formula("Example Formula 1", "This is an example formula")
    formula2 = formula_service.create_formula("Example Formula 2", "This is another example formula")

    # Create calculation methods
    calculation_method1 = formula_service.create_calculation_method(formula1.id, "Example Method 1", "This is an example method")
    calculation_method2 = formula_service.create_calculation_method(formula2.id, "Example Method 2", "This is another example method")

    # Create results
    result1 = formula_service.create_result(calculation_method1.id, "Example input values", "Example output value", "Example output units")
    result2 = formula_service.create_result(calculation_method2.id, "Another example input values", "Another example output value", "Another example output units")
