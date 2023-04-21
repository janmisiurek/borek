import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from utilities import login_to_twitter

app = Flask(__name__)

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

    global tweets
    tweets = login_to_twitter()

    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html', tweets=tweets)

if __name__ == '__main__':
    app.run(debug=True)
