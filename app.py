import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from utilities import login_to_twitter, scrap_tweets, add_comments_to_df
import openai
import urllib

app = Flask(__name__)
driver = None

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/submit_login', methods=['POST'])
def submit_login():
    email = request.form['email']
    username = request.form['username']
    number = request.form['number']
    password = request.form['password']
    api_key = request.form['api_key']
    list_url = request.form['list_url']
    
    # Zapisz dane jako zmienne środowiskowe
    os.environ['EMAIL'] = email
    os.environ['TWITTER_USERNAME'] = username
    os.environ['TWITTER_PASSWORD'] = password
    os.environ['NUMBER'] = number
    os.environ['OPENAI_API_KEY'] = api_key
    os.environ['TWITTER_LIST_URL'] = list_url

    global driver
    driver = login_to_twitter()

    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    
    tweets = scrap_tweets(driver)
    tweets_with_comments = add_comments_to_df(tweets)

    return render_template('dashboard.html', tweets=tweets_with_comments)


if __name__ == '__main__':
    app.run(debug=True)
