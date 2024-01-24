import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "64a630c9be5944fc8cf59cd00a69b92e"
account_sid = "AC8e5c09e87e9054543d1201886cf27994"
auth_token = ("aeec0d78cf29223d13be75476cad192e")

weather_params = {
    "lat": -23.010031,
    "lon": -44.318649,
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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+18447252612",
        to="+1 435 840 1494"
    )
    print(message.status)
