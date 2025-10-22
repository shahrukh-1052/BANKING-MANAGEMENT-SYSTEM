-- Create and use database
CREATE DATABASE IF NOT EXISTS bank;
USE bank;

-- Main table
CREATE TABLE IF NOT EXISTS customers (
    username VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(20) NOT NULL,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    city VARCHAR(50) NOT NULL,
    balance INT DEFAULT 0,
    account_number BIGINT NOT NULL UNIQUE,
    status BOOLEAN NOT NULL DEFAULT 1
);
-- Transaction history table
CREATE TABLE IF NOT EXISTS transaction_history (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    transaction_type VARCHAR(50) NOT NULL,
    amount INT NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES customers(username)
); 


--username : sameer45 , pass : 1234 , acno : 60696277
--username : shahrukh45 , pass : 4321 , acno : 40606741