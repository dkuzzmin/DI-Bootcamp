
INSERT INTO
products_desc (description, product_id)
VALUES
	('Amazing iPad', 10),
	('Great iPhone', 11),
	('Best iWatch', 12),
	('Fastest car ever iCar', 13);
	
SELECT * FROM products;

SELECT products.id, products.name, products.price, product_desc.description from products
INNER JOIN products_desc
ON products.id = product_desc.product_id;

SELECT products.id, products.name, products.price, product_desc.description 
FROM products, products_desc
WHERE products.id = product_desc.product_id;
 
SELECT city.cuty, country.country from city
INNER JOIN country
ON city.country_id = country.country_id;

-- SELECT products.id, products.name, products.price, product_desc.description from products
-- INNER JOIN products_desc
-- ON products.id = product_desc.product_id;








SELECT
	customer.first_name,
	customer.last_name,
	customer.email,
	customer.address,
	customer.district,
	city.city,
	country.country
FROM customer
INNER JOIN address
ON customer.address_id = address.address_id
INNER JOIN city
ON address.city_id = city.city_id
INNER JOIN country
ON city.country_id = county.country_id









SELECT products.id, products.name, product.price