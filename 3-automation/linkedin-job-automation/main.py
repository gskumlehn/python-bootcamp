from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep


# Search for jobs in linkein, input desired filters and add URL here (don't forget easy apply)
LINKEDIN_URL = "URL_HERE"

EMAIL = "YOUR_EMAIL_HERE"
PASSWORD = "YOUR_PASWORD_HERE"
CHROME_DRIVER_PATH = "YOUR_CHROME_DRIVER_PATH_HERE"

# Opens chrome driver in linkedin page
drive = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
drive.get(LINKEDIN_URL)

actions = ActionChains(drive)

# Logs in
entrar = drive.find_element(By.CLASS_NAME, "nav__button-secondary")
entrar.click()
sleep(3)
username = drive.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = drive.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
sleep(3)

# Finds list of jobs
jobs = drive.find_elements(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li/div/div/div[1]/div[2]/div[1]/a")

# EASY APPLIES
for job in jobs:
    job.click()
    sleep(5)
    try:
        apply_button = drive.find_element(By.XPATH, '//button[normalize-space()="Apply now"]')
    except NoSuchElementException:
        continue
    else:
        sleep(5)
        apply_button.click()
        sleep(5)
        try:
            submit = drive.find_element(By.XPATH, '//button[normalize-space()="Submit application"]')
        except NoSuchElementException:
            sleep(5)
            actions.send_keys(Keys.ESCAPE)
            actions.perform()
            sleep(5)
            discard = drive.find_element(By.XPATH, '//button[normalize-space()="Discard"]')
            discard.click()
            sleep(5)
        else:
            submit.click()
            sleep(5)
            actions.send_keys(Keys.ESCAPE)
            actions.perform()
            sleep(5)
