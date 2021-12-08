#Shaina Starr 
#11/4/21

import pygame as py, os, random, time
py.init()
BLACK=(0,0,204)
WHITE=(153,205,204)
PINK=(255,105,180)
WIDTH = 800       
HEIGHT = 800
colors={'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,255), 'purple': (150,0,150), 'white': (255,255,255), 'black': (0,0,0), 'navy': (0,80,128), 'hot pink': (255,105,180), 'orange': (255,165,0)}
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
COLOR=WHITE
bmessages=["Back"]
messages=['Instructions','Level 1','Level 2','Settings','Score Board', 'Exit']
messages2=['Screen size', 'Object Color', 'Sound on/off', ]
Ssmessages=['Larger', 'Smaller', ]
imessages=["To win make the circle eat the square"]
win=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Setting Window")
TITLE_FONT= py.font.SysFont('comicsans', 80)
SUBTITLE_FONT= py.font.SysFont('comicsans', 40)
INSTRUCTION_FONT=py.font.SysFont('comicsans',20)
text=TITLE_FONT.render('message',1,BLACK)
xbox=25
wbox=25
square=py.Rect(10,10, wbox, xbox)

#images
#BG1=py.image.load('Images\\maze.jpg')

def display_message(message, x,y):
    py.time.delay(100)
    text=TITLE_FONT.render(message,30, BLACK )
    win.blit(text, (WIDTH/2-text.get_width()/2, 30) )
    py.display.update()
    py.time.delay(10)

def displaySub(subTitle,ysub):
    py.time.delay(100)
    text=SUBTITLE_FONT.render(subTitle,1, BLACK )
    win.blit(text, (10, ysub ))
    py.display.update()
    py.time.delay(10)

def display_back():
    x=660
    y=730
    square.x=x
    square.y=y
    for i in range(0,len(bmessages)):
        word= bmessages[i]
        py.draw.rect(win, PINK, square)
        text=SUBTITLE_FONT.render(word,10, BLACK)
        win.blit(text, (x+wbox+10, y))
        py.display.flip()
        
        square.y=y

counter=1
def display_Menu(messageList):
    x=70
    y=190
    square.x=x
    square.y=y
    counter=1
    for i in range(0, len(messageList)):
        word= messageList[i]
        py.draw.rect(win, PINK, square)
        text=SUBTITLE_FONT.render(word,10, BLACK)
        win.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 100
        square.y=y
        py.display.set_caption("Menu Window")

win.fill(WHITE)
display_message('Menu', xbox, wbox)
ysub=200
py.time.delay(200)
display_Menu(messages)

run=True
counter=1
back=1
while run:
    
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False

    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=py.mouse.get_pos()
            # print(mouse_pos)
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>490 and mouse_pos[1]<515 and counter==1:
                win.fill(WHITE)
                display_message("Settings", xbox, wbox)
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                counter +=2
                display_Menu(messages2)
                back+=1
                x=660
                y=730
                square.x=x
                square.y=y
                display_back()

            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==1:
                win.fill(WHITE)
                display_message('Instructions', xbox, wbox)
                py.display.set_caption("instructions window")
                # x=70
                # y=190
                # square.x=x
                # square.y=y
                myfile=open('instructions.txt', 'r')
                yi=200
                for line in myfile.readlines():
                    print(line)
                    text=INSTRUCTION_FONT.render(line,1,BLACK)
                    win.blit(text, (40,yi))
                    py.display.flip()
                    py.time.delay(50)
                    yi+=50
                myfile.close()
                
                
                # for i in range(0, len(imessages)):
                #     word= imessages[i]
                #     py.draw.rect(win, PINK, square)
                #     text=SUBTITLE_FONT.render(word,10, BLACK)
                #     win.blit(text, (x+wbox+10, y))
                #     py.display.flip()
                #     py.time.delay(100)
                #     y += 100
                #     square.y=y
                
                back+=1
                counter+=1
                x=660
                y=730
                square.x=x
                square.y=y
                display_back()
                

            
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==3:
                win.fill(WHITE)
                display_message('Screen Size', xbox, wbox)
                py.display.set_caption("Screen Size Window")
                x=70
                y=190
                square.x=x
                square.y=y
                display_Menu(Ssmessages)
                display_back()
                counter+=1
                back+=1

            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>730 and mouse_pos[1]<=755 and (back==2 or counter==1):
                win.fill(WHITE)
                display_message('Menu', xbox, wbox)
                counter=1
                back=1
                display_Menu(messages)



            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>730 and mouse_pos[1]<=755 and (back==3 or counter==3):
                win.fill(WHITE)
                counter=3
                back=1
                win.fill(WHITE)
                display_message("Settings")
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                x=70
                y=190
                square.x=x
                square.y=y
                display_Menu(messages2)
                back+=1
                x=660
                y=730
                square.x=x
                square.y=y
                display_back()
                square.y=y    
                
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>190 and mouse_pos[1]<=215 and counter==4:
                WIDTH+=50
                HEIGHT+=50
                win=py.display.set_mode((WIDTH,HEIGHT))
                win.fill(WHITE)
                display_message('Screen Size', xbox, wbox)
                display_Menu(Ssmessages)
                display_back()
                   
               
py.quit()        
