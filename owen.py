#Owen Ross 
#10/26
#learning about fonts, blit, and creating functions
import pygame as py, os, time, random
py.init()

colors = {'red':(150,0,0),'green':(0,255,0),'purple':(150,0,150),'black':(0,0,0), 'white':(255,255,255), 'blue':(0,0,255)}
black = colors.get('black')
white = colors.get('white')
width = 700
height = 700
window = py.display.set_mode((width, height))
#declare 2 types of font, title and words
title_font=py.font.SysFont('comicsana',80)
#Name of font, size, bold (true or false), Italic(true or false)
#words_font=py.font.SysFont(comicsana,40)
text=title_font.render("message", 1, black)
def display_Title(message, x,y):
    py.time.delay(100)
    text=title_font.render(message, 1, black)
    window.blit(text, (x,y))
    py.display.update
    py.time.delay(100)
#UPDATE DONT WORK FOR FONT
#Use the Get width to find length of word, then use that to position the text as you like
run = True
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False

    window.fill((255,255,255))
    display_Title("Settings",width/2-text.get_width()/2,40)
    py.time.delay(200)
    display_Title("Dallas", width/2-text.get_width()/2,height/2)
    py.time.delay(200)

