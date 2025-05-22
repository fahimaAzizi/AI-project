from time import sleep
from googletrans import Translator
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition as sr
from playsound import playsound
import os
import time

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

# Translation and speaking logic
print(googletrans.LANGUAGES)
translator = Translator()
speak("Choose the language in which you want to translate")
b = input("To_Lang : ")
query = takeCommand()

try:
    text_to_translate = translator.translate(query, src='auto', dest=b)
    text = text_to_translate.text
    speakg1 = gTTS(text=text, lang=b, slow=False)
    speakg1.save("voice.mp3")
    playsound("voice.mp3")
    time.sleep(5)
    os.remove("voice.mp3")
except:
    print("Unable to translate")
