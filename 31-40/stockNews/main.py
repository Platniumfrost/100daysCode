import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "+18447252612"
VERIFIED_NUMBER = "+14358401494"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "5276PQ5W2IJZXOPS"
NEWS_API_KEY = "0991a94721164ad8a4b751eae6d28fa9"
TWILIO_SID = "AC8e5c09e87e9054543d1201886cf27994"
TWILIO_AUTH_TOKEN = "aeec0d78cf29223d13be75476cad192e"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "UP"
else:
    up_down = "DOWN"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)



if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)


    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    try:
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_=VIRTUAL_TWILIO_NUMBER,
                to=VERIFIED_NUMBER
            )
            print(f"Message sent successfully to {VERIFIED_NUMBER}. SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

