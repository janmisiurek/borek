# Aplikacja Flask do automatycznego komentowania tweetów na Twitterze
Wymagania:

Python 3.6+

Flask

Selenium

python-dotenv

Instalacja:

git clone https://github.com/janmisiurek/borek.git

cd your-app

python -m venv venv

source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

Utwórz folder drivers i umieść tam sterownik przeglądarki Selenium (taki jak chromedriver) musi być odpowiedni dla używanej przeglądarki i wersji systemu operacyjnego.

Utwórz plik .env w głównym katalogu aplikacji:

EMAIL=

TWITTER_USERNAME=

TWITTER_PASSWORD=

OPENAI_API_KEY=

TWITTER_LIST_URL=

Uruchom aplikację:

python app.py



