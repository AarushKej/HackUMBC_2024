import google.generativeai as genai
import os
import json
import pyautogui as pg
import cv2
from functions import openApp, search, opentab, closetab, ask, press


def doShit(command):
    api_key = "AIzaSyA2M7JcwXPJV_jHfauEzi0a8UawxHso2pM"
    genai.configure(api_key=api_key)

    screen_size = pg.size()
    image = cv2.imread("screen.png")
    height, width = image.shape[:2]

    myfile = genai.upload_file("screen.png")

    generation_config = {
        "temperature": 0,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro"
        )
    valid = False
    while not valid:
        try:
            result = model.generate_content(
                [myfile, "\n\n", "From this image of a Mac computer's screen which is of this size" + str((width, height)) + "; perform the task in this command: "+ command +" ; I want you to respond with only a list of the commands and each step should be in a dictionary. For example, if the command was to open the Chrome app, you should return something like this: [{\"action\": \"click\", \"locationX\": \"45%\", \"locationY\": \"98%\"}]. Also ensure that your response has nothing other than the JSON response, I should be able to take your response directly and convert it into a JSON without having to perform any other format modifications. Double check to ensure that the coordinates you give are correct as well, an error would result in the wrong app being opened. Also remember that the origin of the screen is the top left corner. Also ensure that the coordinates are percentages of the total screen size and not pixle values. Ensure coordinates are accurate for clicking the correct icon. Also ensure that there are no redundant or unneeded steps. Also ensure this error does not arise: Expecting value: line 1 column 1 (char 0). Make sure the percentages are between 0 and 100%. If the command is to open an app, do not worry about the mouse position or anything, but worry about the name of the application. You should return something like this in that case: {\"action\": \"open\", \"app\": \"APPNAME\"}. If the command is to search something up, do not worry about the mouse position or the app name or anything, but worry about the name of the search. You should return something like this in that case: {\"action\": \"search\", \"search\": \"SEATCHTITLE\"}. If the command is a question forget everything no mouse no app no search and return the answer. Something like this.{\"action\": \"question\", \"question\": \"ANSWER\"} I]. If the action is close tab forget about everything else and only return something like this You should return something like this in that case: {\"action\": \"close tab\", \"close tab\": \"true\"}. if the command is to press a certain keybord determine which key it is between the options that pyautogui allows you to use You should return something like this in that case: {\"action\": \"press\", \"press\": \"KEY TO PRESS\"}. Make sure you differenciate between a question and a command. dont make questiosn into type responses. if the command starts with what is or who is or when was or how is or any sort of question word return type question. of the command begins with open make sure to return type open if the command starts with search or search up make sure to return type search. never use return type of type unless the command says type this. Make sure you look at the whole command and dont infer whaat you want it to do. Only base the command off of what is said"]
            )

            actions = json.loads(result.text)
            print(result.text)
            if float(actions[0]['locationX'].split("%")[0]) < 100 and float(actions[0]['locationY'].split("%")[0]) < 100: valid = True
        except:
            try: 
                if actions[0]['action'] == "open": valid = True
                if actions[0]['action'] == "search": valid = True
                if actions[0]['action'] == "question": valid = True
                if actions[0]['action'] == "type": valid = True
                if actions[0]['action'] == "close tab": valid = True
                if actions[0]['action'] == "press": valid = True

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
    elif actions[0]['action'] == "open":
        openApp(actions[0]['app'])
    elif actions[0]['action'] == "search":
        opentab()
        search(actions[0]['search'])
    elif actions[0]['action'] == "question":
        ask(actions[0]['question'])
    elif actions[0]['action'] == "type":
        search(actions[0]['type'])
    elif actions[0]['action'] == "close tab":
        closetab()
    elif actions[0]['action'] == "press":
        press(actions[0]['press'])

    # Read the original image

    # Ensure the coordinates are integers
    if actions[0]['action'] == "click":
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
        else:
            print("Error: Cropped image is empty or invalid")

        myfile = genai.upload_file("cropped_screen.png")

        cimage = cv2.imread("cropped_screen.png")
        cheight, cwidth = cimage.shape[:2]


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


        Xpos = Xperc * int(screen_size[0])
        Ypos = Yperc * int(screen_size[1])


        pg.click(Xpos, Ypos + 20)

