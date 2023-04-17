import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def login_to_twitter():
    email = os.environ['EMAIL']
    username = os.environ['TWITTER_USERNAME']
    password = os.environ['TWITTER_PASSWORD']

    chrome_driver_path = os.environ.get("GOOGLE_CHROME_SHIM", None))
    chrome_bin = ENV.fetch('GOOGLE_CHROME_SHIM', nil)
    chrome_options.binary_location = chrome_bin
    service = Service(executable_path=chrome_driver_path)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://twitter.com/i/flow/login')
    driver.implicitly_wait(10)
    time.sleep(3)

    # Press the 'Tab' key three times
    for _ in range(3):
        driver.switch_to.active_element.send_keys(Keys.TAB)
        time.sleep(0.5)  # Wait a bit between key presses

    # Type in the email address and press 'Enter'
    driver.switch_to.active_element.send_keys(email)
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.switch_to.active_element.send_keys(username)
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.switch_to.active_element.send_keys(password)
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    time.sleep(5)

    return driver
