
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
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
            print("Sorry, I didn't catch that.")
            return "None"
    return query
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)



def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def sreachGoogle(query):
     if "google" in query:
        import wikipedia as googleScrap
        query= query.replace("jarvis","")
        query= query.replace("Google sreach","")
        query= query.replace("google ","")
        query= query.replace("youtube","")
        speak("this is what i found on google")

        try:
           pywhatkit.search(query)
           result =googleScrap.summary(query,1)
           speak(result)
        
        except:
             speak("No speakable output available")
          
def        


