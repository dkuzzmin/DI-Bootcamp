CREATE TABLE countries (
    country_id serial PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    capital VARCHAR(255) NOT NULL,
	url VARCHAR(255),
	subregion VARCHAR(255),
	popul INT
);

SELECT * FROM countries



