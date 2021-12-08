#Aman Jaleel
#Here is my final game
#I am doing falling skies
#11/25/21

import os,random,time, pygame as py, sys, math
import pygame, os,random,time

from pygame import color
os.system('cls')
pygame.init()

## LISTS FOR MENU MESSAGES
figy=600

WIDTH=800
HEIGHT=800
figx=350
FALLING_SPEED= 1
pixel=64
fall_y=0
fall_x=random.random()*WIDTH
screenMessage=[ "800x800", "800x600", "600x600"]
settingMessages=["Screen Size", "Background colors",]
mainMenu=["Instructions", 'Settings', "Level 1", "Level 2", "ScoreBoard", "Exit"]
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,145), 'white':(255,255,255), 'purple':(150,0,150), 'orange':(255, 165, 0)}
#GLOBAL VARIABLES
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
COLOR=WHITE
MAINMENU=True
SETTINGS=False
INSTRUCTIONS=False
BACKGROUND=False
SCREEN=False
LEVEL1=False
LEVEL2=False
SCOREBOARD=False
OBJECTCOLOR=False
SOUNDS=False
flag=False

# Screen and square definition
WIDTH=800
HEIGHT=800
wbox=30
hbox=30
rect = py.Rect(figx, figy, hbox, wbox)
rocksquare= py.Rect(fall_x,fall_y, 100, 50)
x=70
y=150
xs=50
ys=200
xm=0
ym=0
speed=10
win=pygame.display.set_mode((WIDTH,HEIGHT))
bg=py.image.load("Pygame-Tutorials-master\Game\\bg.jpg")
FIG=py.image.load("Pygame-Tutorials-master\Game\standing.png")
Fall=py.image.load("Pygame-Tutorials-master\Game\L9E.png")
picture = pygame.transform.scale(Fall, (200, 300))
pygame.display.set_caption("Setting Window")
square=pygame.Rect(x,y, wbox,hbox)
screenSize=pygame.Rect(xs,ys,wbox*4, hbox*4)
win.fill(COLOR)
squaresSize=[pygame.Rect(xs,ys,wbox*4, hbox*4), pygame.Rect(xs,ys,wbox*4, hbox*3), pygame.Rect(xs,ys,wbox*3, hbox*3)]
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('comicsans', 80)
MENU_FONT=pygame.font.SysFont('comicsans', 40)
INSTRUCTIONS_FONT=pygame.font.SysFont('comicsans', 30)
text= TITLE_FONT.render('message',1,BLACK)
#New window title
#images
#bg1 = pygame.image.load('bgSmaller.jpg')
#Function to print Titles to all screens
def display_Title(message,ym):
    pygame.time.delay(100)
    text= TITLE_FONT.render(message,1,BLACK)
    xm=WIDTH/2-text.get_width()/2
    win.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(100)

#Function to print all the menus 
def Menu_function(line):
    pygame.time.delay(100)
    ym=y
    square.y=y
    xm=x+wbox+10
    for i in range(0,len(line)):
        word=line[i]
        pygame.draw.rect(win, ORANGE, square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.flip()
        pygame.time.delay(100)
        ym +=100
        square.y=ym
    
def MainMenuWin(xm,ym):
    global MAINMENU
    global INSTRUCTIONS
    global SETTINGS
    global LEVEL1
    global LEVEL2
    global SCOREBOARD
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.fill(COLOR)
        pygame.display.set_caption("Instructions")
        display_Title("Instructions", 70)
        display_Title("Back", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        INSTRUCTIONS = True               
    if xm>=70 and xm<=95 and ym>=250 and ym<=275: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Settings")
        display_Title("SETTINGS",  70)
        Menu_function(settingMessages)
        display_Title("BACK", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        SETTINGS = True  
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Level 1")
        display_Title("Level 1",  70)
        display_Title("Back", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        LEVEL1 = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Level 2")
        display_Title("Level 2",  70)
        display_Title("Back", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=550 and ym<=575: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("ScoreBoard")
        display_Title("Scoreboard",  70)
        display_Title("Back", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=650 and ym<=675: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("Exit",  70)
        display_Title("Back", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        global run
        run=False
def SettingMenuWin(xm,ym):
    global SETTINGS
    global SCREEN
    global BACKGROUND
    global OBJECTCOLOR
   
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.fill(COLOR)
        display_Title("Screen Size", 70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        SCREEN = True  
                   
    if xm>=70 and xm<=95 and ym>=250 and ym<=275 and flag: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("BACKGROUND COLORS",  70)
        display_Title("BACK", 750)
        pygame.display.update()
        BACKGROUND = True
        SETTINGS = False             
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("OBJECT COLORS",  70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("SOUNDS",  70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True
def Menu_Back():
    win.fill(COLOR)
    display_Title("MAIN", 70)
    Menu_function(mainMenu)
    pygame.display.update()
def Setting_Back():
    win.fill(COLOR)
    display_Title("SETTINGS", 70)
    Menu_function(settingMessages)
    display_Title("Back", HEIGHT-95)
    pygame.display.update()
def Screen_size():
    pygame.time.delay(100)
    ym=ys
    screenSize.x=xs
    xm=xs
    for i in range(0,len(squaresSize)):
        squary=squaresSize[i]
        squary.x=xm
        pygame.draw.rect(win, ORANGE, squary)
        word= screenMessage[i]
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm-10,ym-40))
        pygame.display.flip()
        pygame.time.delay(100)
        xm +=200
def game_Level1():
    global fall_y
    global figx
    global figy
    global fall_x
    #win.blit(bg1, (0,0))
    pygame.display.set_caption("My game 1")
    pygame.display.flip()
    win.blit(bg, (0,0))
    win.blit(FIG, (figx, figy))
    win.blit(Fall, (fall_x,fall_y))
    fall_y +=2
    py.display.flip()
    py.time.delay(100)
    

    #add your game logic here
def end():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    end()
                return
# def Color_screen():
#     for key in colors:
#Start Program
display_Title("MENU", 40)
Menu_function(mainMenu)
run=True 
clock=pygame.time.Clock()
# C:\Users\suarezm\OneDrive - Greenhill School\Game Design\GameDesign2021_Fall_Ablock\cade.py  
while run:
    moveLeft=False
    moveRight=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == pygame.K_RIGHT:
                moveLeft = False
                moveRight = True
            if event.key == pygame.K_UP:
                moveDown = False
                moveUp = True
            if event.key == pygame.K_DOWN:
                moveUp = False
                moveDown = True
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pressed=pygame.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos=pygame.mouse.get_pos()
                print(pygame.mouse.get_pos())
                xm=mouse_pos[0]
                ym=mouse_pos[1]
        if MAINMENU:
            MainMenuWin(xm,ym)
        if INSTRUCTIONS:
            myFile=open('instructions.txt', 'r')
            yi=150
            for line in myFile.readlines():
                text=INSTRUCTIONS_FONT.render(line, 1, BLACK)
                win.blit(text, (40,yi))
                pygame.display.update()
                pygame.time.delay(100)
                yi+=50
            myFile.close()
            if xm >335 and xm<460 and ym>745 and ym<795:
                Menu_Back()
                MAINMENU = True
                INSTRUCTIONS = False
        if SETTINGS:
            SettingMenuWin(xm,ym)
            flag=True
            if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                Menu_Back()
                MAINMENU = True
                SETTINGS = False
                flag=False
        if SCREEN:
            Screen_size()
            display_Title("Back", HEIGHT-95)
            pygame.display.update()
            if xm>450 and xm <540 and ym>200 and ym<290: 
                WIDTH=600
                HEIGHT=600
                win=pygame.display.set_mode((WIDTH,HEIGHT))
                win.fill(COLOR)
                Screen_size()
                display_Title("Back", HEIGHT-95)

                pygame.display.update()
            if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                Setting_Back()
                SETTINGS = True
                SCREEN = False
            if xm >335 and xm<460 and ym>745 and ym<795:
                Setting_Back()
                SETTINGS = True
                SCREEN = False
        if BACKGROUND:
            if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                Setting_Back()
                SETTINGS = True
                BACKGROUND = False
        if OBJECTCOLOR:
            if xm >335 and xm<460 and ym>745 and ym<795:
                Setting_Back()
                SETTINGS = True
                OBJECTCOLOR = False
        if LEVEL1 :
            #play game here
            
            game_Level1()
            if moveLeft and figx >5:
                figx -=speed
                rect.x -=speed
            if moveRight and figx <WIDTH-50:
                figx +=speed
                rect.x +=speed
            eDistance = math.dist([figx, figy], [fall_x, fall_y])
            if eDistance < 50:
                LEVEL1 = False
                MAINMENU = True
                #go back to menu
            fall_y += FALLING_SPEED
            rocksquare.y +=FALLING_SPEED
            win.fill(WHITE)
            win.blit(bg, (0,0))
            py.draw.rect(win,1,rect) 
            py.draw.rect(win,1,rocksquare)
            win.blit(FIG, (figx,figy))
            win.blit(Fall, (fall_x,fall_y))
            
            if fall_y > HEIGHT:
                fall_y = 0
                fall_x= random.random()*WIDTH
                pygame.draw.rect(win,1,rocksquare)
                #check if fally hits figure y, create rect around rock rectcollidepoint 

                #make list of charecters, randomly select one, randomly select x value to change position of where the charecter appears, create moer images that will fall    
            pygame.display.flip()
            
            if xm >335 and xm<460 and ym>745 and ym<795:
                Menu_Back()
                MAINMENU = True
                LEVEL1 = False
            pygame.display.flip()
        if LEVEL2:
            #Play game
            if xm >335 and xm<460 and ym>745 and ym<795:
                Menu_Back()
                MAINMENU = True
                LEVEL2 = False
    clock.tick(30)
pygame.quit()
