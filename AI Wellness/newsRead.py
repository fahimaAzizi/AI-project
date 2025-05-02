import requests 
import json
import pyttsx3



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def latestnews():
 api_dict = {
    "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=YOUR_API_KEY",
    "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=YOUR_API_KEY",
    "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=YOUR_API_KEY",
    "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=YOUR_API_KEY",
    "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=YOUR_API_KEY",
    "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=YOUR_API_KEY"
}


def speak(text):
    print(text)

speak("Which field news do you want? Options: [business], [health], [technology], [sports], [entertainment], [science]")


field = input("Type field news that you want: ").strip().lower()


url = api_dict.get(field) # type: ignore

if url:
    speak(f"Fetching news for category: {field}")
    response = requests.get(url)
    
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])

        if articles:
            speak("Here is the first news:")
            print("Title:", articles[0].get("title"))
            print("Description:", articles[0].get("description"))
            print("URL:", articles[0].get("url"))
        else:
            speak("No news articles found in this category.")
    else:
        speak("Failed to fetch news. Please check your API key or try again later.")
else:
    speak("Category not found. Please choose from the listed categories.")