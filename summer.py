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
