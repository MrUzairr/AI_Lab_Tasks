import random

# Define the chatbot's responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "traffic": "I'm sorry, I don't have access to real-time map information.",
    "joke": "Why did the chicken cross the road? To get to the other side!",
    "story": "Once upon a time, in a faraway land, there lived a brave knight..."
}

# Main chat loop
while True:
    user_input = input("User: ").lower()  # Convert input to lowercase for case-insensitivity

    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break

    if "hello" in user_input:
        print("Chatbot: Hi there! How can I help you today?")
    elif "traffic" in user_input:
        print("Chatbot: I'm sorry, I don't have access to real-time map information.")
    elif "joke" in user_input:
        print(f"Chatbot: {responses['joke']}")
    elif "story" in user_input:
        print(f"Chatbot: {responses['story']}")
    else:
        print("Chatbot: I'm not sure how to respond to that. Please ask me something else or type 'exit' to end the conversation.")
