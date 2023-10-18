from utils import database_2


menu = ("""
    'e':enter',
    'l':list',
    'r':read',
    'd':delete',
    'x':exit'.
    please enter your action: """)

def run_menu():
    database_2.create_book_table()
    user_input = input(menu)
    while user_input != 'x':
        if user_input == 'e':
            enter_book_info()
        elif user_input == 'l':
            list_all_book()
        elif user_input == 'r':
            read_book_name()
        elif user_input == 'd':
            delete_book_name()
        user_input = input(menu)

def enter_book_info():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    database_2.enter_book(name, author)

def list_all_book():
    for book in database_2.list_book():
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} — Read: {read}")
    # database.list_book()

def read_book_name():
    name = input('Enter the book name: ')
    database_2.read_book(name)

def delete_book_name():
    name = input('Enter the book name: ')
    database_2.delete_book(name)



run_menu()
# enter_book_info()

