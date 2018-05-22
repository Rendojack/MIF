CREATE TABLE AUTHOR
(
	ID INT(11) AUTO_INCREMENT PRIMARY KEY,
	FIRST_NAME VARCHAR(255) NOT NULL,
	LAST_NAME VARCHAR(255) NOT NULL
);

CREATE TABLE BOOK
(
	ID INT(11) AUTO_INCREMENT PRIMARY KEY,
	TITLE VARCHAR(255) NOT NULL,
	DESCRIPTION VARCHAR(255) NOT NULL,
	STUDENT_ID INT(11) NULL,

	CONSTRAINT BOOK_STUDENT_ID_fk FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT (ID)
);

CREATE TABLE AUTHOR_BOOK
(
	AUTHOR_ID INT(11) NOT NULL,
	BOOK_ID INT(11) NOT NULL,

	CONSTRAINT AUTHOR_BOOK_AUTHOR_ID_fk FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHOR (ID),
	CONSTRAINT AUTHOR_BOOK_BOOK_ID_fk FOREIGN KEY (BOOK_ID) REFERENCES BOOK (ID)
);

CREATE TABLE STUDENT
(
	ID INT(11) AUTO_INCREMENT PRIMARY KEY,
	FIRST_NAME VARCHAR(255) NOT NULL,
	LAST_NAME VARCHAR(255) NOT NULL
);


