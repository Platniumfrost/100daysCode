import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("64a630c9be5944fc8cf59cd00a69b92e")
account_sid = "AC8e5c09e87e9054543d1201886cf27994"
auth_token = os.environ.get("5c414215de4eb30b1406886e34105241")

weather_params = {
    "lat": -17.847290,
    "lon": 25.856310,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()



will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        Body="It's going to rain today. remember to bring an umbrella",
        From="+18447252612",
        To="+4358401494"
    )
    print(message.status)