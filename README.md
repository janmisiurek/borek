# B.O.R.E.K. 
## _Bot Odwzorowujący Reakcje Elokwentnego Komentatora_

**Wymagania:**
- Python 3.6+
- Flask
- Selenium
- python-dotenv

**Instalacja:**
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


Utwórz folder drivers i umieść tam sterownik przeglądarki Selenium (taki jak chromedriver) musi być odpowiedni dla używanej przeglądarki i wersji systemu operacyjnego.

Utwórz plik .env w głównym katalogu aplikacji:
```sh
EMAIL=
TWITTER_USERNAME=
TWITTER_PASSWORD=
OPENAI_API_KEY=
TWITTER_LIST_URL=
```

**Uruchom aplikację:**
```sh
python app.py
```
