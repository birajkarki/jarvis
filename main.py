# main.py
import speech_recognition as sr
import pyttsx3
from commands import tell_time, take_screenshot, open_youtube, shutdown, set_reminder, take_note, check_weather, play_music
from utils import check_password, log_activity
from config import PASSWORD

# Initialize the recognizer and the engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, the service is down.")
            return ""

# Main function to handle commands
def handle_command(command):
    if 'time' in command:
        response = tell_time()
    elif 'screenshot' in command:
        response = take_screenshot()
    elif 'youtube' in command:
        speak("What should I search for?")
        query = listen()
        if query:
            response = open_youtube(query)
        else:
            response = "No query provided"
    elif 'shutdown' in command:
        speak("Please enter the password")
        input_password = input("Enter password: ")
        if check_password(input_password, PASSWORD):
            response = shutdown()
        else:
            response = "Incorrect password. Shutdown aborted."
    elif 'reminder' in command:
        speak("What should the reminder say?")
        reminder_text = listen()
        if reminder_text:
            speak("In how many minutes should I remind you?")
            try:
                time_delta = int(listen())
                response = set_reminder(reminder_text, time_delta)
            except ValueError:
                response = "Invalid time input. Reminder not set."
        else:
            response = "No reminder text provided"
    elif 'note' in command:
        speak("What should the note say?")
        note_text = listen()
        if note_text:
            response = take_note(note_text)
        else:
            response = "No note text provided"
    elif 'weather' in command:
        speak("Which location's weather would you like to know?")
        location = listen()
        if location:
            response = check_weather(location)
        else:
            response = "No location provided"
    elif 'play music' in command:
        speak("What song should I play?")
        song_name = listen()
        if song_name:
            response = play_music(song_name)
        else:
            response = "No song name provided"
    else:
        response = "Command not recognized"
    
    speak(response)
    log_activity(f"Executed command: {command} - {response}")

# Main loop
if __name__ == "__main__":
    speak("Hello, how can I help you today?")
    while True:
        command = listen()
        if command:
            handle_command(command)
