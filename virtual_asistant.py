import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# voice options / language
id1 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
id2 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# listen to our microphone and return the audio as text
def transform_audio_to_text():

    # store recognizer in variable
    r = sr.Recognizer()

    # configure the microphone
    with sr.Microphone() as source1:

        # Hold on
        r.pause_threshold = 0.8

        # to inform that the recording has started
        print("you can speak")

        # save what you hear as audio
        audio = r.listen(source1)

        try:
            # search on Google
            order = r.recognize_google(audio, language="en")

            # proof that he was able to enter
            print("You said: " + order)

            # response order
            return order

        # in case you do not understand the audio
        except sr.UnknownValueError:

            # proof that you did not understand the audio
            print("ups, I dont get you")

            # return error
            return "I am still waiting"

        # in case of failure to resolve the order
        except sr.RequestError:

            # proof that it did not understand the audio
            print("ups, no service")

            # return error
            return "I am still waiting"

        # error unexpected
        except:

            # proof that it did not understand the audio
            print("ups, something is wrong")

            # return error
            return "I am still waiting"

# function so that the assistant can be heard
def speak(message):
    # start the engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id2)  # Mueve esta línea aquí
    # deliver message
    engine.say(message)
    engine.runAndWait()

# Inform day of week
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

# inform what time it is
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

# central function of the assistant
def ask_things():
    # activate initial greeting
    inicial_greeting()

    # cut-off variable
    begining = True

    # central loop
    while begining:
        # activate the microphone and save the order in a string
        order1 = transform_audio_to_text().lower()

        if 'open youtube' in order1:
            speak('With pleasure, I am opening YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open navigator' in order1:
            speak('Sure, I am on it')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is today' in order1:
            ask_day()
            continue
        elif 'what time is it' in order1:
            ask_hour()
            continue
        elif 'search in wikipedia' in order1:
            speak('Looking it up on Wikipedia')
            search_term = order1.replace('search in wikipedia', '').strip()

            # Check if search_term is empty
            if not search_term:
                speak("Please provide a term to search on Wikipedia.")
                continue

            wikipedia.set_lang('en')
            try:
                result = wikipedia.summary(search_term, sentences=1)
                speak('Wikipedia says the following:')
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for that. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any page matching that term.")
            except Exception as e:
                speak(f"An error occurred while searching Wikipedia: {e}")
            continue
        elif 'search on the internet' in order1:
            speak('I am working on it right now')
            order = order1.replace('search on the internet', '')
            pywhatkit.search(order1)
            speak('This is what I have found')
            continue
        elif 'reproduce' in order1:
            speak('good idea, I am starting to reproduce it')
            pywhatkit.playonyt(order1)
            continue
        elif 'joke' in order1:
            speak(pyjokes.get_joke('en'))
            continue
        elif 'stock price' in order1:
            stok_shares = order1.replace('stock price', '').strip()
            pocket = {'apple': 'AAPL',
                      'amazon': 'AMZN',
                      'google': 'GOOGL'}
            try:
                share_searched = pocket[stok_shares.lower()]
                share_searched = yf.Ticker(share_searched)
                current_price = share_searched.info['regularMarketPrice']
                speak(f'I found, the price of {stok_shares} is {current_price}')
            except KeyError:
                speak("Sorry, but I couldn't find that stock.")
            except Exception as e:
                speak(f"Sorry, but I could not find the stock price. Error: {e}")
                continue
        elif 'bye' in order1:
            speak('I am going to rest, let me know if you need anything.')
            break


ask_things()