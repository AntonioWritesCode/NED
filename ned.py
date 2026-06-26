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

# NED Greeting
print("Hello! I am NED, your friendly assistant. How can I help you today?")

user_input = input("Input: ")

# NED Response
print("Thanks for your input!")

# Process User Input
print(f"You entered: {user_input}")

# Run the script
while True:
    user_input = input("Input: ")

    if user_input == "quit": # Check if the user wants to quit
        print("NED shutting down...")
        break


    