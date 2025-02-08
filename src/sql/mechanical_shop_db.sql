DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS client;


CREATE TABLE client (
    client_id SERIAL PRIMARY KEY,
    dni VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

CREATE TABLE sales (
    client_id INT NOT NULL,
    product_id INT NOT NULL,
    sold_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (client_id, product_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE
);


INSERT INTO client (dni, name, email) VALUES 
('12345678A', 'Ana Pérez', 'ana.perez@example.com'),
('23456789B', 'Juan Gómez', 'juan.gomez@example.com'),
('34567890C', 'Luis Martínez', 'luis.martinez@example.com');

INSERT INTO product (description, price) VALUES 
('Llave inglesa ajustable', 25.50),
('Juego de destornilladores', 45.99),
('Gato hidráulico para coche', 120.00),
('Juego de llaves Allen', 18.75),
('Compresor de aire portátil', 85.00);

INSERT INTO sales (client_id, product_id, sold_date) VALUES 
(1, 1, '2024-02-01 10:30:00'),
(1, 3, '2024-02-02 15:45:00'),
(2, 2, '2024-02-03 12:00:00'),
(2, 5, '2024-02-04 09:15:00'),
(3, 1, '2024-02-05 14:20:00'),
(3, 4, '2024-02-06 16:30:00');
