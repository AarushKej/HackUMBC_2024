import numpy as np
import cv2
from PIL import ImageGrab
x=1
while(x==1):
    x +=1
    screen = np.array(ImageGrab.grab(bbox=(0,40,2560,1664)))

while(True):  
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break