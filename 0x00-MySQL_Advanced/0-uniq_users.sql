-- creates a table users with id, email, and name attribute
CREATE DATABASE IF NOT EXISTS holberton;
USE holberton;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
