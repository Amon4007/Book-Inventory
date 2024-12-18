import sqlite3
from models.book import initialize_database

DATABASE_NAME = "database.db"

def add_book():
    """Add a new book to the inventory."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    status = input("Enter the status (Available/Checked Out): ")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, status) VALUES (?, ?, ?)",
        (title, author, status)
    )
    connection.commit()
    connection.close()
    print(f"Book '{title}' by {author} added successfully!")

def view_books():
    """View all books in the inventory."""
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()

    if books:
        print("\nBook Inventory:")
        print(f"{'ID':<5} {'Title':<20} {'Author':<20} {'Status'}")
        print("-" * 50)
        for book in books:
            print(f"{book[0]:<5} {book[1]:<20} {book[2]:<20} {book[3]}")
    else:
        print("No books found in the inventory.")

def update_book_status():
    """Update the status of a book."""
    book_id = input("Enter the ID of the book you want to update: ")
    new_status = input("Enter the new status (Available/Checked Out): ")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE books SET status = ? WHERE id = ?",
        (new_status, book_id)
    )
    connection.commit()
    connection.close()

    if cursor.rowcount:
        print(f"Book ID {book_id} status updated to '{new_status}'.")
    else:
        print(f"No book found with ID {book_id}.")

def delete_book():
    """Delete a book from the inventory."""
    book_id = input("Enter the ID of the book you want to delete: ")

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()

    if cursor.rowcount:
        print(f"Book ID {book_id} has been deleted.")
    else:
        print(f"No book found with ID {book_id}.")

def exit_program():
    """Exit the program."""
    print("Goodbye!")
    exit()
