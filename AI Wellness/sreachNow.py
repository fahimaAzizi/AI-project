
import pyttsx3
import speech_recognition as sr 
import pywhatkit
import wikipedia

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300

        audio = r.listen(source,0,4)