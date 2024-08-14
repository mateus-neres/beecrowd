CREATE DATABASE products;
CREATE TABLE products(
    id SERIAL PRIMARY key,
    name VARCHAR(100),
    amount INTEGER,
    price DECIMAL(10, 2)
);

INSERT INTO products (name, amount, price) VALUES 
('Two-door wardrobe', 100, 80),
('Dining table', 1000, 560),
('Towel holder', 10000, 5.50),
('Computer desk', 350, 100),
('Chair', 3000, 210.64),
('Single bed', 750, 99);

SELECT * FROM products;