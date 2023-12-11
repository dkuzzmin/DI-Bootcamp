

CREATE TABLE students(
	id serial PRIMARY KEY,
	last_name varchar(255),
	first_name varchar(255),
	birth_date timestamp
);


INSERT INTO students (first_name, last_name, birth_date)
VALUES
('Marc', 'Benichou', to_date('02/11/1998','DD/MM/YYYY')),
('Yoan', 'Cohen', to_date('03/12/2010','DD/MM/YYYY')),
('Lea', 'Benichou', to_date('27/07/1987','DD/MM/YYYY')),
('Amelia', 'Dux', to_date('07/04/1996','DD/MM/YYYY')),
('David', 'Grez', to_date('14/06/2003','DD/MM/YYYY')),
('Omer', 'Simpson', to_date('03/10/1980','DD/MM/YYYY'))


INSERT INTO students (first_name, last_name, birth_date)
VALUES
('Dima', 'Kuzmin', to_date('09/07/1983','DD/MM/YYYY'))

SELECT * FROM students

SELECT first_name, last_name FROM students

SELECT first_name, last_name FROM students WHERE id = 2

SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc'

SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc'

SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%'
SELECT first_name, last_name FROM students WHERE (first_name LIKE 'a%') OR (first_name LIKE 'A%')
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a'

SELECT first_name, last_name FROM students WHERE first_name LIKE '%a_'

SELECT first_name, last_name FROM students WHERE id = 1 AND id = 3

SELECT first_name, last_name FROM students WHERE birth_date > '2000-01-01'








