import sqlite3
import os

# Define the database file name
DB_FILE = "database.db"

def create_connection():
    """
    Establish a connection to the SQLite database. Creates the database file if it doesn't exist.
    """
    try:
        # Check if the database file exists
        if not os.path.exists(DB_FILE):
            print(f"Database file '{DB_FILE}' does not exist. Creating a new database.")
        # Connect to the database
        conn = sqlite3.connect(DB_FILE)
        print("Connected to the database successfully.")
        return conn
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        raise

def create_tables():
    """
    Create or alter the tables for the database.
    """
    try:
        conn = create_connection()
        cursor = conn.cursor()

        # Create authors table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        print("Authors table created successfully (if not existing).")

        # Check if the genre column exists in the books table
        cursor.execute("PRAGMA table_info(books)")
        columns = [column[1] for column in cursor.fetchall()]

        if 'genre' not in columns:
            cursor.execute("ALTER TABLE books ADD COLUMN genre TEXT NOT NULL DEFAULT 'Unknown'")
            print("Genre column added to books table.")

        conn.commit()
        conn.close()
    except sqlite3.DatabaseError as e:
        print(f"Error creating or altering tables: {e}")
        raise
