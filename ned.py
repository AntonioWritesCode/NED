"""
=================================================
||           NED v1.0                          ||
||      Not Entirely Dumb                      ||
||      Created by Toni & Cozi                 ||
=================================================
"""

# This is a simple Python script for the NED (Not Entirely Dumb) project.
# It is designed to be a simple, easy-to-use tool for basic tasks.


import ollama
import json
import os
import datetime

AI_NAME = "NED"
MODEL = "llama3.1"

MEMORY_FILE = "memory.json"


# Load memory
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    return {
        "user": "Jason",
        "facts": []
    }


# Save memory
def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


memory = load_memory()


# System personality
system_prompt = f"""
You are {AI_NAME}, a personal AI assistant.

You are helpful, intelligent, and conversational.

User name:
{memory['user']}

Remember these facts:
{memory['facts']}

Current date:
{datetime.datetime.now()}
"""


chat_history = [
    {
        "role": "system",
        "content": system_prompt
    }
]


print(f"{AI_NAME}: Online. How can I help you?")


while True:

    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit", "shutdown"]:
        print(f"{AI_NAME}: Shutting down.")
        break


    # Memory command
    if user_input.lower().startswith("remember"):

        fact = user_input.replace("remember", "").strip()

        memory["facts"].append(fact)

        save_memory(memory)

        print(f"{AI_NAME}: I'll remember that.")

        continue



    chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    response = ollama.chat(
        model=MODEL,
        messages=chat_history
    )


    answer = response["message"]["content"]


    print(f"\n{AI_NAME}: {answer}")


    chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )