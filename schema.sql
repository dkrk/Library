PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users_user (
	id INTEGER NOT NULL, 
	name VARCHAR(50), 
	email VARCHAR(120), 
	password VARCHAR(120), 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
INSERT INTO "users_user" VALUES(1,'admin','admin@library.com','pbkdf2:sha1:1000$D4vGicwQ$df01c6d225576b5887354bd8e7ca0c6776a389b5');
CREATE TABLE books_book (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO "books_book" VALUES(1,'Теория и расчет гироскопических приборов');
INSERT INTO "books_book" VALUES(2,'Курс дифференциального и интегрального исчисления. т.1. ');
INSERT INTO "books_book" VALUES(3,'Курс дифференциального и интегрального исчисления. т.2.');
INSERT INTO "books_book" VALUES(4,'Курс дифференциального и интегрального исчисления. т.3.');
INSERT INTO "books_book" VALUES(5,'Справочник по математике для научных работников и инженеров.');
INSERT INTO "books_book" VALUES(6,'Справочник по обыкновенным дифференциальным уравнениям.');
INSERT INTO "books_book" VALUES(7,'Курс общей физики. т.1. Механика, колебания и волны, молекулярная физика. ');
INSERT INTO "books_book" VALUES(8,'Курс общей физики. т.2. Электричество.');
INSERT INTO "books_book" VALUES(9,'Курс общей физики. т.3. Оптика, атомная физика.');
INSERT INTO "books_book" VALUES(10,'Теоретическая физика. т.1. Механика.');
INSERT INTO "books_book" VALUES(11,'Теоретическая физика. т.7. Теория упругости.');
INSERT INTO "books_book" VALUES(12,'Моделювання на ЕОМ');
INSERT INTO "books_book" VALUES(13,'Моделирование процессов и систем в MATLAB');
INSERT INTO "books_book" VALUES(14,'Моделирование процессов и технических систем в MATLAB');
INSERT INTO "books_book" VALUES(15,'Завдання до лабораторних робіт з дисципліни "Моделювання на ЕОМ"');
CREATE TABLE books_author (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO "books_author" VALUES(6,'Камке Э.');
INSERT INTO "books_author" VALUES(3,'Корн Г.');
INSERT INTO "books_author" VALUES(4,'Корн Т.');
INSERT INTO "books_author" VALUES(10,'Лазарев Ю.Ф.');
INSERT INTO "books_author" VALUES(8,'Ландау Л.Д.');
INSERT INTO "books_author" VALUES(9,'Лифшиц Е.М.');
INSERT INTO "books_author" VALUES(1,'Одинцов А.А.');
INSERT INTO "books_author" VALUES(7,'Савельев И.В');
INSERT INTO "books_author" VALUES(2,'Фихтенгольц Г.М.');
CREATE TABLE books_book_author (
	book_id INTEGER, 
	author_id INTEGER, 
	FOREIGN KEY(book_id) REFERENCES books_book (id), 
	FOREIGN KEY(author_id) REFERENCES books_author (id)
);
INSERT INTO "books_book_author" VALUES(1,1);
INSERT INTO "books_book_author" VALUES(2,2);
INSERT INTO "books_book_author" VALUES(3,2);
INSERT INTO "books_book_author" VALUES(4,2);
INSERT INTO "books_book_author" VALUES(5,3);
INSERT INTO "books_book_author" VALUES(5,4);
INSERT INTO "books_book_author" VALUES(6,6);
INSERT INTO "books_book_author" VALUES(7,7);
INSERT INTO "books_book_author" VALUES(8,7);
INSERT INTO "books_book_author" VALUES(9,7);
INSERT INTO "books_book_author" VALUES(10,8);
INSERT INTO "books_book_author" VALUES(10,9);
INSERT INTO "books_book_author" VALUES(11,8);
INSERT INTO "books_book_author" VALUES(11,9);
INSERT INTO "books_book_author" VALUES(12,10);
INSERT INTO "books_book_author" VALUES(13,10);
INSERT INTO "books_book_author" VALUES(14,10);
INSERT INTO "books_book_author" VALUES(15,10);
COMMIT;
