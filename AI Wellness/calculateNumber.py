import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wolfRamAIpha(query): 
    apikey = "VQRRYV-WJB8UL76UQL"
    requester = wolfRamAIpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results)
        return answer
    except:
        speak("the value s not answerable")

def Calc(query):
    
    Term = str(query)
    Term =Term.replace("jarvis","")
    Term =Term.replace("multiply","")
    Term =Term.replace("plus","")
    Term =Term.replace("minus","")
    Term =Term.replace("divide","")
     
    final = str(Term)
    try:
        result =wolfRamAIpha(final)
        print(f"{result}")
        speak(result)
    except:
        speak("the value is not answerable")
