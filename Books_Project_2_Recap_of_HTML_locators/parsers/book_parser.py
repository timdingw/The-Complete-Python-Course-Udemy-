import re

# from Books_Project_2_Recap_of_HTML_locators.pages.all_book_pages import AllBookPage
from Books_Project_2_Recap_of_HTML_locators.locators.book_locators import BookLocators


class BookParser:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price}, ({self.rating}) stars>'
        # return f'{self.rating}'

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name
# select_one(locator) is a method provided by BeautifulSoup
# (often referred to as a BeautifulSoup "selector") to locate the first HTML element that matches the provided locator.
# The locator is typically a CSS selector.

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class'] # ['star_rating' 'Three']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0], 9)
        return rating_number