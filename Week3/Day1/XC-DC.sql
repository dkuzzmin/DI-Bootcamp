CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','1970-10-08', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
('George','Clooney','1961-05-06', 2),
('Angelina','Jolie','1975-06-04', 1),
('Jennifer','Aniston','1969-11-02', 0)
;

SELECT * FROM actors

SELECT COUNT(actor_id)
FROM actors

INSERT INTO actors (first_name, last_name)
VALUES('Hoakin','Fenix');



