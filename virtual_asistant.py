import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# voice options / language
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# listen to our microphone and return the audio as text
def transform_audio_to_text():
    # store recognizer in variable
    r = sr.Recognizer()
    # microphone configuration

# function so that the assistant can be heard
def speak(message):

    # start the engine of pyttsx3
    engine = pyttsx3.init()

    # deliver message
    engine.say(message)
    engine.runAndWait()
    engine.setProperty('voice', id2)

# notify day of week
def ask_day():

    # create variable whit today dates
    day = datetime.date.today()
    print(day)

    # create variable for the day of week
    day_week = day.weekday()
    print(day_week)

    # dictionary of day names
    calendar = {0: 'Monday',
                  1: 'Tuesday',
                  2: 'Wednesday',
                  3: 'Thursday',
                  4: 'Friday',
                  5: 'Saturday',
                  6: 'Sunday'}

    # say the day of the week
    speak(f'Today is {calendar[day_week]}')

# informar que hora es
def ask_hour():

    # create a variable whit hour's date
    hourx = datetime.datetime.now()
    hourx = f'In this moment it is {hourx.hour} whit {hourx.minute} minutes and {hourx.second} seconds'
    print(hourx)

    # say hour
    speak(hourx)

# function initial greeting
def inicial_greeting():

    # create variable with time data
    hourz = datetime.datetime.now()
    if hourz.hour < 6 or hourz.hour > 20:
        time = 'Good evening'
    elif 6 <= hourz.hour < 13:
        time = 'Good morning'
    else:
        time = 'Good afternoon'

    # say hello
    speak(f'{time}, I am Helena, your personal assistant. Please tell me how I can help you')

inicial_greeting()
#ask_hour()
