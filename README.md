Limkokwing Library API
Description

This project is a simple digital library API simulation developed using Python. The system demonstrates how APIs can be used in a library environment to allow users to search for books, borrow books, return books, and manage library operations efficiently.

The project also demonstrates asynchronous programming using async and await, allowing multiple users to interact with the system at the same time.

This assignment was developed for the Limkokwing University Faculty of Information and Communication Technology.

Features
View all books in the library
Search books by title
Borrow books
Return borrowed books
Simulate multiple users accessing the system simultaneously
Uses asynchronous programming (asyncio)
Includes type annotations for cleaner code
Technologies Used
Python 3
Asyncio
Type Annotations
GitHub
API Endpoints Simulated
Endpoint	Method	Description
/books	GET	Retrieve all books
/books/search	GET	Search books by title
/borrow	POST	Borrow a book
/return	POST	Return a borrowed book
/fines	GET	Check overdue fines
Project Structure
limkokwing-library-api/
│
├── library_api.py
├── README.md
├── .gitignore
└── screenshots/
How to Run the Project
Step 1 – Install Python


Example Output
--- ALL BOOKS ---
{'id': 1, 'title': 'Python Basics', 'author': 'John Doe', 'category': 'Programming', 'available': True}

--- SEARCH RESULTS ---
{'id': 1, 'title': 'Python Basics', 'author': 'John Doe', 'category': 'Programming', 'available': True}

--- BORROWING BOOKS ---
Samuel borrowed Python Basics
Mary borrowed Database Systems

--- RETURNING BOOK ---
Samuel returned the book successfully
Async Programming

This project uses asynchronous programming concepts:

async def borrow_book(user: str, book_id: int) -> str:

and

await asyncio.gather(
    borrow_book("Samuel", 1),
    borrow_book("Mary", 2)
)

This allows multiple users to borrow books simultaneously without blocking the system.

Type Annotations

The project includes type annotations for better readability and error checking.

Example:

async def search_book(title: str) -> List[Dict]:
Future Improvements

Possible future upgrades include:

User authentication
Real database integration
Web interface
Book reservation system
Notification system
Fine payment integration
GitHub Requirements Included

This repository contains:

Source code
README.md
.gitignore
Project documentation

Artur: Sydney Renner-Thomas
Faculty of Information and Communication Technology
Limkokwing University of Creative Technology

License

This project is for educational purposes only.
