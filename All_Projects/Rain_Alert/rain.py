import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "ACd400fd8415d4644bb07e343403fb1636"
auth_token = "2f9bca9a32431b4ed47a34cdb4e4fb3e"

api_key = "1135efa285c7f2e26265e1a9c53c1d59"

parameter = {
    "lat": 28.626230,
    "lon": 77.394096,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)

weather_data = response.json()
weather_condition = weather_data["hourly"][:12]

will_rain = False

for hourly_data in weather_condition:
    weather_condition_code = hourly_data["weather"][0]["id"]
    if 500 <= weather_condition_code <= 600:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an ☂️",
                from_="+19032823075",
                to="+918076431825")

    print(message.status)
