import speech_recognition as sr
import pygame

pygame.init()

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
running = True
activated = False
command = ""
while running: 
    with sr.Microphone() as source:
        if not activated: audio_text = r.listen(source, 3, 2)
        else: audio_text = r.listen(source, 8, 3)
        try:
            query = r.recognize_google(audio_text)
            if (activated):
                command = query
                activated = False
            else: command = ""
            if ('Jarvis' in query or 'jarvis' in query):
                activated = True
                pygame.mixer.music.load("JARVIS_Awake.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
                print("TALK")
        except:
            print("Sorry, I did not get that")

        if command != "": print(command)