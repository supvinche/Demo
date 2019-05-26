import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        reply = input("Do you mean {} instead ? Enter y for Yes and n for No : ".format(get_close_matches(word, data.keys())[0]))
        if reply == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif reply =="n":
            return "the word doesn't exist"
        else:
            return "only n and y were accepted"

    else:
        return "the word doesn't exist"

word = input("Please give a word :   ")
print(translate(word))
