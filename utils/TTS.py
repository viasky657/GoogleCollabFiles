import os
import torch
import requests
import urllib.parse
import elevenlabs
import ffmpeg

#set the Elevenlabs API Key. 
import getpass

def get_api_key():
    # Prompt the user to enter their API key without showing it on the screen
    api_key = getpass.getpass('Enter your API key: ')
    return api_key

# Now you can use the API key in your code securely
api_key = get_api_key()
print("API key securely entered!")
# Proceed with using the api_key for your API requests or other tasks

elevenlabs.set_api_key(api_key)

def generate_subtitle(chat_now, result_id): #Generate Subtitles in OBS code moved here from subtitles.py file. 
     # output.txt will be used to display the subtitle on OBS
    try:
        write_to_file("output.txt", result_id)
    except Exception as e:
        print(f"Error writing to output.txt: {e}")

     # chat.txt will be used to display the chat/question on OBS
    try:
        write_to_file("chat.txt", chat_now)
    except Exception as e:
        print(f"Error writing to chat.txt: {e}")

def write_to_file(filename, text): 
    words = text.split()
    lines = [" ".join(words[i:i+10]) for i in range(0, len(words), 10)]
    with open(filename, "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(lines))

def elevenlabs_tts(text, voice_id):
    # Generate and play voice audio
    audio = elevenlabs.generate(text=text, voice=voice_id)
    elevenlabs.play(audio)
    return text

def get_Voice_ID():
    # Prompt the user to enter their API key without showing it on the screen
    VoiceID = getpass.getpass('Enter your Elevenlabs Voice ID: ')
    return VoiceID

# Now you can use the API key in your code securely
VoiceID = get_Voice_ID()
print("VoiceID entered!")
# Proceed with using the api_key for your API requests or other tasks

elevenlabs.set_api_key(api_key)

# Example usage
chat_text = "output.txt"
result_text = "output.txt"

generated_text = elevenlabs_tts(result_text, voice_id)
generate_subtitle(chat_text, generated_text)
