from builtins import EncodingWarning
from cgitb import text
import pyttsx3
from decouple import config
USERNAME = config('USER')
BOTNAME = config('BOTNAME')
engine = pyttsx3.init('sapi5')
# Set Rate
engine.setProperty('rate', 190)
# Set Volume
engine.setProperty('volume', 1.0) 
# Set Voice (Male)
voices = engine.getproperty('voices')
engine.getproperty('voice', voices[1].id)
# Text to Speech Conversation
def speak(text):
    """Used to speak what ever is passed to it"""
engine.say(text)
engine.runAndWait()
from datetime import datetime
def greet_user():
    """Greets the user according to the time"""
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon{USERNAME}")
    elif(hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"hi I am {BOTNAME}. How may assist you")
import speech_recognition as sr
from random import choice
from utils import opening_text
def take_user_imput():
            """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Listening....')
    r.pause_threshold = 1
    audio = r.listen(source)

    print('Recognizing...')
    query = r.recognize_google(audio, language=' en-in')
if not 'exit' in query or 'stop' in query:
    speak(choice(opening_title))
else:
    hour = datetime.now().hour
    if hour >= 21 and hour < 6:
        speak("good night sir, take care!")
    else:
        speak('have a good day sir')
    exit()
    speak('Sorry, I could not understand. could you please say that again?')
    query = 'None'
    query
opening_text = [
   "cool i am on it sir.",
   "Okay sir, I'm working on it.",
    "Just a second sir.",
]
import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
def open_notepad():
    os.startfile(paths['notepad'])
def open_discord():
    os.startfile(paths['discord'])
def open_cmd():
    os.system('start cmd')
def open_calculator():
    sp.Popen(paths['calculator'])
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
{
    "ip": "117.214.111.199"
}
def find_my_ip():
    ip_address = request.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results
def play_on_youtube(video):
    kit.playonyt(video)
def search_on_google(query):
    kit.search(query)
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
def send_email(receiver_address, subject, message):
        email = EmailMessange()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['Form'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
        print(e)
        return False
NEWS_API_KEY = config("NEWS_API_KEY")


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
{
  "status": "ok",
  "totalResults": 38,
  "articles": [
    {
      "source": {
        "id": null,
        "name": "Sportskeeda"
      },
      "author": "Aniket Thakkar",
      "title": "Latest Free Fire redeem code to get Weapon loot crate today (14 October 2021) - Sportskeeda",
      "description": "Gun crates are one of the ways that players in Free Fire can obtain impressive and appealing gun skins.",
      "url": "https://www.sportskeeda.com/free-fire/latest-free-fire-redeem-code-get-weapon-loot-crate-today-14-october-2021",
      "urlToImage": "https://staticg.sportskeeda.com/editor/2021/10/d0b83-16341799119781-1920.jpg",
      "publishedAt": "2021-10-14T03:51:50Z",
      "content": null
    },
    {
      "source": {
        "id": null,
        "name": "NDTV News"
      },
      "author": null,
      "title": "BSF Gets Increased Powers In 3 Border States: What It Means - NDTV",
      "description": "Border Security Force (BSF) officers will now have the power toarrest, search, and of seizure to the extent of 50 km inside three newstates sharing international boundaries with Pakistan and Bangladesh.",
      "url": "https://www.ndtv.com/india-news/bsf-gets-increased-powers-in-3-border-states-what-it-means-2574644",
      "urlToImage": "https://c.ndtvimg.com/2021-08/eglno7qk_-bsf-recruitment-2021_625x300_10_August_21.jpg",
      "publishedAt": "2021-10-14T03:44:00Z",
      "content": "This move is quickly snowballing into a debate on state autonomy. New Delhi: Border Security Force (BSF) officers will now have the power to arrest, search, and of seizure to the extent of 50 km ins… [+4143 chars]"
    },
    {
      "source": {
        "id": "the-times-of-india",
        "name": "The Times of India"
      },
      "author": "TIMESOFINDIA.COM",
      "title": "5 health conditions that can make your joints hurt - Times of India",
      "description": "Joint pain caused by these everyday issues generally goes away on its own when you stretch yourself a little and flex your muscles.",
      "url": "https://timesofindia.indiatimes.com/life-style/health-fitness/health-news/5-health-conditions-that-can-make-your-joints-hurt/photostory/86994969.cms",
      "urlToImage": "https://static.toiimg.com/photo/86995017.cms",
      "publishedAt": "2021-10-14T03:30:00Z",
      "content": "Depression is a mental health condition, but the symptoms may manifest even on your physical health. Unexpected aches and pain in the joints that you may experience when suffering from chronic depres… [+373 chars]"
    },
    {
      "source": {
        "id": null,
        "name": "The Indian Express"
      },
      "author": "Devendra Pandey",
      "title": "Rahul Dravid likely to be interim coach for New Zealand series - The Indian Express",
      "description": "It’s learnt that a few Australian coaches expressed interest in the job, but the BCCI isn’t keen as they are focussing on an Indian for the role, before they look elsewhere.",
      "url": "https://indianexpress.com/article/sports/cricket/rahul-dravid-likely-to-be-interim-coach-for-new-zealand-series-7570990/",
      "urlToImage": "https://images.indianexpress.com/2021/05/rahul-dravid.jpg",
      "publishedAt": "2021-10-14T03:26:09Z",
      "content": "Rahul Dravid is likely to be approached by the Indian cricket board to be the interim coach for Indias home series against New Zealand. Head coach Ravi Shastri and the core of the support staff will … [+1972 chars]"
    },
    {
      "source": {
        "id": null,
        "name": "CNBCTV18"
      },
      "author": null,
      "title": "Thursday's top brokerage calls: Infosys, Wipro and more - CNBCTV18",
      "description": "Goldman Sachs has maintained its 'sell' rating on Mindtree largely due to expensive valuations, while UBS expects a muted reaction from Wipro's stock. Here are the top brokerage calls for the day:",
      "url": "https://www.cnbctv18.com/market/stocks/thursdays-top-brokerage-calls-infosys-wipro-and-more-11101072.htm",
      "urlToImage": "https://images.cnbctv18.com/wp-content/uploads/2019/03/buy-sell.jpg",
      "publishedAt": "2021-10-14T03:26:03Z",
      "content": "MiniGoldman Sachs has maintained its 'sell' rating on Mindtree largely due to expensive valuations, while UBS expects a muted reaction from Wipro's stock. Here are the top brokerage calls for the day:"
    }
  ]
}
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"
    {
    "coord": {
        "lon": 85,
        "lat": 24.7833
    },
    "weather": [
        {
            "id": 721,
            "main": "Haze",
            "description": "haze",
            "icon": "50d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 26.95,
        "feels_like": 26.64,
        "temp_min": 26.95,
        "temp_max": 26.95,
        "pressure": 1011,
        "humidity": 36
    },
    "visibility": 3000,
    "wind": {
        "speed": 2.57,
        "deg": 310
    },
    "clouds": {
        "all": 57
    },
    "dt": 1637227634,
    "sys": {
        "type": 1,
        "id": 9115,
        "country": "IN",
        "sunrise": 1637195904,
        "sunset": 1637235130
    },
    "timezone": 19800,
    "id": 1271439,
    "name": "Gaya",
    "cod": 200
}
TMDB_API_KEY = config("TMDB_API_KEY")


def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]
    {
  "page": 1,
  "results": [
    {
      "video": false,
      "vote_average": 7.9,
      "overview": "Shang-Chi must confront the past he thought he left behind when he is drawn into the web of the mysterious Ten Rings organization.",
      "release_date": "2021-09-01",
      "title": "Shang-Chi and the Legend of the Ten Rings",
      "adult": false,
      "backdrop_path": "/cinER0ESG0eJ49kXlExM0MEWGxW.jpg",
      "vote_count": 2917,
      "genre_ids": [28, 12, 14],
      "id": 566525,
      "original_language": "en",
      "original_title": "Shang-Chi and the Legend of the Ten Rings",
      "poster_path": "/1BIoJGKbXjdFDAqUEiA2VHqkK1Z.jpg",
      "popularity": 9559.446,
      "media_type": "movie"
    },
    {
      "adult": false,
      "backdrop_path": "/dK12GIdhGP6NPGFssK2Fh265jyr.jpg",
      "genre_ids": [28, 35, 80, 53],
      "id": 512195,
      "original_language": "en",
      "original_title": "Red Notice",
      "overview": "An Interpol-issued Red Notice is a global alert to hunt and capture the world's most wanted. But when a daring heist brings together the FBI's top profiler and two rival criminals, there's no telling what will happen.",
      "poster_path": "/wdE6ewaKZHr62bLqCn7A2DiGShm.jpg",
      "release_date": "2021-11-04",
      "title": "Red Notice",
      "video": false,
      "vote_average": 6.9,
      "vote_count": 832,
      "popularity": 1990.503,
      "media_type": "movie"
    },
    {
      "genre_ids": [12, 28, 53],
      "original_language": "en",
      "original_title": "No Time to Die",
      "poster_path": "/iUgygt3fscRoKWCV1d0C7FbM9TP.jpg",
      "video": false,
      "vote_average": 7.6,
      "overview": "Bond has left active service and is enjoying a tranquil life in Jamaica. His peace is short-lived when his old friend Felix Leiter from the CIA turns up asking for help. The mission to rescue a kidnapped scientist turns out to be far more treacherous than expected, leading Bond onto the trail of a mysterious villain armed with dangerous new technology.",
      "id": 370172,
      "vote_count": 1804,
      "title": "No Time to Die",
      "adult": false,
      "backdrop_path": "/1953j0QEbtN17WFFTnJHIm6bn6I.jpg",
      "release_date": "2021-09-29",
      "popularity": 4639.439,
      "media_type": "movie"
    },
    {
      "poster_path": "/5pVJ9SuuO72IgN6i9kMwQwnhGHG.jpg",
      "video": false,
      "vote_average": 0,
      "overview": "Peter Parker is unmasked and no longer able to separate his normal life from the high-stakes of being a Super Hero. When he asks for help from Doctor Strange the stakes become even more dangerous, forcing him to discover what it truly means to be Spider-Man.",
      "release_date": "2021-12-15",
      "id": 634649,
      "adult": false,
      "backdrop_path": "/vK18znei8Uha2z7ZhZtBa40HIrm.jpg",
      "vote_count": 0,
      "genre_ids": [28, 12, 878],
      "title": "Spider-Man: No Way Home",
      "original_language": "en",
      "original_title": "Spider-Man: No Way Home",
      "popularity": 1084.815,
      "media_type": "movie"
    },
    {
      "video": false,
      "vote_average": 6.8,
      "overview": "After finding a host body in investigative reporter Eddie Brock, the alien symbiote must face a new enemy, Carnage, the alter ego of serial killer Cletus Kasady.",
      "release_date": "2021-09-30",
      "adult": false,
      "backdrop_path": "/70nxSw3mFBsGmtkvcs91PbjerwD.jpg",
      "vote_count": 1950,
      "genre_ids": [878, 28, 12],
      "id": 580489,
      "original_language": "en",
      "original_title": "Venom: Let There Be Carnage",
      "poster_path": "/rjkmN1dniUHVYAtwuV3Tji7FsDO.jpg",
      "title": "Venom: Let There Be Carnage",
      "popularity": 4527.568,
      "media_type": "movie"
    }
  ],
  "total_pages": 1000,
  "total_results": 20000
}
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
    def get_random_advice():
        res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from pprint import pprint


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
