#Maria I Suarez
# Libraries
import os

os.system('cls')
star=int(input("How many stars? "))
print("stars", star)
line=star
spc=0
for i in range(line):
    #add a loop for the spaces
    for counter in range(star): #you can use a number or var
        print("*", end=" " )   #print on the same line
        #print(counter+1, end=" ")
    for space in range (spc):
        print(" ", end=" " )
    for counter in range(star): #you can use a number or var
        print("*", end=" " )   #print on the s
    print() #print a return creating a new line
    star-=1# short cut for star=star-1 
    spc +=2
print("Thank you! ")