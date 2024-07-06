# commands.py
import datetime
import webbrowser
import os
import requests
from PIL import ImageGrab
from utils import log_activity, send_notification
from config import WEATHER_API_KEY

# Function to tell the current time
def tell_time():
    now = datetime.datetime.now()
    response = f"The current time is {now.strftime('%H:%M')}"
    log_activity("Told time: " + response)
    return response

# Function to take a screenshot
def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshots/screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    log_activity("Took screenshot")
    return "Screenshot taken"

# Function to open YouTube and search for a video
def open_youtube(search_query):
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)
    log_activity(f"Searched YouTube for {search_query}")
    return f"Opening YouTube and searching for {search_query}"

# Function to shut down the laptop
def shutdown():
    log_activity("Shutdown initiated")
    os.system("shutdown /s /t 1")  # Windows
    # os.system("shutdown -h now")  # Linux
    # os.system("sudo shutdown -h now")  # macOS
    return "Shutting down the laptop"

# Function to set a reminder
def set_reminder(reminder_text, time_delta):
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=time_delta)
    response = f"Reminder set for {reminder_time.strftime('%H:%M')}: {reminder_text}"
    log_activity("Set reminder: " + response)
    # Simulate sending a notification
    send_notification("Reminder", reminder_text)
    return response

# Function to take a note
def take_note(note_text):
    with open('notes.txt', 'a') as file:
        file.write(note_text + "\n")
    log_activity("Saved note: " + note_text)
    return "Note saved"

# Function to check the weather
def check_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        response = f"The current weather in {location} is {weather_description} with a temperature of {temperature}°C."
    else:
        response = "I couldn't fetch the weather information. Please try again."
    log_activity("Checked weather: " + response)
    return response

# Function to play music (using a default music player)
def play_music(song_name):
    webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
    log_activity("Playing music: " + song_name)
    return f"Playing {song_name} on YouTube."
