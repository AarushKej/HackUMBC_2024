import numpy as np
import cv2
from PIL import ImageGrab

while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,10,2650,1080)))

    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break