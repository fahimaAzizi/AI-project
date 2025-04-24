# from fastapi import FastAPI
# import json
# from pydantic import BaseModel
# class add(BaseModel):
#     a:int 
#     b: int
# app =FastAPI()

# @app.post("/hello")
# def hello(req: add):  # Fixed 'daf' to 'def'
#     return "helloMr."

import pyttsx3
import speech_recognition as sr  # use 'sr' for shorter reference
import requests
from bs4 import BeautifulSoup  # Fixed typo 'BeautifulSop'
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300

        audio = r.listen(source, 0, 4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if " wake up" in query:
            from greeMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if " go to sleep" in query:
                    speak(" ok sir, you can call me anytime ")
                    break

                elif "hello" in query:
                    speak("hello jee , how can i hellp you")
                elif "what is you neme" in query:
                    speak("nice name ")
                elif "are you okay " in query:
                    speak("not like you")
                elif "thank you " in query:
                    speak("our welcome, jee")
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle()
                elif "youtube" in query:
                    from searchNow import searchyoutube
                    searchyoutube()

                elif "temperatuer" in query:
                    search = "temperatuer in quetta pakistan"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")  # Fixed typo
                    temp = data.find("div", class_="BNeawe").text  # Completed statement
                    speak(f"current {search} is {temp}")

                elif "weather" in query:
                    search = "temperatuer in quetta pakistan"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")  # Fixed typo
                    temp = data.find("div", class_="BNeawe").text  # Completed statement
                    speak(f"current {search} is {temp}")

                elif "the time " in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the time is {strTime}")
                elif "i am done" in query:
                    speak("going to sleep,sir")
                    exit()
