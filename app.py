import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def getMeaning(word):

    if word.lower() in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        userPrompt = input("Did you mean %s instead? (Y | N): " %
                           get_close_matches(word, data.keys())[0])
        if userPrompt.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif userPrompt.lower() == 'n':
            return "The word does not exist"
        else:
            return "Invalid entry, please try again!"
    else:
        return "The word does not exist"


print("\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\tEnter ex1t to Quit the Program\n")
while True:

    # user prompt
    print("__________________________\n")
    userWord = input("Enter a word: ")
    if userWord == 'ex1t':
        break
    else:
        wordDefn = getMeaning(userWord)

        # converting a list into a string
        print("__________________________")
        print("\nThe definition of %s:" % userWord, end='\n\n')
        if type(wordDefn) == list:
            # this means the word is a list and thus we will convert it into seperate strings
            for sentence in wordDefn:
                print(sentence)
            # print('\n')
            print("__________________________")

        else:
            print(wordDefn)


print("Thanks for using the program ")
