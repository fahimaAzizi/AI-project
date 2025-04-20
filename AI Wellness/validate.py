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
        try:
            audio = r.listen(source, timeout=4, phrase_time_limit=4)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network.")
            return ""

# Example usage
speak("Hello! How can I help you?")
takeCommand()




 