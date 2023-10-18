import requests

from Milestone_Project_3_A_Quote_Scraper.pages.quotes_pages import QuotesPage
from Milestone_Project_3_A_Quote_Scraper.parsers.quote import QuoteParser

page_content = requests.get('https://quotes.toscrape.com/').content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote)

# for quote in page.quotes:
#     QuoteParser.author(quote)


