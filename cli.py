from models.author import Author
from models.book import Book
from models.database import create_tables

def show_menu():
    """Display the main menu for the user."""
    print("\n--- Book Inventory System ---")
    print("1. Add Author")
    print("2. Add Book")
    print("3. View All Authors")
    print("4. View All Books")
    print("5. Delete Author")
    print("6. Delete Book")
    print("7. Exit")
    choice = input("Choose an option: ")
    return choice

def add_author():
    """Allow the user to add a new author."""
    name = input("Enter author's name: ")
    try:
        Author.create(name)
        print(f"Author '{name}' added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def add_book():
    """Allow the user to add a new book."""
    title = input("Enter book title: ")
    genre = input("Enter book genre: ")
    author_id = input("Enter author ID: ")
    try:
        Book.create(title, genre, author_id)
        print(f"Book '{title}' added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def view_all_authors():
    """Display all authors."""
    authors = Author.get_all()
    print("\n--- Authors ---")
    for author in authors:
        print(f"ID: {author[0]}, Name: {author[1]}")

def view_all_books():
    """Display all books."""
    books = Book.get_all()
    print("\n--- Books ---")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Genre: {book[2]}, Author ID: {book[3]}")

def delete_author():
    """Allow the user to delete an author."""
    author_id = input("Enter author ID to delete: ")
    Author.delete(author_id)
    print(f"Author with ID {author_id} deleted.")

def delete_book():
    """Allow the user to delete a book."""
    book_id = input("Enter book ID to delete: ")
    Book.delete(book_id)
    print(f"Book with ID {book_id} deleted.")

def main():
    """Main function to run the CLI app."""
    create_tables()  # Ensure the tables exist before we start
    while True:
        choice = show_menu()

        if choice == '1':
            add_author()
        elif choice == '2':
            add_book()
        elif choice == '3':
            view_all_authors()
        elif choice == '4':
            view_all_books()
        elif choice == '5':
            delete_author()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
