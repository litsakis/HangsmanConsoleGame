import random

with open('wordlist.txt', 'r' , encoding = "utf8") as f:
    word=random.choice(f.readlines()).rstrip()
    
found=False
tries=15
letters=[]


def hide():
    hidden=''
    for letter in word:
        if letter in letters:
            hidden += letter
        else:
            hidden += '-'
    return hidden
    
letter= input('Please give a letter! or press - to exit')
letters.append(letter)
hidden_word=hide()
while (letter != '-'):
    print (hidden_word)
    hidden_word=hide()
    letter= input('Please give a letter! or press - to exit!')



print ('bye!')