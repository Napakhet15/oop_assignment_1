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


