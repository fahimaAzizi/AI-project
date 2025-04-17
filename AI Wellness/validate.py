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

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
print(voices[0])
