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


import os
import winsound

# ... imports ...

from TTS.api import TTS

tts = TTS(
    "tts_models/multilingual/multi-dataset/xtts_v2"
)

VOICE_SAMPLE = "voices/myvoice.wav"


def speak(text):

    print("Jarvis:", text)

    os.makedirs("output", exist_ok=True)

    output_file = os.path.abspath("output/raw.wav")

    tts.tts_to_file(
        text=text,
        speaker_wav=VOICE_SAMPLE,
        language="en",
        file_path=output_file
    )

    if os.path.exists(output_file):
        play_audio(output_file)
    else:
        print("raw.wav was not created")


def play_audio(file):

    try:
        winsound.PlaySound(
            file,
            winsound.SND_FILENAME
        )

    except Exception as e:
        print(e)





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

