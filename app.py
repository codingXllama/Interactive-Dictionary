import json
from difflib import get_close_matches

# opening and loading the content inside the json file
data = json.load(open('data.json'))

# This function is used for checking if the word exists in the json file and how to deal with the word if it's not
# This function returns the defintion for the word if it's found


def getMeaning(word):

    if word.lower() in data:
        return data[word]

    # if the word is not found in the json file directly, we will check for similar words in the json file
    elif len(get_close_matches(word, data.keys())) > 0:
        userPrompt = input("Did you mean %s instead? (Y for yes| N for no): " %
                           get_close_matches(word, data.keys())[0])
        # returning the similar word
        if userPrompt.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif userPrompt.lower() == 'n':
            return "The word does not exist"
        else:
            return "Invalid entry, please try again!"
    # if the word from the user is not similar from the already existing words in the json file
    else:
        return "The word does not exist"


# This is the menu for the user to decide what to input and what their output will be
print("\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\tEnter ex1t to Quit the Program\n")
while True:

    # user prompt
    print("__________________________\n")

    userWord = input("Enter a word: ")

    # checking if the user want's to exist the program
    if userWord == 'ex1t':
        break
    else:
        # getting the meaning for the inputted word
        wordDefn = getMeaning(userWord)

        # converting a list into a string
        print("__________________________")
        print("\nThe definition of %s:" % userWord, end='\n\n')

        # if the word definition  is type list, we will break it down into smaller sentences else we will just display the sentence
        if type(wordDefn) == list:
            # this means the word is a list and thus we will convert it into seperate strings
            for sentence in wordDefn:
                print(sentence)
            # print('\n')
            print("__________________________")

        else:
            print(''.join(wordDefn))


print("Thanks for using the program ")
