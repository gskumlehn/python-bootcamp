from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep


EMAIL = "YOUR_EMAIL_HERE"
PASSWORD "YOUR_PASSWORD_HERE"
CHROME_DRIVER_PATH = "YOUR_CHROME_DRIVER_PATH_HERE"

# Opens tinder page in Chrome driver
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
driver.get("https://tinder.com")
driver.set_window_size(1700, 1000)
sleep(10)

# Logs in using Facebook popup
log_in = driver.find_element(By.LINK_TEXT, "Entre")
log_in.click()
sleep(5)
with_facebook = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
with_facebook.click()
sleep(10)
facebook_page = driver.window_handles[1]
tinder_page = driver.window_handles[0]
driver.switch_to.window(facebook_page)
email = driver.find_element(By.ID, "email")
email.send_keys(EMAIL)
password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
sleep(10)

# Returns to tinder page and accepts popups
driver.switch_to.window(tinder_page)
aceito = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/button")
aceito.click()
sleep(10)
permitir = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
permitir.click()
sleep(5)
interesse = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[2]")
interesse.click()
sleep(5)

# Starts swipings right
like = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
for _ in range(100):
    try:
        like.click()
    except ElementClickInterceptedException:
        exit = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button")
        exit.click()
    finally:
        sleep(5)