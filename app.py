import json
from difflib import get_close_matches

data = json.load(open('data.json'))

running = True

while running:
    def translate(w):
        w = w.lower()
        if w in data:
            return data[w]
        elif w.title() in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(w, data.keys())) > 0:
            yn = input('Did you mean %s instead? \n (Y/N)' %
                       get_close_matches(w, data.keys())[0])
            yn = yn.lower()
            if yn == 'y':
                return data[get_close_matches(w, data.keys())[0]]
            if yn == 'n':
                return '-------'*6 + '\n'+'The word doesn\'t exists. Please double check it.'
            else:
                return '-------'*6 + '\n'+'Wrong input!'

        else:
            return '-------'*6 + '\n'+'The word doesn\'t exists. Please double check it.'

    word = input(
        '-------'*6 + '\nProgram is running \n Press Q to Quit \n or \n Enter word: ')

    if word == 'q' or word == 'q':
        running = False
    else:
        output = translate(word)

        if type(output) == list:
            for item in output:
                print('-------'*6 + '\n'+item)
        else:
            print('-------'*6 + '\n'+output)
