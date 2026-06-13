import ollama
from datetime import datetime


# ROLE SET
messages = [

    {
        "role": "system",
        "content": "You are a NIFTY Trading MEntor"
    }

]

while True:
#INPUTS
    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Goodbye")
        break

    messages.append(
        {
            "role": "user",
            "content": user
        }
    )

# Processing
    response = ollama.chat(
        model="llama3",
        messages=messages
    )


# OUTPUT
    reply = response["message"]["content"]

    print("Bot:", reply)

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )