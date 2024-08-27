-- Active: 1723675705494@@127.0.0.1@5432@products
SELECT products.name, providers.name
FROM products, providers
WHERE products.id_providers = providers.id
and products.id_categories = 6;
