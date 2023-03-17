import requests
import datetime
from twilio.rest import Client
import os

account_sid = os.environ.get("OWM_API_KEY")
auth_token = os.environ.get("OWN_TOKEN")
client = Client(account_sid, auth_token)

parameters = {
    "lat": 25.0,
    "lon": 55.0,
    "exclude": "current,minutely,daily,alerts",
    "appid": "69f04e4613056b159c2761a9d9e664d2"
}

weather_data= {}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

# Get the timezone offset in seconds
timezone_offset = response.json()["timezone_offset"]

# Get the Unix timestamp for hourly data at index 0
hourly_timestamp = response.json()["hourly"][0]["dt"]

# Convert the Unix timestamp to a datetime object
local_time = datetime.datetime.utcfromtimestamp(hourly_timestamp + timezone_offset)

# print("Local time for hourly data at index 0:", local_time)

for time in range(0,12):
    weather_id= response.json()["hourly"][time]["weather"][0]["id"]
    weather_description = response.json()["hourly"][time]["weather"][0]["description"]
    weather_data[time]= {"id":weather_id,
                         "description":weather_description
                         }
# print(weather_data)

if min([x["id"] for x in weather_data.values()]) < 700:
    message = client.messages.create(
        body='It will rain today. Bring an umbrella',
        from_='whatsapp:+14155238886',
        to='whatsapp:+971508964120'
    )
else:
    message = client.messages.create(
        body="Today's weather is great!",
        from_='whatsapp:+14155238886',
        to='whatsapp:+971508964120'
    )

print(message.status)
