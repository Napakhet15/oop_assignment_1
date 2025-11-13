# oop_version.py

class Book:
    def __init__(self, id, title, author, total_copy):
        self.id = id
        self.title = title
        self.author = author
        self.total_copy = total_copy
        self.available_copies = total_copy

    def borrow(self):
        """number of available copies when borrowed"""
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        """number of available copies when returned"""
        if self.available_copies < self.total_copy:
            self.available_copies += 1
            return True
        return False

    def __str__(self):
        return f"[{self.id}] {self.title} by {self.author} ({self.available_copies}/{self.total_copy} available)"


class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books_list = []

    def can_borrow(self):
        """Check member borrow books"""
        return len(self.borrowed_books_list) < 3

    def borrow_book(self, book):
        """Borrow a book if allowed"""
        if book.id in self.borrowed_books_list:
            print("Error: Member already borrowed this book!")
            return False

        if not self.can_borrow():
            print("Error: Member has reached the borrowing limit!")
            return False

        if not book.borrow():
            print("Error: No copies available!")
            return False

        self.borrowed_books_list.append(book.id)
        print(f"{self.name} borrowed '{book.title}'")
        return True

    def return_book(self, book):
        """Return borrow book"""
        if book.id not in self.borrowed_books_list:
            print("Error: This member hasn't borrowed this book!")
            return False

        book.return_book()
        self.borrowed_books_list.remove(book.id)
        print(f"{self.name} returned '{book.title}'")
        return True

    def __str__(self):
        """Display member borrow book """
        if not self.borrowed_books_list:
            borrowed = "No books borrowed"
        else:
            borrowed = ""
            for book_id in self.borrowed_books_list:
                borrowed += f"{book_id}, "
            borrowed = borrowed.rstrip(", ")
        return f"Member: {self.name} ({self.email}) | Borrowed: {borrowed}"


class Library:
    def __init__(self):
        self.books = {}    
        self.members = {}  
        self.borrowed_books = []  

    def add_book(self, book_id, title, author, total_copies):
        if book_id in self.books:
            print("Error: Book ID already exists!")
            return
        self.books[book_id] = Book(book_id, title, author, total_copies)
        print(f"Book '{title}' added successfully!")

    def find_book(self, book_id):
        return self.books.get(book_id, None)
  
    def add_member(self, member_id, name, email):
        if member_id in self.members:
            print("Error: Member ID already exists!")
            return
        self.members[member_id] = Member(member_id, name, email)
        print(f"Member '{name}' registered successfully!")

    def find_member(self, member_id):
        return self.members.get(member_id, None)

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return False

        if not book:
            print("Error: Book not found!")
            return False

        success = member.borrow_book(book)
        if success:
            transaction = {
                "member_id": member.id,
                "book_id": book.id,
                "member_name": member.name,
                "book_title": book.title
            }
            self.borrowed_books.append(transaction)
        return success

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False

        success = member.return_book(book)
        if success:
            # Remove 
            for i, t in enumerate(self.borrowed_books):
                if t["member_id"] == member_id and t["book_id"] == book_id:
                    self.borrowed_books.pop(i)
                    break
        return success

    def display_available_books(self):
        print("\n=== Available Books ===")
        available = [b for b in self.books.values() if b.available_copies > 0]
        if not available:
            print("No books available at the moment.")
            return
        for book in available:
            print(book)

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books_list:
            print("No books currently borrowed.")
        else:
            for bid in member.borrowed_books_list:
                book = self.find_book(bid)
                if book:
                    print(f"- {book.title} by {book.author}")

    def display_all_members(self):
        print("\n=== Members ===")
        for member in self.members.values():
            print(member)

#OOP Test Code

def test_library_system():
    """Comprehensive test of all library functions"""
    
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)
    
    library = Library()
    
    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    library.add_book(4, "Design Patterns", "Gang of Four", 2)
    
    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    library.add_member(101, "Alice Smith", "alice@email.com")
    library.add_member(102, "Bob Jones", "bob@email.com")
    library.add_member(103, "Carol White", "carol@email.com")
    
    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    library.display_available_books()
    
    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(101, 1)  # Alice borrows Python Crash Course
    library.borrow_book(101, 2)  # Alice borrows Clean Code
    library.borrow_book(102, 1)  # Bob borrows Python Crash Course
    
    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    library.display_member_books(101)  # Alice's books
    library.display_member_books(102)  # Bob's books
    library.display_member_books(103)  # Carol's books (none)
    
    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_available_books()
    
    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    library.borrow_book(103, 3)  # Carol borrows the only copy of Pragmatic Programmer
    library.display_available_books()
    
    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(102, 3)  # Bob tries to borrow unavailable book
    
    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    library.borrow_book(101, 4)  # Alice's 3rd book
    library.display_member_books(101)
    library.borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)
    
    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    library.return_book(101, 1)  # Alice returns Python Crash Course
    library.return_book(102, 1)  # Bob returns Python Crash Course
    library.display_member_books(101)
    library.display_available_books()
    
    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(102, 2)  # Bob tries to return book he didn't borrow
    
    # Test 12: Return and Borrow Again
    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(103, 3)  # Carol returns Pragmatic Programmer
    library.borrow_book(102, 3)  # Bob borrows it
    library.display_member_books(102)
    
    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 1)  # Non-existent member
    library.borrow_book(101, 999)  # Non-existent book
    library.return_book(999, 1)  # Non-existent member
    library.display_member_books(999)  # Non-existent member
    
    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for transaction in library.borrowed_books:
        print(f"  {transaction['member_name']} has '{transaction['book_title']}'")
    
    print("\nAll Members and Their Books:")
    for member in library.members.values():
        print(f"\n{member.name} ({member.id}):")
        if member.borrowed_books_list:
            for book_id in member.borrowed_books_list:
                book = library.find_book(book_id)
                print(f"  - {book.title}")
        else:
            print("  (No books borrowed)")
    
    library.display_available_books()
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


# Run test
if __name__ == "__main__":
    test_library_system()
