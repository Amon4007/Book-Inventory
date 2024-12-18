import sqlite3

# Database initialization
DATABASE_NAME = "database.db"

def initialize_database():
    """Create the books table if it does not exist."""
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Create books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()
