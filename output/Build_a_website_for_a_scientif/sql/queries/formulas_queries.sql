sql
-- formulas_queries.sql

-- Drop tables if they exist
DROP TABLE IF EXISTS formulas;
DROP TABLE IF EXISTS formula_results;
DROP TABLE IF EXISTS formula_methods;
DROP TABLE IF EXISTS calculations;

-- Create tables
CREATE TABLE calculations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE formula_methods (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    calculation_id INT,
    FOREIGN KEY (calculation_id) REFERENCES calculations(id)
);

CREATE TABLE formulas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    equation VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    method_id INT,
    FOREIGN KEY (method_id) REFERENCES formula_methods(id)
);

CREATE TABLE formula_results (
    id INT PRIMARY KEY AUTO_INCREMENT,
    formula_id INT NOT NULL,
    result_value DECIMAL(10, 5) NOT NULL,
    result_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (formula_id) REFERENCES formulas(id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_formulas_method_id ON formulas (method_id);
CREATE INDEX idx_formula_results_formula_id ON formula_results (formula_id);
CREATE INDEX idx_calculations_name ON calculations (name);
CREATE INDEX idx_formula_methods_calculation_id ON formula_methods (calculation_id);

-- Functions
DELIMITER $$

CREATE FUNCTION save_formula_result(formula_id INT, result_value DECIMAL(10, 5), result_description TEXT) RETURNS INT
BEGIN
    DECLARE new_id INT;
    INSERT INTO formula_results (formula_id, result_value, result_description) VALUES (formula_id, result_value, result_description);
    SET new_id = LAST_INSERT_ID();
    RETURN new_id;
END$$

CREATE FUNCTION get_formula_result(formula_id INT) RETURNS DECIMAL(10, 5)
BEGIN
    DECLARE result_value DECIMAL(10, 5);
    SELECT result_value INTO result_value FROM formula_results WHERE formula_id = formula_id ORDER BY id LIMIT 1;
    RETURN result_value;
END$$

DELIMITER ;

-- Queries
DELIMITER $$

CREATE PROCEDURE create_calculation(name VARCHAR(255), description TEXT)
BEGIN
    INSERT INTO calculations (name, description) VALUES (name, description);
END$$

CREATE PROCEDURE create_method(calculation_id INT, name VARCHAR(255), description TEXT)
BEGIN
    INSERT INTO formula_methods (calculation_id, name, description) VALUES (calculation_id, name, description);
END$$

CREATE PROCEDURE create_formula(method_id INT, name VARCHAR(255), description TEXT, equation VARCHAR(255))
BEGIN
    INSERT INTO formulas (method_id, name, description, equation) VALUES (method_id, name, description, equation);
END$$

CREATE PROCEDURE get_calculations_by_name(name VARCHAR(255)) RETURNS TABLE
BEGIN
    RETURN (
        SELECT * FROM calculations WHERE name LIKE CONCAT("%", name, "%")
    );
END$$

DELIMITER ;


Please note that the above SQL code uses MySQL syntax, but similar queries can be created using other SQL dialects.