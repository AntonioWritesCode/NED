"""
=================================================
||           NED v1.0                          ||
||      Not Entirely Dumb                      ||
||      Created by Toni & Cozi                 ||
=================================================
"""

# This is a simple Python script for the NED (Not Entirely Dumb) project.
# It is designed to be a simple, easy-to-use tool for basic tasks.
BOT_NAME = "NED"

import time
from datetime import datetime

BOT_NAME = "NED"

def speak(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

print("=" * 50)
print(f"Initializing {BOT_NAME} Systems...")
time.sleep(1)

print("Loading voice interface...")
time.sleep(0.7)

print("Loading memory...")
time.sleep(0.7)

print("Connecting modules...")
time.sleep(0.7)

print("System Online.\n")

current_time = datetime.now().strftime("%I:%M %p")

speak(f"Good day. I am {BOT_NAME}.")
speak(f"The current time is {current_time}.")
speak("All systems are operational.")
speak("How may I assist you today?")

user_input = input("Input: ")

# NED Response
print("Thanks for your input!")

# Process User Input
print(f"You entered: {user_input}")

# Run the script
while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["quit", "exit", "shutdown"]:
        speak("Understood. Shutting down systems.")
        break

    elif "hello" in user_input.lower():
        speak("Hello. It's good to see you again.")

    elif "time" in user_input.lower():
        speak(f"It is currently {datetime.now().strftime('%I:%M %p')}.")

    elif "status" in user_input.lower():
        speak("All systems are functioning within normal parameters.")

    else:
        speak("I'm still learning. I recorded your request for future upgrades.")


import random

acknowledgements = [
    "Certainly.",
    "Right away.",
    "Of course.",
    "As you wish.",
    "Understood.",
    "Working on it.",
    "Immediately."
]

def acknowledge():
    speak(random.choice(acknowledgements))