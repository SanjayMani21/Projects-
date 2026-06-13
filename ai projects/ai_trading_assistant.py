#import AI 
import ollama
import webbrowser
import json

# Memory
messages =[
    {
        # Telling AI who it is.
        "role": "system",
        "content": "You are a professional Trading Assistant."
    }
] 

# Load file if it already exists:
try:
    with open("trading_assistant_memory.json","r") as file:
        messages = json.load(file)

# If doesn't exist create empty:
except:
    messages =[
    {
        # Telling AI who it is.
        "role": "system",
        "content": "You are a professional Trading Assistant."
    }
] 

# INPUTS
while True:

    
    user = input("You: ").lower()


    if user == "bye":
        print("\nBot: Bye!!!")
        break

    # add the input from user to memory
    
    elif "open" in user:
        key_word = user.replace("open","").strip()
        
        
        if key_word == "trading view" or key_word == "tradingview":

            webbrowser.open("https://www.tradingview.com/")
            print("\nOpening Trading View.")
        continue




    elif "search" in user:
        key_word = user.replace("search","").strip()
        webbrowser.open(f"https://google.com/search?q={key_word}")
        print(f"Searching {key_word.capitalize()} ...")
        continue
        
    # stores the inputs from user to messages list
    messages.append(
        {            
            "role": "user",
            "content" : user
        }
    )



# PROCESSING
    response = ollama.chat(
        model="llama3",
        messages= messages
    )
        
# Output
    reply = response["message"]["content"]
    # Stores the reply from assistant to messages.
    messages.append(
        {
            "role" : "assistant",
            "content" : reply
        }
    )

# Print Output
    print("\nBot: " + reply + "\n")
    
# Saving the responses and input in file:
    with open("trading_assistant_memory.json","w") as file:
        json.dump(messages,file)



    # if input is hi process the input and say hi





