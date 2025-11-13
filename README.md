# Library Management System (OOP Version)

# Lab Overview
This project demonstrates the use of Object-Oriented Programming (OOP) in Python 
by implementing a simple Library Management System. The system can manage 
books, members, and borrow/return transactions.

# Project Structure
library-management-oop/
│
├── README.md                          # This file
│
├── procedural_version/
│   ├── library_procedural.py         # Original procedural code
│   └── test_procedural.py            # Comprehensive test suite
│
├── oop_solution/
│   ├── library_oop.py                # Student's OOP implementation 
│   └── test_oop.py                   # Tests for OOP version 

# Design Overview
1. Book Class
   Represents a book in the library.
    - borrow(): decreases available copies when borrowed
    - return_book(): increases available copies when returned
    - __str__(): displays book information

2. Member Class
   Represents a library member.
    - can_borrow(): checks if the member can borrow more books (limit 3)
    - borrow_book(book): allows borrowing a book if possible
    - return_book(book): allows returning a borrowed book
    - __str__(): displays member information and borrowed books

3. Library Class
   Manages all books and members in the system.
    - add_book() / add_member(): add new entries
    - find_book() / find_member(): search by ID
    - borrow_book() / return_book(): manage transactions
    - display_available_books(): show available books
    - display_member_books(): show books borrowed by a member
    - display_all_members(): show all registered members

# Features
1. Add and search for books or members
2. Borrow and return books with automatic copy tracking
3. Borrowing limit of 3 books per member
4. Display current status of books and members

# How to Test and Run the Code
1. Ensure you have Python 3.x installed.
2. Open your terminal or command prompt in the project directory.
3. Run the following command:

   python oop_version.py
