import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
import pandas as pd
import time
import openai

chromedriver_autoinstaller.install() 

chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

def login_to_twitter():
    

    email = os.environ['EMAIL']
    username = os.environ['TWITTER_USERNAME']
    password = os.environ['TWITTER_PASSWORD']
    number = os.environ['NUMBER']

    # ...
    print("After initializing driver")
    driver.get('https://twitter.com/i/flow/login')
    driver.implicitly_wait(10)
    time.sleep(3)

    # login 
    print("Before logging in")
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
    time.sleep(2)
    driver.switch_to.active_element.send_keys(number)
    time.sleep(1)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    time.sleep(5)
    print("After logging in")
    body = driver.find_element('tag name','body')
    print(body.text)

def scrap_tweets():

    # Open the list URL in a new tab
    print('opening new tab')
    driver.execute_script("window.open('');")
    print('switching to new tab')
    driver.switch_to.window(driver.window_handles[1])
    twitter_list_url = 'https://twitter.com/i/lists/1638664477859106816'
    print('opening list')
    driver.get(twitter_list_url)
    time.sleep(4)
    driver.switch_to.active_element.send_keys(Keys.END)
    time.sleep(5)

    # scrap and convert tweets to pandas dataframe
    tweets = driver.find_elements("xpath", '//div[@data-testid]//article[@data-testid="tweet"]')
    print('raw tweets:', tweets)
    body = driver.find_element('tag name','body')
    print(body.text)
    data = []
    for tweet in tweets:
        try:
            username = tweet.find_element("xpath", './/div[@dir="ltr"]/span').text
            date = tweet.find_element("xpath", './/time').get_attribute('datetime')
            content = tweet.find_element("xpath", './/div[@data-testid="tweetText"]').text
            permalink = tweet.find_element("xpath", './/a[contains(@href, "/status/")]').get_attribute('href')
            data.append([username, date, content, permalink])
        except NoSuchElementException:
            continue

    df = pd.DataFrame(data, columns=['Username', 'Date', 'Content', 'Tweet_Link'])

    return df

def generate_comment(content):

    openai.api_key = os.environ["OPENAI_API_KEY"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following tweet content, suggest a relevant comment:\n\nTweet: {content}"}
        ]
    )

    generated_comment = response.choices[0].message['content'].strip()
    return generated_comment


def add_comments_to_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Comment'] = ''

    for index, row in df.iterrows():
        if row['is_new']:
            df.at[index, 'Comment'] = generate_comment(row['Content'])

    return df
