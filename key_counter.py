from pynput import keyboard
import datetime
import os
import json

# File to store counts
LOG_FILE = "key_counts.json"

# Load existing counts if available
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r') as f:
        key_counts = json.load(f)
else:
    key_counts = {}

def save_counts():
    with open(LOG_FILE, 'w') as f:
        json.dump(key_counts, f)

def on_press(key):
    try:
        key_char = key.char  # Get character pressed
    except AttributeError:
        key_char = str(key)  # Handle special keys (shift, ctrl, etc.)

    date = datetime.datetime.now().strftime("%Y-%m-%d")  # Get today's date
    year = datetime.datetime.now().year
    month = datetime.datetime.now().strftime("%Y-%m")

    # Initialize date, month, and year logs if not present
    if date not in key_counts:
        key_counts[date] = {}
    if month not in key_counts:
        key_counts[month] = {}
    if year not in key_counts:
        key_counts[year] = {}

    # Increment the key count for date
    key_counts[date][key_char] = key_counts[date].get(key_char, 0) + 1
    # Increment the key count for month
    key_counts[month][key_char] = key_counts[month].get(key_char, 0) + 1
    # Increment the key count for year
    key_counts[year][key_char] = key_counts[year].get(key_char, 0) + 1

    # Save the updated counts
    save_counts()

# Use a keyboard listener to track key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
