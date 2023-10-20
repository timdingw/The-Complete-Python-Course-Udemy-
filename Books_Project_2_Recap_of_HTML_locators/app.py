import requests

from Books_Project_2_Recap_of_HTML_locators.pages.all_book_pages import AllBookPage

page_content = requests.get('https://books.toscrape.com').content
page = AllBookPage(page_content)

books = page.books

for book in books:
    print(book)