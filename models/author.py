from models.database import create_connection

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Author name cannot be empty.")
        self._name = value

    @classmethod
    def create(cls, name):
        """Create a new author and add to the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, author_id):
        """Delete an author from the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM authors WHERE id = ?', (author_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Get all authors from the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()
        conn.close()
        return authors

    @classmethod
    def find_by_id(cls, author_id):
        """Find an author by ID."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        author = cursor.fetchone()
        conn.close()
        return author
