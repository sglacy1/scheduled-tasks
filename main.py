import requests
from twilio.rest import Client
import os

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ["OWM_API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

weather_parameters = {
    "lat": 36.169941,
    "lon": -115.139832,
    "units": "imperial",
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)

weather_list = weather_data["list"]
# print(weather_list)

condition_list = []

for weather in weather_list:
    weather_id = weather["weather"][0]["id"]
    # print(weather_id)
    condition_list.append(weather_id)

will_rain = False

for condition in condition_list:
    if condition < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18444031304',
        body="It's going to rain today. Bring an ☂️",
        to='+18777804236'
    )

    print(message.status)


