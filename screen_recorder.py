import numpy as np
import cv2
from PIL import ImageGrab
from PIL import Image
import time

time.sleep(3)
screen = np.array(ImageGrab.grab(bbox=(0,40,2560,1664)))
im = Image.fromarray(screen)
im.convert('RGB')
im.save("screen.png")
print("captured")

