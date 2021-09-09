#Maria I Suarez
# 
import os

os.system('cls')
star=int(input("How many stars? "))
print("stars", star)
line=star
for i in range(line):
    #add a loop for the spaces
    for counter in range(star): #you can use a number or var
        print("*", end=" " )   #print on the same line
        #print(counter+1, end=" ")
    print() #print a return creating a new line
    star-=1# short cut for star=star-1 
print("Thank you! ")