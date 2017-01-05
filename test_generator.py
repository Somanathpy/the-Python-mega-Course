#text generator
#Authotr:- Somanath Patil

import string,random
vowels = 'aeiou'
consonants = 'bcdfghijklmnpqrstvxyz'
letters = string.ascii_lowercase

letter_input1 = raw_input("enter a letter,for vowels:'v',for consonants:'c',for any letter:'l'")
letter_input2 = raw_input("enter a letter,for vowels:'v',for consonants:'c',for any letter:'l'")
letter_input3 = raw_input("enter a letter,for vowels:'v',for consonants:'c',for any letter:'l'")

def generator():
    if letter_input1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = letter_input1

    if letter_input2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_input2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = letter_input2

    if letter_input3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input3 == 'c':
        letter3 = random.choice(consonants)
    elif letter_input3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = letter_input3
    name = letter1+letter2+letter3
    return name
for i in range(20):
    print generator()
