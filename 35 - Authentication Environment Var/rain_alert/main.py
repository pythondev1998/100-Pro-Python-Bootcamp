import requests

import os
from twilio.rest import Client

client = Client("AC116c37b1987c3093664d726b1bbd2e3a", "b97f91cfb411cb7ce51f4518ceff0e58")

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall?"
api_key = ""

weather_params = {
    "lat": 18.5001200,
    "lon": -69.9885700,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["hourly"] [0:12])
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]  # Next weather condition 12 hours

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="Hello.",
        from_='+12708133850',
        to='+1829721'
    )
    print(message.status)
