#Learning Python Collections

#Maria Suarez
#09/28/2021
#Lists
import os, random
os.system('cls')

names = ["Alex", "Jack", "Mary", "Ellen", "Peter", "Ray"]
print(names[1])
print(names)
# printing with a loop
for nam in names:
    print(nam, end= "  ")
print("\n These are all the names! \n")
# going in reverse
print(names[-1])
print(names[-2])
# range of indexes 
print(names[2:5])
#change value of an element
names[3]= "Betty"
if "Ellen" in names:
    print("You win!")
else:
    print("sorry, you are wrong ")
#lenght of a list
print(len(names))
#add elements using append()
names.append("Owen")
print(names)
#add elements using insert()
names.insert(4,"Joan")
print(names)
#copy a list to another list
otherNames= names[2:6].copy()
print(otherNames)
compParts=["keyboard", "printer", "MotherBoard", "CPU", " cooling fan", "storage"]

word= random.choice(compParts)
word = word.lower()
print(word)
for letter in word:
    print("_", end=" ")
print("\n")
guess=input("guess the word I am thinking ")
while (guess not in word):
    guess= guess.lower()
    if guess in word:
        print("You are right!! ")
        break
    else:
        print(" wrong!!!")
        guess=input("Try again ")
print("thank you for playing")
