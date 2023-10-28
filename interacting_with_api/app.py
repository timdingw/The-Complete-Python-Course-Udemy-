import requests
from libs.openexchange import OpenExchangeClient

APP_ID = '2a042b47583742aea5a882022d43073c'
# END_POINT = 'https://openexchangerates.org/api/latest.json'

# response = requests.get(f"{END_POINT}?app_id={APP_ID}")
# exchange_rates = response.json()["rates"]

# usd_amount = 100
# cad_amount = usd_amount * exchange_rates["CAD"]
# cny_amount = usd_amount * exchange_rates["CNY"]
# cny_amount = usd_amount * exchange_rates["CNY"]
# exchange_rate_cny_cad = cny_amount/cad_amount
#
# print(f"USD{usd_amount} is CAD{cad_amount}")
# print(f"USD{usd_amount} is CNY{cny_amount}")
# print(f"CAD{usd_amount} is CNY{100*exchange_rate_cny_cad}")

client = OpenExchangeClient(APP_ID)

amount = 100
from_currency = input("Please enter your base currency: ").upper() # "CAD"
to_currency = input("Please enter your quote currency: ").upper() # "CNY"
# cad_amount = client.covert(usd_amount,"USD","CAD")
to_currency_amount = round(client.covert(amount,from_currency,to_currency),2)

print(f"{from_currency}{amount} is {to_currency}{to_currency_amount}")