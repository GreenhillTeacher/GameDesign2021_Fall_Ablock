import pygame as py, random
py.init()
width=700
height=600
# win = py.display.set_mode((width, height))
colors={'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,255), 'purple': (150,0,150), 'white': (255,255,255), 'black': (0,0,0), 'navy': (0,80,128), 'hot pink': (255,105,180), 'orange': (255,165,0), 'yellow': (255,240,31)}
myColor = colors.get('purple')
ColorList = ['red', 'green', 'blue', 'white','purple', 'white', 'black', 'navy', 'hot pink', 'orange']
randColor = random.choice(ColorList)
BG1=py.image.load('Images\\realimagelevel1.jpg')
clock = py.time.Clock()
run=True
guyx=200
guyy=300
speed=40
wbox=64
hbox=64
Left= False
Right= False
WalkCount=0
char=py.image.load('Images\pigdownreal1-removebg-preview10.png')
screen = py.display.set_mode((width, height))
screen.blit(char, (guyx, guyy))
walkRight=[py.image.load('Images\pigright1-removebg-preview.png'),py.image.load('Images\pigright2-removebg-preview.png'), py.image.load('Images\pigright3-removebg-preview.png')]
walkLeft=[py.image.load('Images\pigleftreal1-removebg-preview.png'), py.image.load('Images\pigleftreal2-removebg-preview.png'), py.image.load('Images\pigleftreal3-removebg-preview.png')]
applex=400
appley=600
apple=py.image.load('Images\\apple-removebg-preview.png')
screen = py.display.set_mode((width, height))
COUNT = 12
jumpCount = COUNT
Jump = False
Left = False
Right = False


def redrawGameWindow():
    global WalkCount
    screen.blit(BG1,(0,0))
    if WalkCount +1 >= 9:
        WalkCount = 0

    if Left:
        screen.blit(walkLeft[WalkCount//3], (guyx,guyy))
        WalkCount += 1
    elif Right:
        screen.blit(walkRight[WalkCount//3], (guyx,guyy))
        WalkCount += 1
    else:
        screen.blit(char, (guyx,guyy))

    py.display.flip()
    py.time.delay(100)
    # screen.fill((0,0,0))
    
    # py.display.update()

run=True
while run:
    clock.tick(9)
    for eve in py.event.get():
        if eve.type ==py.QUIT:
            run=False
    screen.blit(BG1, (0,0))
    py.display.set_caption("My Game")
    py.display.flip()
    py.time.delay(100)
    screen.blit(apple, (applex, appley))
    

#the pig is able to move around
    keyPressed= py.key.get_pressed()
    
    if keyPressed[py.K_LEFT] and guyx > speed:
         guyx -= speed
         Left= True
         Right= False
         
    elif keyPressed[py.K_RIGHT] and guyx < width- speed:
         guyx += speed
         Right = True
         Left = False
    else:
        Right= False
        Left = False
        WalkCount= 0

        
    # screen.blit(char,(guyx, guyy))
    # py.display.flip()

    if not Jump:
        if keyPressed[py.K_SPACE]:
            Jump = True
            Right = False
            Left = False
            WalkCount = 0
    else:
        if jumpCount>=-COUNT:
            guyy-= jumpCount*abs(jumpCount)/2
            jumpCount -=1

        else:
            jumpCount=COUNT
            Jump=False
    redrawGameWindow()
