--1
-- CREATE TABLE items(
-- 	id serial PRIMARY KEY,
-- 	name varchar(255) NOT NULL,
-- 	price integer NOT NULL
-- );

-- CREATE TABLE customers(
-- 	id serial PRIMARY KEY,
-- 	firstname varchar(255),
-- 	surname varchar(255)
-- )

-- INSERT INTO items (name, price)
-- VALUES ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80)

-- INSERT INTO customers (firstname, surname)
-- VALUES 
-- ('Greg','Jones'),
-- ('Sandra','Jones'),
-- ('Scott','Scott'),
-- ('Trevor','Green'),
-- ('Melanie','Johnson');

-- All the items.
-- SELECT * from items;
-- SELECT * from customers;

-- All the items with a price above 80 (80 not included).
SELECT * FROM items WHERE price > 80;

-- All the items with a price below 300. (300 included)
SELECT * FROM items WHERE price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT * FROM customers WHERE surname in ('Smith');

-- All customers whose last name is ‘Jones’.
SELECT * FROM customers WHERE surname in ('Jones');

-- All customers whose firstname is not ‘Scott’.
SELECT * FROM customers WHERE firstname not in ('Scott');





