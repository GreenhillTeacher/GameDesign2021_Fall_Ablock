#MAria SUarez 
# 10/26/2021 
# FONTS, Blit and creating functions

import pygame as py, os, time, random


py.init()

colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
WIDTH=700
HEIGHT=700
BLACK=colors.get('black')
WHITE=colors.get('white')
win=py.display.set_mode((WIDTH, HEIGHT))
win.fill(colors.get('white'))
#TITLE_FONT=py.font.SysFont(name of Font, size, bold=False, italic=False)
TITLE_FONT=py.font.SysFont("comicsans", 80)
WORDS_FONT=py.font.SysFont('comicsana',40)
text=TITLE_FONT.render("message", 1, BLACK)

#Images
bg1 = pygame.image.load('bgSmaller.jpg')


def display_Title(message, x,y):
    py.time.delay(100)
    text=TITLE_FONT.render(message, 1, BLACK)
    #the x is going to be 1/2 of WIDTH - half of text
    # the y is going to be 1/2 oh HEIGTH - 40
    win.blit(text, (x,y))
    py.display.update()
    py.time.delay(100)

run = True
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False

    win.fill(WHITE)
    display_Title("Settings",WIDTH/2-text.get_width()/2,40)
    py.time.delay(200)
    display_Title("Dallas",WIDTH/2-text.get_width()/2,HEIGHT/2-40)
    py.time.delay(200)