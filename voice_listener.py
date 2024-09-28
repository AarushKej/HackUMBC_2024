import speech_recognition as sr
import pygame
from gtts import gTTS
import os
import gemini
from geminiAPI import doShit
from screen_recorder import ss

pygame.init()

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
running = True
activated = False
command = ""

def text_to_speech(text, language='en'):
    

   
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the audio file
    tts.save("output.mp3")
    
    # Play the audio file
    #os.system("output.mp3")  # For Windows
    # os.system("mpg321 output.mp3")  # For Linux
    os.system("afplay output.mp3")  # For macOS

while running: 
    with sr.Microphone() as source:
        if not activated: audio_text = r.listen(source, 3, 1)
        else: audio_text = r.listen(source, 6, 4)
        try:
            query = r.recognize_google(audio_text)
            if (activated):
                command = query
                activated = False
            else: command = ""
            if ('Alex' in query or 'Alex' in query):
                activated = True
                ss()
                pygame.mixer.music.load("JARVIS_Awake.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
                text_to_speech("talk now")
                print("TALK")
        except:
            text_to_speech("Sorry, I did not get that")
            print("Sorry, I did not get that")

        if command != "": 
            print(command)
            doShit(command)
            command = ""
            activated = False
