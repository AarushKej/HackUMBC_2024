from gemini import Gemini

client = Gemini(auto_cookies=True)


response = client.generate_content("Hello, Gemini. What's the weather like in Seoul today?")
print(response.payload)