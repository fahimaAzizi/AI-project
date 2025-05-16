import pyttsx3
import speech_recognition as sr
import random

# Initialize TTS engine
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
        audio = r.listen(source, timeout=4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return "none"
    return query.lower()

def game_play():
    speak("Let's play Rock Paper Scissors!")
    print("Let's play Rock Paper Scissors!")
    
    me_score = 0
    computer_score = 0
    rounds = 5

    options = ["rock", "paper", "scissors"]

    for i in range(rounds):
        speak(f"Round {i+1}")
        print(f"\n--- Round {i+1} ---")
        speak("Your turn, say rock, paper, or scissors.")
        user_choice = takeCommand()

        if user_choice not in options:
            speak("Invalid choice. Please say rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        speak(f"I chose {computer_choice}")
        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {user_choice}")

        # Determine winner
        if user_choice == computer_choice:
            speak("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            me_score += 1
            speak("You win this round!")
        else:
            computer_score += 1
            speak("I win this round!")

        print(f"Score -> You: {me_score} | Computer: {computer_score}")

    # Final result
    speak("Game over!")
    if me_score > computer_score:
        speak(f"You won the game by {me_score} to {computer_score}!")
    elif me_score < computer_score:
        speak(f"I won the game by {computer_score} to {me_score}!")
    else:
        speak("It's a draw!")

# To run the game
game_play()
