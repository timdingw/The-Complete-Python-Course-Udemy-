from .database_connection import DatabaseConnection

book_list = 'books2.db'

def create_book_table():
    with DatabaseConnection(book_list) as conn:
        cursor = conn.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def enter_book(name, author):
    with DatabaseConnection(book_list) as conn:
        cursor = conn.cursor()

        cursor.execute('INSERT INTO books VALUES(?,?,0)',(name, author))


def list_book():
    with DatabaseConnection(book_list) as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0],'author': row[1],'read': row[2]} for row in cursor.fetchall()]
        return books


def read_book(name):
    with DatabaseConnection(book_list) as conn:
        cursor = conn.cursor()

        cursor.execute('UPDATE books SET read = 1 WHERE name = ?',(name,)) # "," after first parameter



def delete_book(name):
    with DatabaseConnection(book_list) as conn:
        cursor = conn.cursor()

        cursor.execute('DELETE FROM books WHERE name = ?',(name,)) # "," after first parameter

