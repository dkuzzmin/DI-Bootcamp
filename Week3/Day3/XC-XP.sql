-- Exercise 1: DVD Rental
--#1
SELECT name FROM language

--#2 Get a list of all films joined with their languages – select the following details : 
-- film title, description, and language name.

SELECT film.title, film.description, language.name AS language FROM film
INNER JOIN language
on film.language_id = language.language_id;

--#3 Get all languages, even if there are no films in those languages – select the following 
-- details : film title, description, and language name.

SELECT film.title, film.description, language.name AS language FROM language
LEFT  JOIN film
on film.language_id = language.language_id;

--4
-- Create a new table called new_film with the following columns : id, name. 
-- Add some new films to the table.

CREATE TABLE new_film (
	id serial PRIMARY KEY,
	name VARCHAR (500)
);

INSERT INTO 
    new_film (name)
VALUES 
	('Napoleon'),
	('Joker 2');
	
SELECT * FROM new_film

-- 5 Create a new table called customer_review, which will contain film 
-- reviews that customers will make

CREATE TABLE customer_review (
    review_id serial PRIMARY KEY NOT NULL,
    film_id INT,
    language_id INT,
    title VARCHAR,
    score INT,
    review_text VARCHAR,
    last_update TIMESTAMP,
    FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES language(language_id)
);

INSERT INTO 
    customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES 
	(1,2,'About Napoleon film', 9, 'Review on Napoleon movie. Review on Napoleon movie. Review on Napoleon movie. Review on Napoleon movie. Review on Napoleon movie. Review on Napoleon movie. ', '2023-12-13'),
--	(2,1,'Hoakin Joker', 10, 'Review on Napoleon movie. Review on Napoleon movie. Review on Napoleon movie. ', '2023-12-10');
	
SELECT * FROM customer_review
	
-- 7. Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id = 1;

SELECT * FROM customer_review


-- Exercise 2 : DVD Rental

--1.Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film SET language_id = 3 WHERE film_id = 1;

--2.Which foreign keys (references) are defined for the customer table? 
--How does this affect the way in which we INSERT into the customer table?
customer_address_id_fkey
on update cascade
SELECT * FROM address

--3. We created a new table called customer_review. Drop this table. Is this an easy step, 
-- or does it need extra checking?

DROP TABLE customer_review;

We need to check CONSTRAINTS with other tables

SELECT * FROM customer_review;

--4. Find out how many rentals are still outstanding (ie. have not been returned 
-- to the store yet).

SELECT * FROM rental WHERE return_date IS NULL;

-- 5.Find the 30 most expensive movies which are outstanding (ie. have not been
-- returned to the store yet)

SELECT film.title, film.rental_rate, rental.customer_id, rental.return_date FROM rental 
INNER JOIN inventory
ON rental.inventory_id = inventory.inventory_id
INNER JOIN film
ON film.film_id = inventory.film_id
WHERE rental.return_date IS NULL
ORDER BY film.rental_rate DESC
LIMIT 30


-- 6. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, 
-- but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, 
-- and he returned it between the 28th of July and the 1st of August, 2005.

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” 
-- in the title or description, and it looked like it was a very expensive DVD to replace.

--The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT actor.first_name, actor.last_name, film.title FROM film 
INNER JOIN film_actor
ON film_actor.film_id = film.film_id
INNER JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE (actor.first_name = 'Penelope' AND actor.last_name = 'Monroe') AND 
(film.fulltext @@ to_tsquery('sumo'))


-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT film.title, film.length, category.name, film.rating FROM film
INNER JOIN film_category
ON film.film_id = film_category.film_id
INNER JOIN category
ON film_category.category_id = category.category_id
WHERE category.category_id = 6 AND film.rating = 'R' AND film.length < 60

-- 3. The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, 
-- and he returned it between the 28th of July and the 1st of August, 2005.

SELECT film.title, customer.first_name, customer.last_name, payment.amount, rental.return_date FROM film
INNER JOIN inventory
ON film.film_id = inventory.film_id
INNER JOIN rental
ON rental.inventory_id = inventory.inventory_id
INNER JOIN customer
ON customer.customer_id = rental.customer_id
INNER JOIN payment
ON payment.rental_id = rental.rental_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND payment.amount > 4 
	AND (rental.return_date BETWEEN '2005-07-28' AND '2005-08-01')






--4. The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” 
-- in the title or description, and it looked like it was a very expensive DVD to replace.

SELECT film.title, customer.first_name, customer.last_name, film.replacement_cost, film.description FROM film
INNER JOIN inventory
ON film.film_id = inventory.film_id
INNER JOIN rental
ON rental.inventory_id = inventory.inventory_id
INNER JOIN customer
ON customer.customer_id = rental.customer_id
WHERE (film.description LIKE '%Boat%' OR film.title LIKE '%Boat%') 
	AND customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
ORDER BY film.replacement_cost DESC
LIMIT 1





SELECT * FROM customer;
SELECT * FROM payment;
SELECT * FROM film;
SELECT * FROM film_actor;
SELECT * FROM film_category;
SELECT * FROM category;
SELECT * FROM actor;
SELECT * FROM rental;
SELECT * FROM store;
SELECT * FROM inventory;