import google.generativeai as genai


API_KEY= "AIzaSyDj9X15nYR83615JzaRTswdG2LrHZTcfIE"

genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
