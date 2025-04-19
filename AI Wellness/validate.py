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


# Example usage
speak("Hello! How can I help you?")
takeCommand()




 
