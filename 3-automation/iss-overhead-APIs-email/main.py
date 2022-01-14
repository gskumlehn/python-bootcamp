import requests
from datetime import datetime
from time import sleep
import smtplib


#FILL WITH YOUR GMAIL
EMAIL = "YOUR_EMAIL_GOES_HERE"
PASSWORD = "YOUR_PASSWORD_GOES_HERE"
# Joinville, SC, BRAZIL ###   INSERT YOUR LOCATION   ###
MY_LAT = -26.304760
MY_LNG = -48.845871

# Resquests the iss API for its location, and compares with your location
def iss_is_close():
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_latitude = float(iss_data['iss_position']['latitude'])
    iss_longitude = float(iss_data['iss_position']['longitude'])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True
    else:
        return False

# Requests weather API to check if its nighttime, comparing with the hour of day from datetime
def is_nighttime():
    sun_parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }
    sun_response = requests.get('https://api.sunrise-sunset.org/json', params=sun_parameters)
    sun_data = sun_response.json()
    sunrise = int(sun_data['results']['sunrise'].split('T')[1][0:2])
    sunset = int(sun_data['results']['sunset'].split('T')[1][0:2])
    time_now = datetime.now().hour +3
    if sunset <= time_now <= sunrise:
        return True
    else:
        return False


# If both the iss is overhead and is nightime to email yourself with the warning that the iss is overhead and might be visible
while not iss_is_close() and not is_nighttime():
    sleep(60*5)

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg='Subject:ISS Overhead\n\nHello. today the ISS is passing through your skies during nightime, be sure to look up and search for it!')
