# Maria Suarez
# Date: 09/14/2021
# DAta type and how to check for the right type of data

import os
os.system('cls')

#variable declare and initialize
num = 30
print(type(num))
num = 6.7
print(type(num))
userInput=input("type something ")
#How to check for your data
try:
    userInput=float(userInput)
    print(type(userInput))
    check=True
except ValueError:
    check =False
#Using conditional statement if/else
if (check):
    print(num + userInput)
else:
    print("Sorry I can add that number ")
print(num/0)
