import pyttsx3
import speech_recognition as sr
#import pywhatkit
#import yfinance as yf
#import pyjokes
#import webbrowser
#import datetime
#import wikipedia

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

# voice options / language
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

speak('Hello Gabriel I hope you will have a great day')