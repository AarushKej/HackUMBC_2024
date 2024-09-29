import pyautogui as pg
import os
from gtts import gTTS

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    #os.system("start output.mp3")  # For Windows
    # os.system("mpg321 output.mp3")  # For Linux
    os.system("afplay output.mp3")

def ask(questions):
    text_to_speech(str(questions))

def openApp(app):
    print("OPEN")
    pg.keyDown('command')
    pg.press('space')
    pg.keyUp('command')
    pg.write(str(app))    
    pg.press('enter')

def opentab():
    pg.keyDown('command')

    pg.press('t')
    pg.keyUp('command')
    
def closetab():
    pg.keyDown('command')
    pg.press('w')
    pg.keyUp('command')

def search(words):
    pg.write(words)  
    pg.press('enter')
    
# openApp("Google Chrome")