from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = "CHROME_DRIVER_PATH_HERE"
SIMILAR_ACCOUNT = "SIMILAR_ACCOUNT_NAME_HERE"
USERNAME = "USERNAME_HERE"
PASSWORD = "PASSWORD_HERE"


class InstaFollower:

    # Initiates driver
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

    # Logs in
    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(8)
        user = self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        user.send_keys(USERNAME)
        password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(8)

    # Finds similar account's followers
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        sleep(4)
        followers = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        sleep(5)
        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    # Follows accounts
    def follow(self):
        button_list = self.driver.find_elements(By.XPATH, "/html/body/div[6]/div/div/div[2]/ul/div/li/div/div[2]/button")
        print(len(button_list))
        for button in button_list:
            button.click()
            sleep(4)


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()

