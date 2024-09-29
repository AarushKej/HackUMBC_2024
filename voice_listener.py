import speech_recognition as sr
import pygame
from gtts import gTTS
import os
from geminiAPI import doShit
from screen_recorder import ss
import subprocess
pygame.init()


def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    #os.system("start output.mp3")  # For Windows
    # os.system("mpg321 output.mp3")  # For Linux
    os.system("afplay output.mp3")

def send_mac_notification(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])

def listen_for_keyword():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        print("Listening for the keyword 'Alexa'...")

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source,0,4)

            try:
                speech_text = recognizer.recognize_google(audio).lower()
                print(f"You said: {speech_text}")

                if "friday" or "Friday" in speech_text:
                    print("Keyword 'jarvis' detected! Playing sound...")
                    send_mac_notification("FRIDAY", "at your")
                    pygame.mixer.music.load("JARVIS_Awake.wav")
                    pygame.mixer.music.play()
                    text_to_speech("executing now")
                    ss()
                    doShit(speech_text)
            except sr.UnknownValueError:
                print("Could not understand the audio.")
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")

def listen_for_command(recognizer, microphone):
    recognizer.adjust_for_ambient_noise(microphone)
    audio = recognizer.listen(microphone)
    print("Listening for the command...")
    pygame.mixer.music.load("JARVIS_Awake.wav")
    pygame.mixer.music.play()
    text_to_speech("talk now")
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command received: {command}")
        print(command)
        doShit(command)
        print(f"Executing command: {command}")

    except sr.UnknownValueError:
        print("Could not understand the command.")
        text_to_speech("try again")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")


listen_for_keyword()