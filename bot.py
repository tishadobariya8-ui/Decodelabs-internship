import random
import re

responses = {
    "how are you": "I am fine!",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! How can I assist you today?",
    "good evening": "Good evening! How can I assist you today?",
    "good  night": "Good night! Sleep well.",
    "what is your name": "I am a simple chatbot.",
    "what can you do": "I can answer simple questions and have a conversation with you.",
    "what is the capital of india": "The capital of India is New Delhi.",
    "what is your boss": "I don't have a boss, I am an AI created to assist you.",
    "bye": "Goodbye!"
}

fallback = [
    "I don't understand 🤔",
    "Can you ask something else?",
    "I am still learning 😊",
    "Sorry, I didn't get that.",
    "Please try another question!"
]

while True:

    user = input("You: ").lower().strip()

    if user == "hello" or user == "hii" or user == "hyy":
        print("Bot: Hello, Buddy! I'm here for you.")

    elif user == "how are you ?":
        print("Bot: I am fine! How are you?")

    elif "doing" in user:
        print("Bot: I am doing great! How about you?")

    elif "weather" in user:
        print("Bot: Sorry, I cannot check weather right now.")

    elif "time" in user:
        print("Bot: I cannot check time now.")

    elif "sad" in user:
        print("Bot: Don't worry, everything will be okay 😊")

    elif "i am tired" in user:
        print("Bot: You are doing great. Take some rest 😊")

    elif "thank you" in user or "thanks" in user:
        print("Bot: Anytime! Buddy 😊")

    elif any(op in user for op in "+-*/()"):
        match = re.search(r'[\d+\-*/(). ]+', user)

        if match:
            expression = match.group().strip()

            try:
                print("Bot:", eval(expression))
                
            except:
                print("Bot: Invalid mathematical expression.") 
        
    elif user in responses:
        print("Bot:", responses[user])

    elif user == "exit":
        print("Bot: Goodbye!")
        break
        
    else:
        print("Bot:", random.choice(fallback))
