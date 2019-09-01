import json
from difflib import SequenceMatcher
data = json.load(open("data.json"))


def SimilarWordRatio(userWord):
    for wordInDictionary in data:
        if(SequenceMatcher(None, userWord, wordInDictionary).ratio() > 0.8):
            userInput = input(
                ("\nDid you mean? % s (Y or N): " % wordInDictionary))
            if userInput == 'y':
                return ''.join(data[wordInDictionary])
            else:
                return "The Word is not in dictionary, please try again!"


def GetDefinition(userWord):
    if userWord in data:
        return ''.join(data[userWord])
    else:
        # keepRunning = False
        return SimilarWordRatio(userWord)


keepRunning = True

print("\n\n\t\t\t\t\t\t\t\tType ex1t to quit the program")
while keepRunning:
    userInput = input("Enter Word: ").lower()
    if userInput != 'ex1t':
        print("Definition:", GetDefinition(userInput), "\n")
    else:
        print("\n<______________________>\n")
        print("    Have a good day!")
        print("<______________________>\n")
        keepRunning = False
