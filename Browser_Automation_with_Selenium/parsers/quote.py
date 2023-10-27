from selenium.webdriver.common.by import By
from Browser_Automation_with_Selenium.locators.quote_locators import QuoteLocators

class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about
    the quote (quote content, author, tags).
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.find_element(By.CSS_SELECTOR, locator).text # element

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text # element

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return self.parent.find_element(By.CSS_SELECTOR, locator) # element