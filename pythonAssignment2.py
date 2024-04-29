# Create a simple library management system using object-oriented programming in Python. 

class libBooks:
    def __init__(self, title, author, genre):
        self.title, self.author, self.genre, self.available = title, author, genre, True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre}) - Available: {'Yes' if self.available else 'No'}"

# Create a class and an empty list for the library books

class myLibrary:
    def __init__(self):
        self.books = []

# Append books to the library

    def addBook(self, book):
        self.books.append(book)


# Display library books and current availability

    def displayBooks(self):
        for book in self.books:
            print(book)
        else:
            if not self.books:
                print("Not available in this library")


# Borrow book(s) and display library books and current availability

    def borrowBook(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"You have borrowed {title} successfully")
                else:
                    print(f"{title} is currently not available to be borrowed")
                return
        print(f"The book {title} is not in tnis library")

 # Return book(s) and display all library books and current availability   

    def returnBook(self, title):  
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"You have returned {title} successfully")
                else:
                    print(f"{title} is currently available to be borrowed")
                return
        print(f"The book {title} is not in tnis library")
# Create an empty list to contain the library books to be added/appended

library = myLibrary()

# Add book(s) to the library
library.addBook(libBooks("A Time to Kill", "John Grisham", "legal thriller"))
library.addBook(libBooks("The Firm", "John Grisham", "legal thriller"))
library.addBook(libBooks("The Pelican Brief", "John Grisham", "legal thriller"))

# Test the code with the methods created
# Display books
print("Books we have in this library include:")
library.displayBooks()

# Borrow a book and display all boks after borrowing
print("\nBorrowed book(s):")
library.borrowBook("The Firm")
library.borrowBook("The Pelican Brief")
print("\nBooks and availability after borrowing:")
library.displayBooks()

# Return a book(s) and display all boks after borrowing
print("\nReturned book(s):")
library.returnBook("The Pelican Brief")
print("\nBooks and availability after returns:")
library.displayBooks()



