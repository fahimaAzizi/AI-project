from asyncio import sleep
import os
import pyautogui
import webbrowser
import pyttsx3


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voice")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp ={"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak("Lunching,sie")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replce("open" ,"")
        query = query.replce("jarvis" ,"")
        query = query.replce("launch" ,"")
        query = query.replce(" " ,"")
        webbrowser.open(f"httpa://www.{query}")
    else:
        keys =list(dictapp.keys())  
        for app in keys :
            if app in query :
                os.system(f"satart{dictapp[app]}")
def closeappweb(query):
    speak("closing,sir")
    if "one tab" in query or"1 tab" in query:
        pyautogui.hotke("ctrl","w")
    elif "2 tab " in query:
        pyautogui.hotkey("ctel","w")   
        sleep(0.5)
        pyautogui.hotkey("ctel","w")    
        sleep(0.5)
    elif "3 tab " in query:
        pyautogui.hotkey("ctel","w") 
        sleep(0.5)   
        pyautogui.hotkey("ctel","w")    
        sleep(0.5)  
        pyautogui.hotkey("ctel","w") 
        speak("All tabs closed")
    elif "4 tab " in query:
        pyautogui.hotkey("ctel","w")    
        sleep(0.5)
        pyautogui.hotkey("ctel","w")    
        sleep(0.5)
        pyautogui.hotkey("ctel","w")    
        sleep(0.5) 
        speak("All tabs closed")
    elif "5 tab " in query:
        pyautogui.hotkey("ctel","w")    
        sleep(0.5)
        pyautogui.hotkey("ctel","w")    
        sleep(0.5)
        pyautogui.hotkey("ctel","w")    
        sleep(0.5)
        pyautogui.hotkey("ctel","w")    
        sleep(0.5)
        speak("All tabs closed")
    else:
        keys = list(dictapp.keys())