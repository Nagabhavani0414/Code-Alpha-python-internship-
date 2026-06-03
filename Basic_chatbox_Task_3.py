# Basic Chatbot for CodeAlpha Internship

print("🤖 ChatBot: Hello! I am your chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("🤖 ChatBot: Hello! How are you?")
    
    elif user == "how are you":
        print("🤖 ChatBot: I am fine. Thank you for asking!")
    
    elif user == "what is your name":
        print("🤖 ChatBot: My name is Python ChatBot.")
    
    elif user == "who created you":
        print("🤖 ChatBot: I was created using Python.")
    
    elif user == "help":
        print("🤖 ChatBot: You can ask me simple questions.")
    
    elif user == "bye":
        print("🤖 ChatBot: Goodbye! Have a nice day.")
        break
    
    else:
        print("🤖 ChatBot: Sorry, I don't understand that.")