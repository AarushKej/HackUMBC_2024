from gemini import Gemini

client = Gemini(auto_cookies=True)

api_key = "AIzaSyDj9X15nYR83615JzaRTswdG2LrHZTcfIE"


response = client.generate_content("Hello, Gemini. What's the weather like in Seoul today?")
print(response.payload)