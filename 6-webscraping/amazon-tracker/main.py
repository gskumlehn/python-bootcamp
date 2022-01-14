import requests
from bs4 import BeautifulSoup
import smtplib

# Insert your data here
EMAIL = 'YOUR_GMAIL_HERE'
PASSWORD = 'YOUR_PASSWORD_HERE'
PRODUCT_URL = "ADD_URL_OF_PRODUCT_HERE"
PRICE_GOAL = int("ADD PRICE GOAL HERE")

# Gets products name from URL
PRODUCT_NAME = " ".join(PRODUCT_URL.split("/")[3].split("-"))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

# Requests html page and makes soup
response = requests.get(PRODUCT_URL,
                        headers=headers)
amazon_html = response.text
soup = BeautifulSoup(amazon_html, "lxml")

# Finds tag with price
price_tag = soup.find("span", class_="a-offscreen")
# Filters price into float
price = float(f'{price_tag.getText().split("$")[1].split(",")[0]}.{price_tag.getText().split("$")[1].split(",")[1]}')

# If price is equal or lower than the goal sends email to yourself
if price <= PRICE_GOAL:
    # Creates Message
    msg = f"Subject:AMAZON PRICE ALERT \n\nThe product you've been tracking: {PRODUCT_NAME} \nHas reached price goals: {PRICE_GOAL}\nCheck it out in {PRODUCT_URL}"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=msg)
