import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

def login_to_twitter():
    chromedriver_autoinstaller.install()

    email = os.environ['EMAIL']
    username = os.environ['TWITTER_USERNAME']
    password = os.environ['TWITTER_PASSWORD']

    #chrome_driver_path = os.environ.get("CHROMEDRIVER_PATH", None)
    #chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
    
    chrome_options = Options()
    #chrome_options.binary_location = chrome_bin
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
   #driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)
    # ...
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
