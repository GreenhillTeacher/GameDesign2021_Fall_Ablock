# how to use loops
#how to ask the user for data1
#keyword input()
#input gives you a string ('str')
# we need to typecast force it to be an integer
num=int(input("PLease enter a number "))
print(num)
star = num
for line in range(num):
    for counter in range(star):
        print("*", end=" ")
    star -=1 #(star = star -1)
    print()
