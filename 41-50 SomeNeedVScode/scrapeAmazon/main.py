import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Canon-iP8720-Wireless-AirPrint-Compatible/dp/B00HM0IV52/ref=sr_1_6?keywords=canon+pixma&qid=1705432698&sr=8-6&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

# Correct class name to extract the price
price = soup.find(class_="a-price").get_text(strip=True)
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
