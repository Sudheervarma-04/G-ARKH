# import nltk
# from nltk.chat.util import Chat, reflections

# # Define the chatbot responses using pattern-response pairs
# chatbot_responses = [
#     (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
#     (r'how are you|how are you doing', ['I am doing well, thank you!', 'I\'m fine, thanks!']),
#     (r'what is your name', ['I am a simple chatbot.', 'I\'m just a chatbot.']),
#     (r'bye|goodbye', ['Goodbye!', 'Bye! Have a great day!']),
#     # Add more pattern-response pairs as needed
# ]

# # Create the chatbot with the defined responses
# chatbot = Chat(chatbot_responses, reflections)

# # Main loop to interact with the chatbot
# print("Chatbot: Hi! I'm a simple chatbot. You can start chatting with me. Type 'exit' to end the conversation.")
# while True:
#     user_input = input("You: ").lower()
#     if user_input == 'exit':
#         print("Chatbot: Goodbye!")
#         break

#     response = chatbot.respond(user_input)
#     print("Chatbot:", response)


import requests

# Define a function to fetch weather information from an API
def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_codewhats == 200:
        data = response.json()
        weather_info = data['current']['condition']['text']
        return weather_info
    else:
        return 'Sorry, I could not retrieve weather information at the moment.'

# ... Chatbot code ...

# Main loop to interact with the chatbot
print("Chatbot: Hi! I'm a chatbot. You can ask me about the weather. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ").lower()
    if user_input == 'exit':
        print("Chatbot: Goodbye!")
        break

    if 'weather' in user_input:
        city = input("Chatbot: Sure! Which city would you like to know the weather for? ")
        weather = get_weather(city)
        print("Chatbot: The weather in", city, "is currently", weather)

    # Add more chatbot logic here for other inthients and API interactions

# ... Rest of the chatbot code ...
