import random
from datetime import datetime

name = ""

hello_replies = [
    "Hi",
    "Hello",
    "Hey"
]

bye_replies = [
    "Goodbye",
    "See you",
    "Bye friend"
]

while True:

    user = input("You: ").lower()

    if user == "hello" or user == "hi":

        reply = random.choice(hello_replies)

        if name == "":
            print("Bot:", reply)

        else:
            print("Bot:", reply, name)

    elif user.startswith("my name is"):

        name = user.replace("my name is ", "")

        print(f"Bot: Nice to meet you {name}")

    elif user == "time":

        current_time = datetime.now()

        print("Bot:", current_time)

    elif user == "calculate":

        num1 = int(input("First number: "))
        operator = input("Operator: ")
        num2 = int(input("Second number: "))

        if operator == "+":
            print("Bot:", num1 + num2)

        elif operator == "-":
            print("Bot:", num1 - num2)

        elif operator == "*":
            print("Bot:", num1 * num2)

        elif operator == "/":
            print("Bot:", num1 / num2)

        else:
            print("Bot: Invalid operator")

    elif user == "bye":

        print(
            "Bot:",
            random.choice(bye_replies)
        )

        break

    else:
        print("Bot: I don't understand")