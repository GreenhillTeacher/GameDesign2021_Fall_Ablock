#MAria Suarez
#09/30/2021
#add instuctions
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word
import random, os
os.system('cls')

print("Guess a word one letter at the time ")
compParts=['keyboard', "CPU", "storage", "ports", "Monitors", "OperatING SystEMS"]
name= input(" What is your name ? ")
answer=input(name + ", do you want to play the game? ")
while 'y' in answer:
    word=random.choice(compParts)
    word=word.lower()
    print(word)
    turns=len(word)+2
    check = True
    guesses=''
    while (turns>0 and check):
        for letter in word:
            if letter in guesses:
                print(letter, end=" " )
                if len(guesses)==len(word):
                    check = False
            else:
                print ("_", end=" ")
        newGuess=input ("\n please enter a letter ")
        if newGuess in word:
            guesses += newGuess
            print(" Good guess ")
        else:            
            turns -=1
            print("sorry guess again")
    answer=input( name + "Do you want to play again? ")
print(name+ ", Thank you for playing")
