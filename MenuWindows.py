#MAria SUarez 
# 10/26/2021 
# FONTS, Blit and creating functions

import pygame as py, os, time, random


py.init()

colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
messages=["ScreenSize", "Background Color", "Object Color", "Sounds On/Off"]
WIDTH=700
HEIGHT=700
rt=random.choice(list(colors))

BLACK=colors.get('black')
WHITE=colors.get('white')
PURPLE=colors.get('purple')
win=py.display.set_mode((WIDTH, HEIGHT))
win.fill(colors.get('white'))
#TITLE_FONT=py.font.SysFont(name of Font, size, bold=False, italic=False)
TITLE_FONT=py.font.SysFont("comicsans", 80)
WORDS_FONT=py.font.SysFont('comicsans', 70, italic=True)
text=TITLE_FONT.render("message", 1, BLACK)
wbox=25
hbox=25
square = py.Rect(10,10, wbox,hbox)

def display_Title(message, x,y):
    py.time.delay(100)
    text=TITLE_FONT.render(message, 1, BLACK)
    #the x is going to be 1/2 of WIDTH - half of text
    # the y is going to be 1/2 oh HEIGTH -=70
    win.blit(text, (x,y))
    py.display.update()
    py.time.delay(100)

def display_Menu():
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0, len(messages)):
        word= messages[i]
        py.draw.rect(win, PURPLE, square)
        text=WORDS_FONT.render(word, 1, BLACK)
        win.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 100
        square.y=y
WHITE=colors.get(rt)
win.fill(WHITE)
display_Title("Settings",WIDTH/2-text.get_width()/2, 70)
py.time.delay(200)
display_Menu()
run = True
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=py.mouse.get_pos()
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1] >=190 and mouse_pos[1]<210:
                win.fill(WHITE)
                display_Title("Screen Size",WIDTH/2-text.get_width()/2, 70 ) 
    
    print(py.mouse.get_pos())