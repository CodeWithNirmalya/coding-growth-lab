CREATE DATABASE LibraryManagement;
USE LIBRARYMANAGEMENT;

CREATE TABLE Books(
BOOK_ID bigint PRIMARY KEY,
BOOK_NAME VARCHAR(100) NOT NULL,
AUTHOR VARCHAR(50) NOT NULL,
CATEGORY VARCHAR(20),
PRICE DECIMAL(10,2),
QUANITY INT NOT NULL
);

-- DESCRIBE THE TABLE 
DESC Books;

INSERT INTO BOOKS VALUES
(15120," THE ERA OF ARITIFICIAL INTELIIGANCE","SAMIUL.JACOB","TECHNOLOGY",785.00,15);

INSERT INTO Books VALUES
(16235,'Clean Code','Robert C. Martin','Technology',650.00,10),
(17481,'The Alchemist','Paulo Coelho','Fiction',399.00,20),
(18392,'Atomic Habits','James Clear','Self Help',550.00,18),
(19476,'Rich Dad Poor Dad','Robert Kiyosaki','Finance',450.00,25),
(20561,'The Psychology of Money','Morgan Housel','Finance',499.00,12),
(21654,'Think Like a Monk','Jay Shetty','Self Help',525.00,16),
(22780,'Harry Potter and the Sorcerer''s Stone','J.K. Rowling','Fantasy',699.00,30),
(23891,'The Hobbit','J.R.R. Tolkien','Fantasy',620.00,14),
(24937,'Wings of Fire','A.P.J. Abdul Kalam','Biography',375.00,22),
(25146,'Steve Jobs','Walter Isaacson','Biography',799.00,8),
(26385,'The Silent Patient','Alex Michaelides','Thriller',499.00,11),
(27493,'Gone Girl','Gillian Flynn','Thriller',575.00,9),
(28517,'Pride and Prejudice','Jane Austen','Classic',350.00,17),
(29648,'To Kill a Mockingbird','Harper Lee','Classic',480.00,13),
(30765,'The Great Gatsby','F. Scott Fitzgerald','Classic',420.00,15),
(31892,'A Brief History of Time','Stephen Hawking','Science',699.00,10),
(32984,'Sapiens','Yuval Noah Harari','History',899.00,12),
(34175,'The Power of Now','Eckhart Tolle','Self Help',525.00,14),
(35286,'Deep Work','Cal Newport','Technology',610.00,19),
(36412,'The Let Them Theory','Mel Robbins','Self Help',699.00,20),
(37583,'Fourth Wing','Rebecca Yarros','Fantasy',899.00,18),
(38694,'Iron Flame','Rebecca Yarros','Fantasy',950.00,15),
(39725,'The Housemaid','Freida McFadden','Thriller',599.00,22),
(40816,'The Women','Kristin Hannah','Historical Fiction',799.00,12),
(41937,'Yellowface','R.F. Kuang','Fiction',749.00,16),
(42058,'Tomorrow, and Tomorrow, and Tomorrow','Gabrielle Zevin','Fiction',699.00,14),
(43169,'Lessons in Chemistry','Bonnie Garmus','Fiction',725.00,19),
(44280,'The Creative Act: A Way of Being','Rick Rubin','Self Help',999.00,10),
(45391,'The Anxious Generation','Jonathan Haidt','Psychology',850.00,13);

-- DISPLAY ALL BOOKS
SELECT * FROM BOOKS;

-- Display Book_Name and Author.
SELECT BOOK_NAME, AUTHOR FROM BOOKS;

-- Display books whose Price is greater than 700.
SELECT * FROM BOOKS
WHERE PRICE >700;

ALTER TABLE BOOKS
RENAME COLUMN  QUANITY TO QUANTITY;

-- Display books whose Quantity is less than 5.
SELECT * FROM BOOKS
WHERE QUANTITY <10;

-- Update Quantity.
UPDATE BOOKS
SET QUANTITY = 7
WHERE BOOK_ID = 27493;

-- CHECK UPDATE HISTORY
SELECT * FROM BOOKS
WHERE BOOK_ID =41937;

UPDATE BOOKS
SET PRICE = 1540.45
WHERE BOOK_ID = 41937;

-- DELETE ONE BOOK
DELETE FROM BOOKS
WHERE BOOK_ID = 32984;

-- COUNT TOTAL BOOKS
SELECT COUNT(BOOK_ID) FROM BOOKS;

-- FIND MAXIMUM PRICE
SELECT * FROM BOOKS
ORDER BY PRICE DESC
LIMIT 1;

-- FIND MINIMUM PRICE
SELECT * FROM BOOKS
ORDER BY PRICE 
LIMIT 1;

-- Find Average Price.
SELECT AVG(PRICE) AS AVERAGE_BOOK_PRICE
FROM BOOKS;

-- Display books ordered by Price (Descending).
SELECT * FROM BOOKS
ORDER BY PRICE DESC;

-- Add Publisher column.
ALTER TABLE BOOKS
ADD COLUMN PUBLISHER VARCHAR(50) DEFAULT "NOT GIVEN";

SELECT * FROM BOOKS;
UPDATE  BOOKS
SET PUBLISHER = "ITALIAN BEROCKS PUBLISHERS LTD"
WHERE BOOK_ID = 40816;

-- Rename Quantity to Stock.
ALTER TABLE BOOKS
RENAME COLUMN QUANTITY TO STOCK;


-- CREATING A BACKUP 
CREATE TABLE Books_Backup AS
SELECT * FROM Books;
-- VERIFY THE DATA
SHOW TABLES;
SELECT * FROM BOOKS_BACKUP;

-- DROP THE PUBLISHER COLUMN
ALTER TABLE BOOKS
DROP COLUMN  PUBLISHER ;

 -- TRUNCATE THE TABLE
 TRUNCATE TABLE BOOKS;
SHOW TABLES;
SELECT * FROM BOOKS;

-- DROP THE TABLE BOOKS
DROP TABLE BOOKS;