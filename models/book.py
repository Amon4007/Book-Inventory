from models.database import create_connection

class Book:
    def __init__(self, title, genre, author_id):
        self.title = title
        self.genre = genre
        self.author_id = author_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Book title cannot be empty.")
        self._title = value

    @classmethod
    def create(cls, title, genre, author_id):
        """Create a new book and add to the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, genre, author_id) VALUES (?, ?, ?)',
                       (title, genre, author_id))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, book_id):
        """Delete a book from the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Get all books from the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()
        return books

    @classmethod
    def find_by_id(cls, book_id):
        """Find a book by ID."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book
