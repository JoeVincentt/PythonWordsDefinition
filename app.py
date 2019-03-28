import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Did you mean %s instead? \n (Y/N)' %
                   get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        if yn == 'n':
            return 'The word doesn\'t exists. Please double check it.'
        else:
            return 'Wrong input!'

    else:
        return 'The word doesn\'t exists. Please double check it.'


word = input('Enter word: ')

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
