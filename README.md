# IIT-Library-Management-System 📚

## Description
This is the **IIT Library Management System**, a Python-based application that connects to an **Oracle database** using **cx_Oracle**. The system allows for easy management of library functionalities such as adding customers, adding books, issuing books, and checking book availability through a user-friendly **Python GUI**.

## Key Features:
- **Add Customers**: Easily add new customers to the library system.
- **Add Books**: Manage the inventory by adding new books to the database.
- **Issue Books**: Issue books to customers and keep track of borrowed items.
- **View Book Availability**: Check which books are available or currently issued.

## Technologies Used:
- **Python**: For creating the GUI and business logic.
- **cx_Oracle**: For connecting Python to the Oracle database.
- **Oracle Database**: Used for storing and managing library data.

## Project Files:
- **AddBook.py**: Script for adding new books to the system.
- **AddCust.py**: Script for adding new customers to the system.
- **IssueBook.py**: Handles the process of issuing books to customers.
- **ViewBook.py**: Allows viewing of the book inventory.
- **ViewIssueBook.py**: Provides a view of all currently issued books.
- **main.py**: Main script to launch the Library Management System.
- **lms.sql**: SQL file to set up the Oracle database for the system.
- **background.png**: Background image used in the GUI.

## How to Use:
1. Clone the repository to your local machine.
2. Set up the Oracle database using the provided `lms.sql` file.
3. Install the necessary dependencies, including `cx_Oracle`.
4. Run `main.py` to start the Library Management System.
