sql
-- File: calculation_methods.sql

DROP TABLE IF EXISTS results;

CREATE TABLE results (
  id INT AUTO_INCREMENT PRIMARY KEY,
  calculation_method_id INT,
  formula_id INT,
  calculation_date DATE DEFAULT CURRENT_DATE,
  value DECIMAL(10, 5),
  unit VARCHAR(50),
  result_notes TEXT,
  FOREIGN KEY (calculation_method_id) REFERENCES calculation_methods(id),
  FOREIGN KEY (formula_id) REFERENCES formulas(id)
);

DROP TABLE IF EXISTS calculation_methods;

CREATE TABLE calculation_methods (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  calculation_type VARCHAR(50) NOT NULL,
  calculation_order INT,
  formula_id INT,
  FOREIGN KEY (formula_id) REFERENCES formulas(id)
);

DROP TABLE IF EXISTS formulas;

CREATE TABLE formulas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  formula_expression VARCHAR(500) NOT NULL,
  formula_language VARCHAR(50) NOT NULL
);

-- Example of a pre-populated formula
INSERT INTO formulas (name, description, formula_expression, formula_language)
VALUES 
('Pythagorean Theorem', 'Calculates the length of the hypotenuse of a right triangle', 'c = sqrt(a^2 + b^2)', 'Mathematica');

-- Example of a pre-populated calculation method
INSERT INTO calculation_methods (name, description, calculation_type, calculation_order, formula_id)
VALUES 
('Hypotenuse Calculation', 'Calculates the hypotenuse of a right triangle', 'length', 1, 1);

-- Example of a pre-populated result
INSERT INTO results (calculation_method_id, formula_id, value, unit)
VALUES 
(1, 1, 5.0, 'meters');
