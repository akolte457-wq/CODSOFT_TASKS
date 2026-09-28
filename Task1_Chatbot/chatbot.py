def chatbot():
    print("🤖 Chatbot: Hello! I am a simple Python chatbot.")
    print("🤖 Chatbot: Type 'bye' to end the conversation.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("🤖 Chatbot: My name is CodBot.")

        elif "help" in user_input:
            print("🤖 Chatbot: I can respond to greetings, questions about my name, and simple conversations.")

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that yet.")


if __name__ == "__main__":
    chatbot()
