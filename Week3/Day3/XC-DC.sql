-- Part I
--1
CREATE TABLE customer (
    id serial PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE customerprofile (
    id serial PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INT UNIQUE,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

--2
INSERT INTO customer (first_name, last_name) 
VALUES ('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive')

SELECT * FROM customer

--3
INSERT INTO customerprofile (isLoggedIn, customer_id) 
VALUES (TRUE, (SELECT id FROM customer 
			   WHERE first_name = 'John' AND last_name = 'Doe')),
	(FALSE, (SELECT id FROM customer 
			 WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

--4
SELECT customer.first_name FROM customer
INNER JOIN customerprofile 
ON customer.id = customerprofile.customer_id
WHERE customerprofile.isLoggedIn = TRUE;

SELECT customer.first_name, customerprofile.isLoggedIn FROM customer
LEFT JOIN customerprofile 
ON customer.id = customerprofile.customer_id;


SELECT COUNT(*) FROM customer
LEFT JOIN customerprofile 
ON customer.id = customerprofile.customer_id
WHERE customerprofile.isLoggedIn = FALSE OR customerprofile.isLoggedIn IS NULL;

SELECT * FROM customerprofile




-- Part II

CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);


INSERT INTO book (title, author) 
VALUES ('Alice In Wonderland', 'Lewis Carroll'),
		('Harry Potter', 'J.K Rowling'),
		('To kill a mockingbird', 'Harper Lee')
		
SELECT * FROM book


CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
)

INSERT INTO student (name, age) 
VALUES ('John', 12),
		('Lera', 11),
 		('Patrick', 10),
		('Bob', 14)

INSERT INTO student (name, age) 
VALUES ('Dima', 40)
		
SELECT * FROM student


CREATE TABLE library (
    book_id INT,
    student_id INT,
    borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);


INSERT INTO library  
VALUES 
((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'), 
 (SELECT student_id FROM student WHERE name = 'John'), '2022-02-15');

INSERT INTO library (book_id, student_id, borrowed_date) 
VALUES 
((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'), 
 (SELECT student_id FROM student WHERE name = 'Bob'), '2021-03-03');

INSERT INTO library (book_id, student_id, borrowed_date) 
VALUES 
((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'), 
 (SELECT student_id FROM student WHERE name = 'Lera'), '2021-05-23');

INSERT INTO library (book_id, student_id, borrowed_date) 
VALUES 
((SELECT book_id FROM book WHERE title = 'Harry Potter'), 
 (SELECT student_id FROM student WHERE name = 'Bob'), '2021-08-12');


--7.
SELECT * FROM library


SELECT student.name, book.title
FROM library
JOIN student 
ON library.student_id = student.student_id
JOIN book 
ON library.book_id = book.book_id

-- Select the average age of the children that borrowed 'Alice In Wonderland'
SELECT AVG(student.age) 
FROM library
JOIN student 
ON library.student_id = student.student_id
JOIN book 
ON library.book_id = book.book_id
WHERE book.title = 'Alice In Wonderland'

DELETE FROM student 
WHERE name = 'John'
-- was deleted too

SELECT * FROM library





