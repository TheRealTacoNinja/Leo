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
        """"""