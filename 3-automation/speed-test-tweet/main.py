from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = int("YOUR_PROMISED_DOWNLOAD_SPEED")
PROMISED_UP = int("YOUR_PROMISED_UPLOAD_SPEED")
PROVIDER = "YOUR_PROVIDER_@_HERE"
EMAIL = "YOUR_EMAIL_HERE"
PASS = "YOUR_EMAIL_HERE"
DRIVER_PATH = "CHROME_DRIVER_PATH_HERE"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH))
        self.up = str
        self.down = str

    # Tests speed
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.CLASS_NAME, "start-text")
        go.click()
        sleep(40)
        download_speed = self.driver.find_element(By.XPATH,
                                                  "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]"
                                                  "/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.down = download_speed.text
        upload_speed = self.driver.find_element(By.XPATH,
                                                "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]"
                                                "/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
        self.up = upload_speed.text

    # Tweets complaints
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(8)
        email = self.driver.find_element(By.CSS_SELECTOR, "input[autocomplete='username']")
        email.send_keys(EMAIL)
        email.send_keys(Keys.ENTER)
        sleep(8)
        password = self.driver.find_element(By.CSS_SELECTOR, "input[autocomplete='current-password']")
        password.send_keys(PASS)
        password.send_keys(Keys.ENTER)
        sleep(8)
        tweet = self.driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/"
                                         "div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/"
                                         "div[1]/div/div/div/div/div[2]/div/div/div/div")
        tweet.send_keys(f"Hi {PROVIDER}, my promised download speed is {PROMISED_DOWN}mb and upload "
                        f"{PROMISED_UP}mb, however my current download speed is {self.down}mb and self.up}mb for upload")
        enter = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div"
                                                  "/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div")
        enter.click()
        sleep(8)


st = InternetSpeedTwitterBot()
st.get_internet_speed()
st.tweet_at_provider()
