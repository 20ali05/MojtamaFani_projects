import sqlite3

class Ketab:
    def __init__(self, name, author, publish_year, book_type):
        self.name = name
        self.author = author
        self.publish_year = publish_year
        self.book_type = book_type

class Manage:
    @staticmethod
    def add(book):
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO books (name, author, publish_year, book_type) VALUES (?, ?, ?, ?)
        ''', (book.name, book.author, book.publish_year, book.book_type))
        conn.commit()
        conn.close()

    @staticmethod
    def search(key):
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM books WHERE name LIKE ? OR author LIKE ? OR publish_year LIKE ? OR book_type LIKE ?
        ''', (f'%{key}%', f'%{key}%', f'%{key}%', f'%{key}%'))
        rows = cursor.fetchall()
        conn.close()
        found_books = [f"{i+1}. Name: {row[1]}, Author: {row[2]}, Publish Year: {row[3]}, Type: {row[4]}" for i, row in enumerate(rows)]
        return found_books

    @staticmethod
    def list_all_books():
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        conn.close()
        all_books = [f"{i+1}. Name: {row[1]}, Author: {row[2]}, Publish Year: {row[3]}, Type: {row[4]}" for i, row in enumerate(rows)]
        return all_books

    @staticmethod
    def delete(key):
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM books WHERE name LIKE ? OR author LIKE ? OR publish_year LIKE ? OR book_type LIKE ?
        ''', (f'%{key}%', f'%{key}%', f'%{key}%', f'%{key}%'))
        conn.commit()
        rows_affected = cursor.rowcount
        conn.close()
        return rows_affected > 0
