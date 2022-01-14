import smtplib
import datetime as dt
import pandas as pd
from random import randint

# Fill with your info
my_email = 'YOUR_EMAIL_GOES_HERE'
my_pass = 'YOUR_PASSWORD_GOES_HERE'

# Reads csv file of people with email and birthday data
df = pd.read_csv('data.csv')
birthday_dict = {(data.month, data.day): data for (index, data) in df.iterrows()}

# Get date data of today in the form os a tuple (month,date)
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Checks if today matches with any birthdays and calculates age
if today_tuple in birthday_dict:
    person = birthday_dict[today_tuple]
    age = today.year - person.year
    # Randomizes a birthday wish Letter template and fills with persons data
    with open(f'letters\letter{randint(1, 3)}.txt') as file:
        letter = file.read()
        letter = letter.replace('[NAME]', person['name'])
    # Opens smtplip connection and sends email with the persons age in the subject and letter as de body
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs=person['email'],
                            msg=f'Subject:Happy {age}th Birthday!!\n\n{letter}')
