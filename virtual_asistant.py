import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia

# voice options / language
id1 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
id2 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# listen to our microphone and return the audio as text
def transform_audio_to_text():
    r = sr.Recognizer()
    r.energy_threshold = 300  # Adjust to suit your environment
    with sr.Microphone() as source1:
        r.pause_threshold = 0.8
        print("you can speak")
        audio = r.listen(source1)

        try:
            order = r.recognize_google(audio, language="en")
            print(f"You said: {order}")
            return order
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please speak again.")
            return None
        except sr.RequestError:
            speak("Network issue. Please check your connection.")
            return None
        except Exception as e:
            speak(f"An unexpected error occurred: {str(e)}")
            return None

# function so that the assistant can be heard
# Initialize the engine globally
engine = pyttsx3.init()
engine.setProperty('voice', id2)

def speak(message):
    engine.say(message)
    engine.runAndWait()

# Inform day of week
def get_current_datetime():
    now = datetime.datetime.now()
    return now

def ask_day():
    today = get_current_datetime().strftime('%A')
    speak(f'Today is {today}')

def ask_hour():
    now = get_current_datetime()
    speak(f'In this moment it is {now.hour} with {now.minute} minutes and {now.second} seconds')

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

def ask_things():
    # Activar saludo inicial
    inicial_greeting()

    # Variable de corte
    begining = True

    # Bucle central
    while begining:
        # Activar el micrófono y guardar la orden en una cadena
        order1 = transform_audio_to_text()

        # Verificar si se recibió una orden válida
        if order1:
            order1 = order1.lower()
        else:
            continue  # Volver al inicio del bucle si no se recibió una orden válida

        # Procesar las órdenes recibidas
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

            if not search_term:
                speak("Please provide a term to search on Wikipedia.")
                continue

            wikipedia.set_lang('en')
            try:
                result = wikipedia.summary(search_term, sentences=1)
                speak(f"Wikipedia says: {result}")
            except wikipedia.exceptions.DisambiguationError as e:
                options = e.options[:3]  # Limitar opciones a 3
                speak(f"There are multiple results. Please specify one: {', '.join(options)}")
            except wikipedia.exceptions.PageError:
                speak("No results found.")
            continue
        elif 'search on the internet' in order1:
            speak('I am working on it right now')
            order1 = order1.replace('search on the internet', '')
            pywhatkit.search(order1)
            speak('This is what I have found')
            continue
        elif 'reproduce' in order1:
            speak('Good idea, I am starting to reproduce it')
            pywhatkit.playonyt(order1)
            continue
        elif 'joke' in order1:
            speak(pyjokes.get_joke('en'))
            continue
        elif 'bye' in order1:
            speak('I am going to rest, let me know if you need anything.')
            break
ask_things()