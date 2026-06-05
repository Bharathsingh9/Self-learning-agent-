sql
-- results.sql

CREATE TABLE Formula (
    formula_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE Calculation_Method (
    calculation_method_id INT PRIMARY KEY AUTO_INCREMENT,
    formula_id INT NOT NULL,
    method_name VARCHAR(255) NOT NULL,
    method_description TEXT,
    FOREIGN KEY (formula_id) REFERENCES Formula(formula_id)
);

CREATE TABLE Calculation_Parameter (
    calculation_parameter_id INT PRIMARY KEY AUTO_INCREMENT,
    formula_id INT NOT NULL,
    parameter_name VARCHAR(255) NOT NULL,
    parameter_description TEXT,
    FOREIGN KEY (formula_id) REFERENCES Formula(formula_id)
);

CREATE TABLE Result (
    result_id INT PRIMARY KEY AUTO_INCREMENT,
    calculation_parameter_id INT NOT NULL,
    result_value DECIMAL(10, 5) NOT NULL,
    FOREIGN KEY (calculation_parameter_id) REFERENCES Calculation_Parameter(calculation_parameter_id)
);

CREATE TABLE Calculation_History (
    calculation_history_id INT PRIMARY KEY AUTO_INCREMENT,
    formula_id INT NOT NULL,
    calculation_parameter_id INT NOT NULL,
    input_values TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (formula_id) REFERENCES Formula(formula_id),
    FOREIGN KEY (calculation_parameter_id) REFERENCES Calculation_Parameter(calculation_parameter_id)
);

CREATE TABLE Calculation_Report (
    calculation_report_id INT PRIMARY KEY AUTO_INCREMENT,
    calculation_history_id INT NOT NULL,
    result_id INT NOT NULL,
    FOREIGN KEY (calculation_history_id) REFERENCES Calculation_History(calculation_history_id),
    FOREIGN KEY (result_id) REFERENCES Result(result_id)
);


**Schema explanation:**

1. `Formula`: stores formulas (equations) with name and description.
2. `Calculation_Method`: stores methods used to calculate formulas with associated formula and method name.
3. `Calculation_Parameter`: stores parameters required to calculate formulas with associated formula.
4. `Result`: stores results of formula calculations with associated calculation parameter.
5. `Calculation_History`: stores calculation histories for each formula with associated input values and creation timestamp.
6. `Calculation_Report`: provides a report by linking calculation histories with their results.