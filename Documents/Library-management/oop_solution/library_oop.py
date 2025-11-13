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

