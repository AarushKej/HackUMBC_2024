import google.generativeai as genai
import os
import json
import pyautogui as pg

api_key = "AIzaSyDj9X15nYR83615JzaRTswdG2LrHZTcfIE"
genai.configure(api_key=api_key)

myfile = genai.upload_file("image.png")
print(f"{myfile=}")

model = genai.GenerativeModel("gemini-1.5-flash")
result = model.generate_content(
    [myfile, "\n\n", "From this image of a Mac computer's screen perform the task in this command: Open the tab that says Managing Multi; I want you to respond with only a list of the commands and each step should be in a dictionary. For example, if the command was to open the Chrome app, you should return something like this: [{\"action\": \"click\", \"locationX\": \"45%\", \"locationY\": \"98%\"}] ; for actions you can use one of the following: 'click', 'type', 'right-click', 'double-click'. Also ensure that your response has nothing other than the JSON response, I should be able to take your response directly and convert it into a JSON without having to perform any other format modifications. Double check to ensure that the coordinates you give are correct as well, an error would result in the wrong app being opened. Also remember that the origin of the screen is the top left corner. Also ensure that the coordinates are percentages of the total screen size and not pixle values."]
)
actions = json.loads(result.text)
print(result.text)
XLocPercent = int(actions[0]['locationX'].split("%")[0]) / 100
YLocPercent = int(actions[0]['locationY'].split("%")[0]) / 100
print(XLocPercent, YLocPercent)
screen_size = pg.size()
pg.moveTo(XLocPercent * screen_size[0], YLocPercent * screen_size[1])