import json
data = json.load(open("data.json"))


def GetDefinition(userWord):
    if userWord in data:
        return ''.join(data[userWord])
    else:
        # keepRunning = False
        return 'Word is not in the dictionary!'


keepRunning = True
print("\n\t\t\t\t\t\t\t\tType ex1t to quit the program")
while keepRunning:
    userInput = input("Enter Word: ").lower()
    if userInput != 'ex1t':
        print("Definition:", GetDefinition(userInput), "\n")
    else:
        print("\nHave a good day!\n")
        break
