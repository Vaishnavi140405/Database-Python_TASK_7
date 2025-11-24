CREATE DATABASE sales_db;
USE sales_db;

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO sales (product, quantity, price) VALUES
('Hammer', 10, 300),
('Hammer', 5, 300),
('Drill', 7, 1800),
('Drill', 3, 1800),
('Saw', 12, 450),
('Saw', 8, 450);
