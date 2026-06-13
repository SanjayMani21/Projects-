import ollama
import webbrowser

messages = [

    {
        "role": "system",
        "content": "You are a helpful assistant"
    }

]

while True:

    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye")
        break


    elif "google" in user:
        webbrowser.open("https://google.com")
        print("opening google")
        continue

    
    elif "search" in user:
        key_word =user.replace("search","")
        webbrowser.open(f"https://www.google.com/search?q={key_word.strip()}")
        continue


    # elif user == "open youtube":

    #     webbrowser.open(
    #         "https://youtube.com"
    #     )

        

    #     print("Bot: Opening YouTube")

    #     continue


    # elif user == "open google":

    #     webbrowser.open(
    #         "https://google.com"
    #     )

        

    #     print("Bot: Opening Google")

    #     continue

    messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    reply = response["message"]["content"]

    print("Bot:", reply)

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )