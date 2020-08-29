import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

speechEngine = pyttsx3.init('sapi5')
voices = speechEngine.getProperty('voices')
speechEngine.setProperty('voice', voices[1].id)


def speak(audio):
    speechEngine.say(audio)
    speechEngine.runAndWait()


def initial_response():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, Arnav!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon, Arnav!")

    else:
        speak("Good Evening, Arnav!")

    speak("How can I help you?")


def user_response():
    res = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        res.pause_threshold = 1
        audio = res.listen(source)

    try:
        print("Recognizing...")
        query = res.recognize_google(audio, language='en-in')
        print(f"Arnav: {query}\n")

    except Exception as e:
        # print(e)
        print("Couldn't understand..")
        speak("Sorry, could you please repeat that?")
        return "None"

    return query


if __name__ == '__main__':
    initial_response()
    while True:
        query = user_response().lower()

        if 'open google' in query:
            # google.com
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            # youtube.com
            webbrowser.open("youtube.com")

        elif 'open whatsapp' in query:
            # web.whatsapp.com
            webbrowser.open("web.whatsapp.com")

        elif 'wikipedia' in query:
            # search on wikipedia
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia,")
            print(results)
            speak(results)

        elif 'the time' in query:
            # return time
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Time: {time}")
            speak(f"Current time is {time}")

        elif 'open vs code' in query:
            # open vs code
            path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open pycharm' in query:
            # open pycharm
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'open edge' in query:
            # open edge chromium
            path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(path)

        elif 'open chrome' in query:
            # open chrome
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        elif 'open spotify' or 'play music' in query:
            #open spotify
            path = "C:\\Users\\Dell\\AppData\\Roaming\\Spotify\\Spotify.exe"
