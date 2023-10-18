from bs4 import BeautifulSoup

from Milestone_Project_3_A_Quote_Scraper.locators.quotes_page_locators import QuotesPageLocators
from Milestone_Project_3_A_Quote_Scraper.parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]

