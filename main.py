from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def show_available_books(books): 
    for book in books: #checks through each list
        if book["available"]:#check if books are available
            print(f"{book['id']}: {book['title']} by {book['author']}")


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books(books, term):
    term = term.lower()
    for book in books:
        if term in book["author"].lower() or term in book["genre"].lower():
            print(f"{book['id']}: {book['title']} by {book['author']} ({book['genre']})")

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                due = datetime.today() + timedelta(weeks=2)
                book["due_date"] = due.strftime("%Y-%m-%d")
                book["checkouts"] += 1
                print(f"You checked out {book['title']}. Due back on {book['due_date']}.")
            else:
                print(f"Sorry, {book['title']} is already checked out (due {book['due_date']}).")
                return
            print("Book ID not found.")


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                book["due_date"] = None
                print(f"{book['title']} has been returned and is now available.")
            else:
                print(f"{book['title']} was not checked out.")
            return
    print("Book ID not found.")

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def show_available_books(books):
    today = datetime.today().date()
    overdue = []
    for book in books:
        if not book["available"] and book["due_date"]:
            due_date = datetime.strptime(book["due_date"], "%Y-%m-%d").date()
            if due_date < today:
                overdue.append(book)
    if not overdue:
        print("No overdue books.")
    else:
        print("Overdue books:")
        for book in overdue:
            print(f"{book['id']}: {book['title']} by {book['author']} (due {book['due_date']})")

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    def checkout(self):
        if self.available:
            self.available = False
            due = datetime.today() + timedelta(weeks=2)
            self.due_date = due.strftime("%Y-%m-%d")
            self.checkouts += 1
            print(f"{self.title} checked out, due {self.due_date}.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if not self.available:
            self.available = True
            self.due_date = None
            print(f"{self.title} returned.")
        else:
            print(f"{self.title} was not checked out.")

    def __str__(self):
        status = "Available" if self.available else f"Checked out (due {self.due_date})"
        return f"[{self.id}] {self.title} by {self.author} — {status}"
    

def menu(library):
    while True:
        print("\nMenu:")
        print("1. View available books")
        print("2. Search by author/genre")
        print("3. Checkout a book")
        print("4. Return a book")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            for book in library:
                if book.available:
                    print(book)
        elif choice == "2":
            term = input("Search term: ").lower()
            for book in library:
                if term in book.author.lower() or term in book.genre.lower():
                    print(book)
        elif choice == "3":
            book_id = input("Book ID: ")
            for book in library:
                if book.id == book_id:
                    book.checkout()
        elif choice == "4":
            book_id = input("Book ID: ")
            for book in library:
                if book.id == book_id:
                    book.return_book()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    # You can use this space to test your functions
    pass
show_available_books(library_books)
print("---")
search_books(library_books, "fantasy")
print("---")
checkout_book(library_books, "B1")

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!