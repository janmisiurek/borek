# B.O.R.E.K. 
## _Bot Odwzorowujący Reakcje Elokwentnego Komentatora_

**Requirements:**
- Python 3.6+
- Flask
- Selenium
- python-dotenv

**Installation:**
```sh
git clone https://github.com/janmisiurek/borek.git
```

```sh
cd your-app
```

```sh
python -m venv venv
```

```sh
source venv/bin/activate  # Linux/macOS
```

```sh
venv\Scripts\activate  # Windows
```


Create a drivers folder and put there the Selenium browser driver (such as chromedriver) must be appropriate for the browser you are using and the version of your operating system.
33

34
Create an .env file in the root directory of the applicationCreate a drivers folder and put there the Selenium browser driver (such as chromedriver) must be appropriate for the browser you are using and the version of your operating system.

33

34

Create an .env file in the root directory of the application:
```sh
EMAIL=
TWITTER_USERNAME=
TWITTER_PASSWORD=
OPENAI_API_KEY=
TWITTER_LIST_URL=
```

**Launch the application:**
```sh
python app.py
```
