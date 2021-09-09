#Maria Suarez
#Arithmetic operators
# + - * / %
#check for eve numbers

import os
os.system('cls')

num= int(input("give me a number"))
rem=num%2
#conditional
if(rem ==0):
    print(" The number is even")
else:
    print("the number is odd")