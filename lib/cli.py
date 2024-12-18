from helpers import (
    add_book,
    view_books,
    update_book_status,
    delete_book,
    exit_program
)
from models.book import initialize_database

def main():
    """Main function to run the Book Inventory CLI."""
    initialize_database()  # Initialize database and tables
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book_status()
        elif choice == "4":
            delete_book()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def menu():
    """Display the main menu."""
    print("\nBook Inventory Management CLI")
    print("1. Add a book")
    print("2. View all books")
    print("3. Update book status")
    print("4. Delete a book")
    print("0. Exit")

if __name__ == "__main__":
    main()
