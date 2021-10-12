#Ryan Taffe 
#9/30/21
import os
import random
os.system('cls')
score=0

print("Welcome to Hangman")
HardestWords=["Elephant","Bathtub","Pencil","Texas"]
IntermediateWords=["Desk", "Wire", "Fast", "Shirt"]
EasyWords=["Box","Cat","Man","Dad"]

name=input("What is your name? ")

def Menu():
    print("########################################")
    print("#        Choose a difficulty           #")
    print("#              1=Easy                  #")
    print("#             2=Medium                 #")
    print("#              3=Hard                  #")
    print("#             4=Score Board            #")
    print("#              5=Exit                  #")
    print("########################################")
    difficulty = input("Enter your choice ")
    if '3' in difficulty:
        word=random.choice(HardestWords)
    elif '2' in difficulty:
        word=random.choice(IntermediateWords)
    elif '1' in difficulty:
        word=random.choice(EasyWords)
    elif '4' in difficulty:
        scoreBoard()
        os.system('cls')
        Menu()
    else:
        print("That is not an available difficulty")
        answer=input(name + ", Choose a different difficulty")
    return word
def scoreBoard():
    #create our object file so we can open our txt file
    os.system('cls')
    myScore=open('score.txt', 'r')
    print(myScore.read())
    myScore.close()
    input("Are you ready to leave")
word= Menu()
word=word.lower()
turns=len(word)+2
check = True
guesses=" "
while (turns>0 and check):
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
            if len(guesses)==len(word):
                check = False
        else:
            print("_", end=" ")
    newGuess=input("\n Please enter a letter ")
    newGuess=newGuess.lower()
    if newGuess in word:
        guesses += newGuess
    else:
        turns -=1
        print("Sorry, guess again")
print("You guessed right! The word was", word)
score+=3*len(word)+5*turns
os.system('cls')
print("Score: ", score)
difficulty=Menu()
MyFile=open('score.txt', 'a')
MyFile.write(name+ "\t Score: \t"+str(score))

MyFile.close()
print(name,", thank you for playing")

