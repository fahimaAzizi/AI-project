import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to recognize and repeat speech
def repeat_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source)  # Listen for speech
            text = recognizer.recognize_google(audio)  # Convert speech to text
            print(f"You said: {text}")
            
            # Speak the recognized text
            engine.say(text)
            engine.runAndWait()
            
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            print("Could not connect to the speech recognition service.")

# Run the repeater function in a loop
while True:
    repeat_speech()
