import requests
from twilio.rest import Client

# Insert your Location here (Joinville, SC, Brazil)
lat = -26.3051
lon = -48.8461

# Insert your numbers here
TWILLIO_NUMBER = "YOUR_TWILLIO_NUMBER_HERE"
YOUR_NUMBER = "YOUR_NUMBER_HERE"

# Insert your API information here
url_onecall = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "YOUR_API_KEY_HERE"
account_sid = "YOUR_ACCOUNT_SID_HERE"
auth_token ="YOUR_AUTH_TOKEN_HERE"

onecall_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "units": "metric",
    "exclude": "current,minutely,daily",
}

# Requests weather data
onecall_response = requests.get(url=url_onecall, params=onecall_params)
onecall_response.raise_for_status()
data_onecall = onecall_response.json()
next12h = data_onecall["hourly"][0:12]

# Checks in data if it's going to rain
need_umbrella = False
for hour in next12h:
    if hour["weather"][0]["id"] < 700:
        need_umbrella = True
    else:
        continue

# In case it rains, sends SMS to your phone from Twillio app
if need_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Don't forget your umbrella, it might rain!",
        from_=TWILLIO_NUMBER,
        to=YOUR_NUMBER)
    print(message.status)
