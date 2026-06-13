import json

try:
    
    # Load dump from file
    with open("memory.json", 'r') as file:
            data = json.load(file)

except:
     data = []
    
        

while True:

    print(
         "1 - Enter Details\n" \
         "2 - Show Saved Data \n" \
         "3 - Clear All Data\n" \
         "4 - Exit" 
         )
    

    user_input = input("You: ")
    



    # Conditions
    
    if user_input == '1':
        name = input("\nName: ")
        age = input("Age: ")

        data.append({"Name": name, "Age": age})


        
# Saving in to dumps
        with open("memory.json",'w') as file:
              json.dump(data,file)
        print("\nSaved!!!\n")
        continue

    elif user_input == '2':
        if data ==[]:
            print("\nData is empty\n") 

        else:
            print("\nPrinting Details:")
            print("\n", data , '\n')
        continue

    elif user_input == '3':
         data.clear()
         with open("memory.json",'w') as file:
              json.dump(data,file)
       
         print("\nCleared")
    elif user_input == "4":
         break





