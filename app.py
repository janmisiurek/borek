import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from utilities import login_to_twitter, scrap_tweets, add_comments_to_df
import openai
import urllib
import pandas as pd

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
    import pandas as pd
    import os

    # Wczytaj ostatnie tweety z pliku CSV, jeśli istnieje
    if os.path.exists('last_tweets.csv'):
        last_tweets = pd.read_csv('last_tweets.csv')
    else:
        last_tweets = pd.DataFrame()

    # Pobierz nowe tweety
    tweets = scrap_tweets(driver)

    # Oznacz tweety jako nowe, jeśli nie istnieją w ostatnich tweetach
    tweets['is_new'] = tweets['Tweet_Link'].apply(
        lambda x: x not in last_tweets['Tweet_Link'].values if not last_tweets.empty else True
    )

    # Dodaj komentarze tylko do nowych tweetów
    new_tweets_with_comments = add_comments_to_df(tweets[tweets['is_new']])

    # Połącz stare i nowe tweety z komentarzami
    all_tweets_with_comments = pd.merge(
        tweets,
        new_tweets_with_comments[['Tweet_Link', 'Comment']],
        on='Tweet_Link',
        how='left'
    )

    # Zapisz połączone tweety z komentarzami do pliku CSV
    all_tweets_with_comments.to_csv('last_tweets.csv', index=False)

    # Renderuj szablon HTML z tweetami i komentarzami
    return render_template('dashboard.html', tweets=all_tweets_with_comments)


if __name__ == '__main__':
    app.run(debug=True)
