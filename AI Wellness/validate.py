# from fastapi import FastAPI
# import json
# from pydantic import BaseModel
# class add(BaseModel):
#     a:int 
#     b: int
# app =FastAPI()

# @app.post("/hello")
# daf hello(req: add):
#   return "helloMr."
import pyttsx3
import speech_recognition as sr  # use 'sr' for shorter reference

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

        audio = r.listen(source,0,4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
            print("Sorry, I didn't catch that.")
            return "None"
    return query
if __name__== "__main__":
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






 