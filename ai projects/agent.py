import ollama
import webbrowser

system_prompt = """
You are an AI assistant.

If user wants google search,
reply ONLY like this:

SEARCH: keyword

Examples:
SEARCH: bitcoin
SEARCH: nifty 50

For normal conversation,
reply normally.
"""

messages = [

    {
        "role": "system",
        "content": system_prompt
    }

]

while True:

    user = input("You: ")

    if user.lower() == "bye":
        break

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

    if reply.startswith("SEARCH:"):

        keyword = reply.replace(
            "SEARCH:",
            ""
        ).strip()

        webbrowser.open(
            f"https://google.com/search?q={keyword}"
        )

        print("Opening Google Search...")

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )