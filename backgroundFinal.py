import pygame
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,145), 'white':(255,255,255), 'purple':(150,0,150), 'orange':(255, 165, 0)}
#GLOBAL VARIABLES
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
COLOR=WHITE
# Screen and square definition
WIDTH=800
HEIGHT=800
win=pygame.display.set_mode((WIDTH,HEIGHT))
win.fill(WHITE)
pygame.display.update()
bg1 = pygame.image.load('bgSmaller.jpg')
run=True 
# C:\Users\suarezm\OneDrive - Greenhill School\Game Design\GameDesign2021_Fall_Ablock\cade.py  
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
    win.blit(bg1, (0,0))
    pygame.display.set_caption("My game 1")
    pygame.display.flip()