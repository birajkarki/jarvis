# utils.py
from datetime import datetime
import os

# Function to check password
def check_password(input_password, actual_password):
    return input_password == actual_password

# Function to log activity
def log_activity(activity):
    with open('logs/activity_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()} - {activity}\n")

# Function to send a notification (optional, for setting reminders)
def send_notification(title, message):
    if os.name == 'nt':  # Windows
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=10)
    else:
        os.system(f'notify-send "{title}" "{message}"')
