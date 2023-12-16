-- Exercise 1 : Restaurant Menu Manager

CREATE TABLE Menu_Items (
    item_id serial PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL,
    item_price SMALLINT DEFAULT 0
);

SELECT * FROM Menu_Items