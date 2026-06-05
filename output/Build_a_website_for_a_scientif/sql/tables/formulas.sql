sql
-- formulas.sql

-- Create database
CREATE DATABASE ScientificCalculator;

-- Use database
USE ScientificCalculator;

-- Create table to store unit categories
CREATE TABLE unit_categories (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL
);

-- Create table to store units
CREATE TABLE units (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  unit_category_id INT,
  CONSTRAINT fk_units_unit_categories FOREIGN KEY (unit_category_id) REFERENCES unit_categories (id)
);

-- Create table to store formula types
CREATE TABLE formula_types (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL
);

-- Create table to store formulas
CREATE TABLE formulas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  formula_type_id INT,
  description TEXT,
  CONSTRAINT fk_formulas_formula_types FOREIGN KEY (formula_type_id) REFERENCES formula_types (id)
);

-- Create table to store parameter types
CREATE TABLE parameter_types (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL
);

-- Create table to store parameters
CREATE TABLE parameters (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  parameter_type_id INT,
  formula_id INT,
  description TEXT,
  constraint fk_parameters_formula FOREIGN KEY (formula_id) REFERENCES formulas (id),
  constraint fk_parameters_parameter_types FOREIGN KEY (parameter_type_id) REFERENCES parameter_types (id)
);

-- Create table to store calculation methods
CREATE TABLE calculation_methods (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT
);

-- Create table to store formula calculations
CREATE TABLE formula_calculations (
  id INT PRIMARY KEY AUTO_INCREMENT,
  formula_id INT,
  calculation_method_id INT,
  parameters TEXT,
  result TEXT,
  constraint fk_formula_calculations_formula FOREIGN KEY (formula_id) REFERENCES formulas (id),
  constraint fk_formula_calculations_calculation_methods FOREIGN KEY (calculation_method_id) REFERENCES calculation_methods (id)
);

-- Create table to store results
CREATE TABLE results (
  id INT PRIMARY KEY AUTO_INCREMENT,
  calculation_id INT,
  result TEXT,
  units_id INT,
  CONSTRAINT fk_results_formula_calculations FOREIGN KEY (calculation_id) REFERENCES formula_calculations (id),
  constraint fk_results_units FOREIGN KEY (units_id) REFERENCES units (id)
);

-- Insert initial data
INSERT INTO unit_categories (name) VALUES ('Length'), ('Mass'), ('Time');

INSERT INTO units (name, unit_category_id) VALUES ('Meter', 1), ('Kilogram', 2), ('Second', 3), ('Kilometer', 1), ('Ton', 2);

INSERT INTO formula_types (name) VALUES ('Simple Formula'), ('Complex Formula');

INSERT INTO formulas (name, formula_type_id, description) VALUES ('Area', 1, 'Calculates area of a rectangle'), ('Energy', 2, 'Calculates energy of an object');

INSERT INTO parameter_types (name) VALUES ('Length'), ('Mass'), ('Time');

INSERT INTO parameters (name, parameter_type_id, formula_id, description) VALUES ('Width', 1, 1, 'The width of the rectangle'), ('Height', 1, 1, 'The height of the rectangle'), ('Mass', 2, 2, 'The mass of the object'), ('Velocity', 3, 2, 'The velocity of the object');

INSERT INTO calculation_methods (name) VALUES ('Simple Calculation'), ('Complex Calculation');

INSERT INTO formula_calculations (formula_id, calculation_method_id, parameters, result) VALUES (1, 1, '10, 5', '50'), (2, 2, 'mass, 10, velocity', 'energy');

INSERT INTO results (calculation_id, result, units_id) VALUES (1, '50', 1), (2, '1000', 2);
