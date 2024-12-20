import sqlite3

DATABASE_NAME = 'book_inventory.db'

def create_connection():
    """Create a database connection."""
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    """Create tables for authors and books."""
    conn = create_connection()
    cursor = conn.cursor()

    # Create authors table
    cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')

    # Create books table
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors (id)
    )''')

    conn.commit()
    conn.close()
