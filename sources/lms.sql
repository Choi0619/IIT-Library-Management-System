drop table issue;
drop table books;
drop table customer;
drop table staff;
drop table publisher;
drop sequence book_seq;
drop trigger book_bi;

CREATE SEQUENCE book_seq start with 1;

CREATE TRIGGER book_bi
BEFORE INSERT ON Books
FOR EACH ROW
BEGIN
  SELECT book_seq.nextval
  INTO: new.Book_ID
  FROM dual;
END;


CREATE TABLE  Publisher(	
    Publisher_ID VARCHAR(5), 
    Publisher_NAME VARCHAR2(100) NOT NULL, 
    PRIMARY KEY (Publisher_ID)
);


CREATE TABLE Books
(
    Book_ID int primary key,
    Publisher_ID varchar(5),
    Title varchar(100),
    Author varchar(50) not null,
    ISBN varchar(30) not null unique,
    Num_of_Books int check (Num_of_Books >= 0),
    Foreign key (Publisher_ID) references  Publisher(Publisher_ID)
);

CREATE SEQUENCE book_seq;

CREATE TRIGGER book_bi
BEFORE INSERT ON Books
FOR EACH ROW
BEGIN
  SELECT book_seq.nextval
  INTO: new.Book_ID
  FROM dual;
END;

/*
CREATE TABLE Books_Available
(
    Book_ID int,
    Title varchar(100),
    Num_of_Books int,
    Book_available int,
    primary key (Book_ID),
    Foreign key (Title) references Books(Title),
    Foreign key (Num_of_Books) references Books(Num_of_Books)
);
*/

CREATE TABLE Staff
(
    Staff_ID varchar(5),
	Staff_Name varchar(30) not null,
	Salary numeric(8, 2) check (Salary >= 500),
	Phone varchar(11) not null ,
	Street varchar(50),
    primary key (Staff_ID)
);


CREATE TABLE Customer
(
    Cust_id varchar(5),
    Name varchar(50) not null,
    Email_ID varchar(30) check (Email_ID like '%@%.%'),
    City varchar(20),
    Contact varchar(15) unique,
    primary key(Cust_id)
);


CREATE TABLE Issue
(
    Cust_id varchar(5),
    Book_id int,
    Issue_date date,
    Return_date date,
    Staff_id varchar(5),
    foreign key (Book_id) references Books(Book_ID),
    primary key (Cust_id, Book_id, Issue_date)
);



/*ADD INFO INTO PUBLISHER*/
INSERT INTO Publisher VALUES('P001','McGraw Hill');
INSERT INTO Publisher VALUES('P012','Techneo');
INSERT INTO Publisher VALUES('P003','Oxford');
INSERT INTO Publisher VALUES('P145','BR Patil');
INSERT INTO Publisher VALUES('P456','S Chand');
INSERT INTO Publisher VALUES('P087','Cengage');
INSERT INTO Publisher VALUES('P324','Black Swan');


/*ADD INFO INTO BOOKS*/
/*
INSERT INTO Books VALUES(1421,'P003','DICTIONARY', 'ANTHONY ANDRUS','1234-4587-890-01', 20);
INSERT INTO Books VALUES(6091,'P012','DBMS', 'STEPHAN ROGERS', '4465-9198-21-230', 134);
*/
INSERT INTO Books VALUES('P001','B.E.E', 'BALLANIS', '280-2981-7892-15', 56);
INSERT INTO Books VALUES('P456','SOCIAL STUDIES', 'H. TAUB', '4837-385-9482-88', 47);
INSERT INTO Books VALUES('P012','BIG DATA ANALYTICS', 'SARVESH TALE', '1488-112-70498-87', 78);
INSERT INTO Books VALUES('P003','TELL TALES', 'RK NARAYAN', '9873-721-48-44862', 29);
INSERT INTO Books VALUES('P012','HARRY POTTER', 'RK NARAYAN', '9342-913-2222-12', 50);


/*ADD INFO INTO STAFF*/
INSERT INTO Staff VALUES('S01', 'Eliel', 3000.00,'9167180803', 'Colaba');
INSERT INTO Staff VALUES('S02','Neelam', 3040.00,'9161180803', 'Puri');
INSERT INTO Staff VALUES('S03','Brigham', 13000.00,'9110180803', 'Circular Road');
INSERT INTO Staff VALUES('S04','Jacob', 373000.00,'9169870803', 'Connaught Place');
INSERT INTO Staff VALUES('S05','Gyuhwan', 333000.00,'876180803', 'Fort');
INSERT INTO Staff VALUES('S06','Sareena', 333000.00,'9167181233', 'Tilak Road');
INSERT INTO Staff VALUES('S07','Patrick', 800.00,'916718233', 'Tilak Road1');


/*ADD INFO INTO CUSTOMER*/
INSERT INTO Customer VALUES('C01','Muriel','1938212@gmail.com', 'New Delhi', '3122011235');
INSERT INTO Customer VALUES('C02','Sharone','shar0930@gmail.com', 'Mumbai', '3121314634');
INSERT INTO Customer VALUES('C03','Laurence','ljacobsyee22@gmail.com', 'Nagpur', '09038541656');
INSERT INTO Customer VALUES('C04','Courtney','courtneydabest@yahoo.com', 'Nashik', '312154526');
INSERT INTO Customer VALUES('C05','Raj','raj991@yahoo.com', 'Aurangabad',  '6722562365');
INSERT INTO Customer VALUES('C06','Sebastian','Sebsebthegreat@gmail.com', 'Dadar', '2782562365');


/*ADD INFO INTO ISSUE*/
INSERT INTO Issue VALUES('C04', 1111, '22-09-02', '22-09-11', 'S06');
INSERT INTO Issue VALUES('C05', 2, '20-08-02', NULL, 'S03');
INSERT INTO Issue VALUES('C04', 1, '21-12-03', '22-01-01', 'S01');
INSERT INTO Issue VALUES('C05', 2, '20-08-03', NULL, 'S03');
