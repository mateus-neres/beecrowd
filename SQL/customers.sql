CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    street VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(100),
    state VARCHAR(100),
    credit_limit int NOT NULL
);

INSERT INTO customers (name, street, city, state, credit_limit) VALUES ('Pedro Augusto da Rocha','Rua Pedro Carlos Hoffman','Porto Alegre','RS', 700.00);
INSERT INTO customers (name, street, city, state, credit_limit) VALUES ('Antonio Carlos Mamel','Av. Pinheiros','Belo Horizonte','MG', 3500.00);
INSERT INTO customers (name, street, city, state, credit_limit) VALUES ('Luiza Augusta Mhor','Rua Salto Grande','Niteroi','RJ', 4000.00);
INSERT INTO customers (name, street, city, state, credit_limit) VALUES ('Jane Ester','	Av 7 de setembro','	Erechim','RS', 800.00);
INSERT INTO customers (name, street, city, state, credit_limit) VALUES ('Marcos Antônio dos Santos','Av Farrapos','Porto Alegre','RS', 4250.25);

SELECT * FROM customers