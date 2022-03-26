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
        Exception as e:
        print(e)
        return False
