import pygame, os, time
# MAria Suarez
#Learning how to use pygame

#Initialize pygame
pygame.init()
os.system('cls')
#Declare the object to display game
# red = (150,0,0)
# purple= (150,0, 150)
#create a dictionary of colors:
# ask the user the size and the color forthe window
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
color= input("What color do you prefer: red, blue, green,purple,white, black ) ")
height= input("Enter the height of your window ")
width = input ("What is the width of your window ")

height= int(height) #should i do this? try and except
width = int (width)


screen=pygame.display.set_mode((width, height))
myColor= colors.get(color)
screen.fill(myColor)

pygame.display.update() #Use to update your screen

pygame.display.set_caption("My Game")
run=True #Variable to control the main loop
while run:
    pygame.time.delay(1000) #milliseconds
    for anyThing in pygame.event.get():
        if anyThing.type == pygame.QUIT:
            run =False
pygame.quit()



