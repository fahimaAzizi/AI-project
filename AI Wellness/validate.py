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

from signal import alarm
import webbrowser
import pyttsx3
import speech_recognition as sr  # use 'sr' for shorter reference
import requests
from bs4 import BeautifulSoup  # Fixed typo 'BeautifulSop'
import datetime
import pyautogui
import os
import random
from keyboard import volumeup # type: ignore
from pygame import mixer

for i in range(3):
    a = input("inter password to opne javis:-")
    pw_file = open("password.txt","r")
    pw= pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLEAS SPEKAK[WAKE UP ] TO LOAD ME UP")
        break
    elif (1 ==pw):
        exit()
    elif (a !=pw):
        print("try again")


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








############################################
                elif "change passeord" in query:
                    speak("what's the new password")
                    new_pw = input("enter the new passwod\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("cone sir")
                    speak(f"your new password is {new_pw}")
             

                elif "schedule my days" in query:
                    tasks = []
                    speak ("do you want to clear old tasks (pleas speak yes or no)")
                    query =takeCommand().lower()
                    if "yes" in query:
                          file = open("tasks.txt", "w")
                          file.write(" ")
                          file.close()
                          no_tasks = int(input("Enter the no. of tasks :- "))
                          tasks = []
                          for i in range(no_tasks):
                              tasks.append(input("Enter the task :- "))
                              file = open("tasks.txt", "a")
                              file.write(f"{i}. {tasks[i]}\n")
                              file.close()
                    elif "no" in query:
                         no_tasks = int(input("Enter the no. of tasks :- "))
                         tasks = [] 
                         for i in range(no_tasks):
                           tasks.append(input("Enter the task :- "))
                           file = open("tasks.txt", "a")
                           file.write(f"{i}. {tasks[i]}\n")
                           file.close()
                    elif "show my schedule" in query:
                        file = open("tasks.txt", "r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("any music you want.mp3")
                        mixer.music.play()
                        norification.notify( # type: ignore
                             title = " my scheudule :-",
                             message = content,
                             timeout =15

                         )
                    elif " open" in query:
                        query = query.replace("open","")
                        query = query.replace("jarvis","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")

                    elif "internet speed" in query:
                        wifi = speedtest.Speedtest()
                        upload_net = wifi.upload()/1048576
                        download_net =wifi.download()/1048576
                        print("wifi upload speed is ",upload_net)
                        print("wifi download speed is ",download_net)
                        speak(f"wifi upload speed is {upload_net}")
                        speak(f"wifi download speed is {download_net}")
                                   









                elif "hello" in query:
                    speak("hello jee , how can i hellp you")
                elif "what is you neme" in query:
                    speak("nice name ")
                elif "are you okay " in query:
                    speak("not like you")
                elif "thank you " in query:
                    speak("our welcome, jee")
                elif " tired" in query:
                    speak("playing your favourite songs, sir")
                    a = (1,2,3,4)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("AI Wellness/surnames.mp3")  
                
                
                
                
                elif "pause" in query:
                    pyautogui.press("p")
                    speak("video pause")
                elif "play" in query:
                    speak("video play")
                    pyautogui.press("k")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video mute")
                elif "volumw up" in query:
                    pyautogui.press("m")
                    speak("video volume up")
                    from keyboard import volumeup # type: ignore
                    speak("turning volume up sir")
                    volumedown() # type: ignore

                elif " open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif" close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                
                
                
                
                elif  "opne" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                elif "google" in query:
                    from searchNow import searchGoogle # type: ignore
                    searchGoogle()
                elif "youtube" in query:
                    from searchNow import searchyoutube # type: ignore
                    searchyoutube()
                
                elif "calculate" in query:
                    from calculateNumber import wolfRamAIpha
                    from calculateNumber import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                elif "whatsapp" in query:
                    from whatsapp import sendMessage
                    sendMessage




                

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
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("set the time")
                    a = input("please tell the time:-")
                    alarm(a)
                    speak ("Done,sir")
                elif "the time " in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the time is {strTime}")
                elif "i am done" in query:
                    speak("going to sleep,sir")
                    exit()
                elif " remember that " in query:
                    rememberMessage = query.replace("remember that ","")
                    rememberMessage = query.replace("jarvis","")
                    speak("you told me to remember that "+rememberMessage)
                    remember = open("remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                elif " what do you remember" in query:
                    remember= open("remember.txt","r")
                    speak("you told me to  that "+remember.read())
                
                elif "shotdown system" in query:
                    speak("Are you sure you want to shotdown")
                    shutdown = input("Do you want to shutdown your computer?(yes/no)")
                    if shutdown =="yes":
                        os.system("shoutdown /s /t 1")

                    elif shutdown =="no":
                        break
