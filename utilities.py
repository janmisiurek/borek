import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
import pandas as pd
import time

def login_to_twitter():
    chromedriver_autoinstaller.install()

    email = os.environ['EMAIL']
    username = os.environ['TWITTER_USERNAME']
    password = os.environ['TWITTER_PASSWORD']
    number = os.environ['NUMBER']

    #chrome_driver_path = os.environ.get("CHROMEDRIVER_PATH", None)
    #chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
    
    chrome_options = Options()
    #chrome_options.binary_location = chrome_bin
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    
   #driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)
    # ...
    driver.get('https://twitter.com/i/flow/login')
    driver.implicitly_wait(10)
    time.sleep(3)

    # login 
    for _ in range(3):
        driver.switch_to.active_element.send_keys(Keys.TAB)
        time.sleep(0.5)  # Wait a bit between key presses

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
    driver.switch_to.active_element.send_keys(number)
    time.sleep(1)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    time.sleep(2)

    # open list link in new tab
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    twitter_list_url = 'https://twitter.com/i/lists/1638664477859106816'
    driver.get(twitter_list_url)
    time.sleep(4)
    driver.switch_to.active_element.send_keys(Keys.END)
    time.sleep(5)

    
    # scrap and convert tweets to pandas dataframe
    tweets = driver.find_elements("xpath", '//div[@data-testid]//article[@data-testid="tweet"]')
    
    
    data = []
    for tweet in tweets:
        try:
            username = tweet.find_element("xpath", './/div[@dir="ltr"]/span').text
            date = tweet.find_element("xpath", './/time').get_attribute('datetime')
            content = tweet.find_element("xpath", './/div[@data-testid="tweetText"]').text  # Zaktualizowany selektor XPath
            data.append([username, date, content])
        except NoSuchElementException:
            continue
    df = pd.DataFrame(data, columns=['Username', 'Date', 'Content'])
    
    return df
