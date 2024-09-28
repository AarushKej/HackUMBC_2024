import pyautogui as pg

def spotlight(app):
    pg.keyDown('command')
    pg.press('space')
    pg.keyUp('command')
    pg.write(app)    
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