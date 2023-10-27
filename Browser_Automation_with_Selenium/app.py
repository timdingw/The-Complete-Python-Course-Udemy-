from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Browser_Automation_with_Selenium.pages.quotes_pages import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter the tag you'd like quotes from: ")

    service = Service("E:\ChromeDriver(python)\chromedriver.exe")
    chrome = webdriver.Chrome(service = service)
    chrome.get('https://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))

except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occured. Please try again")


# authors = page.get_available_authors() # Tim
# print("Select one of these tags: {}".format(" \n ".join(authors))) # Tim
#
# author = input("Enter the author you'd like quotes from: ")
# page.select_author(author)
#
# tags = page.get_available_tags()
# print("Select one of these tags: {}".format(" | ".join(tags)))
# selected_tag = input("Enter your tag: ")
#
# page.select_tag(selected_tag)
# page.search_button.click()
#
# print(page.quotes)


