import random
from os import system, name

with open('wordlist.txt', 'r' , encoding = "utf8") as f:
    word=random.choice(f.readlines()).rstrip()
    
found=False
lives=15
tries=0;
letters=[]


def clear():
    # check and make call for specific operating system
    
    # for mac and linux(here, os.name is 'posix')
    if name == 'posix':
        _ = system('clear')
 
    # for win
    else:
        _ = system('cls')

def hide(): # hide letter function - 
    hidden=''
    for letter in word:
        if letter in letters:
            hidden += letter
        else:
            hidden += '-'
    return hidden 
    
def misscounter(tries,lifes): # count misses
    found=False
    for letter in word:
        if letter in letters:
            found = True
    tries +=1    
    print (f'Your have used {tries} lives of your {lives}')

    return tries     

    
letter= input('Please give a letter! or press - to exit')
letters.append(letter)
hidden_word=hide()
while (letter != '-' and tries<lives ): #hide letters
    
    tries=misscounter(tries,lives)
    print (hidden_word)
    hidden_word=hide()
    clear()
    letter= input('Please give a letter! or press - to exit!')


if (letter=='-'):
    print ('bye!')
else:
    print ('Sorry you lost! You can try again! bye!')
