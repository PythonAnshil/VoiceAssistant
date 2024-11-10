import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def get_greeting():
    """Get an appropriate greeting based on the current time."""
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    elif 18 <= current_hour < 22:
        return "Good evening"
    else:
        return "Good night"


def listen_for_command():
    """Listen for the trigger phrase 'Hello Baby' and respond accordingly."""
    with sr.Microphone() as source:
        print("Listening for 'Hello Baby'...")

        # Adjust settings to improve recognition accuracy
        recognizer.energy_threshold = 3000  # Adjust based on your environment
        recognizer.pause_threshold = 1  # Increase if speech is cut off

        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized command: {command}")  # Debug output
            if "hello baby" in command:
                greeting = get_greeting()
                speak(f"Hey Anshil, {greeting}")
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
        except sr.RequestError:
            print("Sorry, the speech service is unavailable.")


# Main loop to keep listening for the command
while True:
    listen_for_command()