import speech_recognition as sr
import pygame
from gtts import gTTS
import os
from geminiAPI import doShit
from screen_recorder import ss

pygame.init()


def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    #os.system("start output.mp3")  # For Windows
    # os.system("mpg321 output.mp3")  # For Linux
    os.system("afplay output.mp3")

def listen_for_keyword():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        print("Listening for the keyword 'Alexa'...")

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                speech_text = recognizer.recognize_google(audio).lower()
                print(f"You said: {speech_text}")

                if "alexa" or "alexa" in speech_text:
                    print("Keyword 'jarvis' detected! Playing sound...")
                    ss()
                    pygame.mixer.music.load("JARVIS_Awake.wav")
                    pygame.mixer.music.play()
                    pygame.event.wait()
                    text_to_speech("talk now")
                    listen_for_command()
            except sr.UnknownValueError:
                print("Could not understand the audio.")
                text_to_speech("try agian")
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")

def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("Listening for the command...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command received: {command}")
            print(command)
            doShit(command)
            print(f"Executing command: {command}")

        except sr.UnknownValueError:
            print("Could not understand the command.")
            text_to_speech("try agian")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")


listen_for_keyword()