# Book Inventory System

## Overview

The **Book Inventory System** is a Python-based Command-Line Interface (CLI) application designed to manage books and authors in a database. Users can perform various actions, including adding authors and books, viewing records, deleting entries, and navigating through an intuitive menu system. By Amon

## Features

- **Add Authors**: Insert new authors into the database.
- **Add Books**: Add books with associated genres and authors.
- **View All Records**:
  - Display all authors.
  - Display all books.
- **Delete Records**:
  - Remove authors.
  - Remove books.
- **Error Handling**: Ensures proper input validation and provides informative error messages.
- **Database Management**: Utilizes SQLite for storing and managing data.

## Project Structure

```
Book-Inventory/
├── cli.py                # Main CLI application
├── models/
│   ├── __init__.py       # Package initializer
│   ├── database.py       # Database connection and table creation
│   ├── author.py         # Author model
│   └── book.py           # Book model
├── Pipfile               # Dependency management
├── Pipfile.lock          # Lockfile for dependencies
└── README.md             # Project documentation
```

## Requirements

- Python 3.7+
- SQLite3

### Dependencies

Dependencies are managed using `pipenv`. Install them with:

```bash
pipenv install
```

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Book-Inventory
   ```

2. Install dependencies:

   ```bash
   pipenv install
   ```

3. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

4. Run the application:

   ```bash
   python cli.py
   ```

## Usage Instructions

Upon running the application, you will see a menu with the following options:

### Main Menu

1. **Add Author**: Input an author's name to add them to the database.
2. **Add Book**: Enter book details, including title, genre, and associated author.
3. **View All Authors**: Lists all authors in the database.
4. **View All Books**: Lists all books, including their titles, genres, and authors.
5. **Delete Author**: Remove an author by specifying their ID.
6. **Delete Book**: Remove a book by specifying its ID.
7. **Exit**: Close the application.

### Example Workflow

1. Start the application:
   ```bash
   python cli.py
   ```
2. Add an author (e.g., "J.K. Rowling").
3. Add a book (e.g., "Harry Potter", genre: "Fantasy", author: "J.K. Rowling").
4. View the list of books to confirm the entry.
5. Delete an entry if needed.
6. Exit the application.

## Database Schema

### Authors Table

| Column | Type    | Constraints                |
| ------ | ------- | -------------------------- |
| id     | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| name   | TEXT    | UNIQUE, NOT NULL           |

### Books Table

| Column     | Type    | Constraints                |
| ---------- | ------- | -------------------------- |
| id         | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| title      | TEXT    | NOT NULL                   |
| genre      | TEXT    | NOT NULL                   |
| author\_id | INTEGER | FOREIGN KEY(authors.id)    |

## Contributing

Contributions are welcome! If you encounter bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Special thanks to the developers of Python and SQLite for providing robust tools to build this project.

