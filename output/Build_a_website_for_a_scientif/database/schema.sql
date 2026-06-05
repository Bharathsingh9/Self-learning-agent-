sql
-- Create database for calculator application
CREATE DATABASE calculator;

-- Use calculator database
USE calculator;

-- Create table for user login information
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create table for user-created equations and formulas
CREATE TABLE formulas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  equation TEXT NOT NULL,
  description TEXT,
  created_by INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (created_by) REFERENCES users(id)
);

-- Create table for calculation history
CREATE TABLE calculations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  formula_id INT,
  input_value DECIMAL(10, 2) NOT NULL,
  result DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (formula_id) REFERENCES formulas(id)
);

-- Create table for tags for user-created formulas
CREATE TABLE tags (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE
);

-- Create table for many-to-many relationship between formulas and tags
CREATE TABLE formula_tags (
  formula_id INT NOT NULL,
  tag_id INT NOT NULL,
  PRIMARY KEY (formula_id, tag_id),
  FOREIGN KEY (formula_id) REFERENCES formulas(id),
  FOREIGN KEY (tag_id) REFERENCES tags(id)
);

-- Create table for saved calculations
CREATE TABLE saved_calculations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  formula_id INT,
  input_value DECIMAL(10, 2) NOT NULL,
  result DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (formula_id) REFERENCES formulas(id)
);
