from bs4 import BeautifulSoup

from Books_Project_2_Recap_of_HTML_locators.locators.all_book_page import AllBooksPageLocators
from Books_Project_2_Recap_of_HTML_locators.parsers.book_parser import BookParser


class AllBookPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
