from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from time import sleep

GOOGLE_FORM = "YOUR_FORM_URL_HERE"
CHROME_DRIVER_PATH = "DRIVER_PATH_HERE"
# Go to Zillow, select all filter preferences and copy URL
ZILLOW_ADDRESS = "ZILLOW_URL_HERE"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
# Resquests hmtl and makes soup
response = requests.get(ZILLOW_ADDRESS, headers=header)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

# Finds link tags and makes list of filtered data
link_tags = soup.select(".list-card-top a")
link_list = []
for tag in link_tags:
    href = tag["href"]
    if "http" not in href:
        href = "https://www.zillow.com/homedetails"+href[2:]
    link_list.append(href)

# Finds address tags and makes list of filtered data
address_tags = soup.select(".list-card-info address")
address_list = []
for tag in address_tags:
    address = tag.get_text()
    if " | " in address:
        split_address = address.split(" | ")
        address = split_address[1]
    address_list.append(address)

# Finds price tags and makes list of filtered data
price_tags = soup.select(".list-card-heading div")
price_list = []
for tag in price_tags:
    price = tag.get_text()
    price_list.append(price)

# Starts driver
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

# Fills info with lists of data
for a,p,l in zip(address_list, price_list, link_list):
    driver.get(GOOGLE_FORM)
    sleep(10)
    inputs = driver.find_elements(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_input = inputs[0]
    price_input = inputs[1]
    link_input = inputs[2]
    submit = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    address_input.send_keys(a)
    sleep(2)
    price_input.send_keys(p)
    sleep(2)
    link_input.send_keys(l)
    sleep(2)
    submit.click()
    sleep(4)
