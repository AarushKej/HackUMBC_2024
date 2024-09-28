import google.generativeai as genai
import os
import json
import pyautogui as pg
import cv2


def doShit(command):
    api_key = "AIzaSyDj9X15nYR83615JzaRTswdG2LrHZTcfIE"
    genai.configure(api_key=api_key)

    screen_size = pg.size()
    image = cv2.imread("screen.png")
    height, width = image.shape[:2]

    myfile = genai.upload_file("screen.png")
    print(f"{myfile=}")
    model = genai.GenerativeModel("gemini-1.5-flash")
    valid = False
    while not valid:
        try:
            result = model.generate_content(
                [myfile, "\n\n", "From this image of a Mac computer's screen which is of this size" + str((width, height)) + "; perform the task in this command: "+ command +" ; I want you to respond with only a list of the commands and each step should be in a dictionary. For example, if the command was to open the Chrome app, you should return something like this: [{\"action\": \"click\", \"locationX\": \"45%\", \"locationY\": \"98%\"}] ; for actions you can use one of the following: 'click', 'type', 'right-click', 'double-click'. Also ensure that your response has nothing other than the JSON response, I should be able to take your response directly and convert it into a JSON without having to perform any other format modifications. Double check to ensure that the coordinates you give are correct as well, an error would result in the wrong app being opened. Also remember that the origin of the screen is the top left corner. Also ensure that the coordinates are percentages of the total screen size and not pixle values. Ensure coordinates are accurate for clicking the correct icon. Also ensure that there are no redundant or unneeded steps. Also ensure this error does not arise: Expecting value: line 1 column 1 (char 0). Make sure the percentages are between 0 and 100%"]
            )
            actions = json.loads(result.text)
            print(result.text)
            if float(actions[0]['locationX'].split("%")[0]) < 100 and float(actions[0]['locationY'].split("%")[0]) < 100: valid = True
        except: pass
    leftX = 0
    rightX = 0
    topY = 0
    bottomY = 0
    if actions[0]['action'] == "click":
        action = actions[0]
        leftX = ((float(action['locationX'].split("%")[0]) - 12.5) / 100) * width
        rightX = ((float(action['locationX'].split("%")[0]) + 12.5) / 100) * width
        topY = ((float(action['locationY'].split("%")[0]) - 12.5) / 100) * height
        bottomY = ((float(action['locationY'].split("%")[0]) + 12.5) / 100) * height
        if leftX < 0: leftX = 0
        if rightX > width: rightX = width
        if topY < 0: topY = 0
        if bottomY > height: bottomY = height


    # Read the original image

    # Ensure the coordinates are integers

    left = int(leftX)
    right = int(rightX)
    top = int(topY)
    bottom = int(bottomY)

    cropped_image = None

    if left >= right or top >= bottom:
        print("Error: Invalid cropping coordinates")
        print(left, right, top, bottom)
        print(leftX, rightX, topY, bottomY)
    else:
        cropped_image = image[top:bottom, left:right]

    if cropped_image is not None and cropped_image.size > 0:
        cv2.imwrite("cropped_screen.png", cropped_image)
        print("Cropped image saved successfully")
    else:
        print("Error: Cropped image is empty or invalid")

    myfile = genai.upload_file("cropped_screen.png")

    cimage = cv2.imread("cropped_screen.png")
    cheight, cwidth = cimage.shape[:2]

    print(f"{myfile=}")
    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(
        [myfile, "\n\n", "From this image of a section of Mac computer's screen which is of this size " + str((cwidth, cheight)) + "; perform the task in this command: "+ command +"; I want you to respond with only a list of the commands and each step should be in a dictionary. For example, if the command was to open the Chrome app, you should return something like this: [{\"action\": \"click\", \"locationX\": \"45%\", \"locationY\": \"98%\"}] ; for actions you can use one of the following: 'click', 'type', 'right-click', 'double-click'. Also ensure that your response has nothing other than the JSON response, I should be able to take your response directly and convert it into a JSON without having to perform any other format modifications. Double check to ensure that the coordinates you give are correct as well, an error would result in the wrong app being opened. Also remember that the origin of the screen is the top left corner. Also ensure that the coordinates are percentages of the total screen size and not pixle values. Ensure coordinates are accurate for clicking the correct icon. Also ensure that there are no redundant or unneeded steps. Also ensure this error does not arise: Expecting value: line 1 column 1 (char 0)"]
    )

    position = json.loads(result.text)
    print(result.text)

    Xpos = (float(position[0]['locationX'].split('%')[0]) / 100) * (cwidth) + left
    Ypos = (float(position[0]['locationY'].split('%')[0]) / 100) * (cheight) + top

    Xperc = Xpos / width
    Yperc = Ypos / height

    print(Xpos, width)
    print(Ypos, height)

    Xpos = Xperc * int(screen_size[0])
    Ypos = Yperc * int(screen_size[1])


    pg.click(Xpos, Ypos + 20)

