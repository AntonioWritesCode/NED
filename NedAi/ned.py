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
from TTS.api import TTS
import sounddevice as sd
import scipy.io.wavfile as wav
import os
import subprocess


AI_NAME = "Jarvis"


# -------------------------
# XTTS Setup
# -------------------------

print("Loading voice model...")


tts = TTS(
    "tts_models/multilingual/multi-dataset/xtts_v2"
)


VOICE_SAMPLE = "voices/myvoice.wav"



# -------------------------
# Ollama
# -------------------------

chat = [

{
"role":"system",
"content":
"""
You are Jarvis.

Speak calmly and intelligently.
Keep answers concise.
"""
}

]



def ask_ai(text):


    chat.append(
        {
        "role":"user",
        "content":text
        }
    )


    response = ollama.chat(

        model="llama3.1",

        messages=chat

    )


    answer = response["message"]["content"]


    chat.append(

        {
        "role":"assistant",
        "content":answer
        }

    )


    return answer



# -------------------------
# XTTS Voice
# -------------------------


def speak(text):

    print("Jarvis:",text)


    tts.tts_to_file(

        text=text,

        speaker_wav=VOICE_SAMPLE,

        language="en",

        file_path="output/raw.wav"

    )


    play_audio(
        "output/raw.wav"
    )



def play_audio(file):


    os.startfile(file)




# -------------------------
# Main
# -------------------------


speak(
"Systems online. How may I assist you?"
)



while True:


    user = input("\nYou: ")


    if user.lower() == "exit":

        speak(
        "Shutting down."
        )

        break



    response = ask_ai(user)


    speak(response)