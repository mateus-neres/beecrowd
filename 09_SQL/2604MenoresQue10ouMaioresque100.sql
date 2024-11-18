-- Active: 1723675705494@@127.0.0.1@5432@postgres
SELECT id, name
FROM products
WHERE price < 10 OR price > 100;