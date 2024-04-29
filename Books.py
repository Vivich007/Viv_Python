class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre}) - Available: {'Yes' if self.available else 'No'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"Book '{title}' has been borrowed successfully.")
                else:
                    print(f"Book '{title}' is not available for borrowing.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"Book '{title}' has been returned successfully.")
                else:
                    print(f"Book '{title}' is already available in the library.")
                return
        print(f"Book '{title}' not found in the library.")



if __name__ == "__main__":
    # Create a library
    library = Library()

    # Add some books
    library.add_book(Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "Fiction"))
    library.add_book(Book("1984", "George Orwell", "Dystopian"))

       # Display all books
    print("All books in the library:")
    library.display_books()

      # Borrow a book
    print("\nBorrowing a book:")
    library.borrow_book("Harry Potter and the Philosopher's Stone")
    library.borrow_book("1984")

    # Display all books after borrowing
    print("\nAll books in the library after borrowing:")
    library.display_books()


     # Return a book
    print("\nReturning a book:")
    library.return_book("1984")

    # Display all books after returning
    print("\nAll books in the library after returning:")
    library.display_books()