import requests
import datetime as dt
from twilio.rest import Client


def update_date():
    global date, date_str
    date = date - dt.timedelta(days=1)
    date_str = str(date)


TWILLIO_NUMBER = "YOUR_TWILLIO_NUMBER_HERE"
YOUR_NUMBER = "YOUR_NUMBER_HERE"

COMPANY_NAME = "COMPANY_YOU_WANT_TO_TRACK_HERE"
COMPANY_SYMBOL = "COMPANY_SYMBOL_HERE"

# Check todays date
today = dt.date.today()
date = today
date_str = str(date)
# Alpha Vantage API
stock_url = "https://www.alphavantage.co/query"
stock_key = "YOUR_ALPHAVANTEGE_KEY_HERE"
# News API
news_url = "https://newsapi.org/v2/everything"
news_key = "YOUR_NEWS_KEY_HERE"
# Twilio API
account_sid = "YOUR_TWILLIO_SID_HERE"
auth_token = "YOUR_AUTH_TOKEN_HERE"


# Switch for an input
search_for = COMPANY_SYMBOL
# Searches for the correct symbol used inside the AlphaVantage API
search_params = {
    "function": "SYMBOL_SEARCH",
    "keywords": search_for,
    "apikey": stock_key
}
search_response = requests.get(url=stock_url, params=search_params)
search_response.raise_for_status()
search_data = search_response.json()
symbol_found = search_data["bestMatches"][0]["1. symbol"]

# Requests the data using the correct company symbol
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": symbol_found,
    "apikey": stock_key,
}
stock_response = requests.get(url=stock_url, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']

# Extracts and calculate the % difference between the last Closing value and the Closing value of the day before
while True:
    try:
        stock_data[date_str]
    except KeyError:
        update_date()
    else:
        last_day = float(stock_data[date_str]['4. close'])
        update_date()
        break
while True:
    try:
        stock_data[date_str]
    except KeyError:
        update_date()
    else:
        day_before = float(stock_data[date_str]['4. close'])
        break
variation = last_day*100/day_before - 100

# Requests news data using newsapi.org and formats it into a message
news_params = {
    "q": COMPANY_NAME,
    "from": str(today),
    "sortBy": "popularity",
    "apiKey": news_key,
}
news_response = requests.get(url=news_url, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
articles = news_data['articles'][:3]
messages = []

if variation > 0:
    up_or_down = "🔺"
else:
    up_or_down = "🔻"
for article in articles:
    i = articles.index(article)
    message = f'{symbol_found}: {up_or_down}{abs(round(variation, 3))}%\n' \
              f'Headline: {articles[i]["title"]}\n' \
              f'Brief: {articles[i]["description"]}'
    messages.append(message)


if abs(variation) >= 5:
    for msg in messages:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(body=msg, from_=TWILLIO_NUMER, to=YOUR_NUMBER)
        print(message.status)

