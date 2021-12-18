import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]      
    elif len(get_close_matches(word,data.keys())) > 0:
        ask = input("Did you mean %s instead?Y/N for yes and no"%get_close_matches(word,data.keys())[0])
        if ask == "Y" or ask == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif ask == "N" or ask == "n":
            return "Not Found."    
    else:
        return "Not Found."    
words = input("Enter Word:")
output = translate(words)

if type(output) == list :
    for i in output:
        print("\n",i,"\n")
else:
    print (output)