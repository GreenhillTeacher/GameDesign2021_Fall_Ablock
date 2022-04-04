import math
import pygame

class SpriteRotate(pygame.sprite.Sprite):

    def __init__(self, imageName, origin, pivot):
        super().__init__() 
        self.image = pygame.image.load(imageName)
        self.original_image = self.image
        self.rect = self.image.get_rect(topleft = (origin[0]-pivot[0], origin[1]-pivot[1]))
        self.origin = origin
        self.pivot = pivot
        self.angle = 0

    def update(self):
        
        # offset from pivot to center
        image_rect = self.original_image.get_rect(topleft = (self.origin[0] - self.pivot[0], self.origin[1]-self.pivot[1]))
        offset_center_to_pivot = pygame.math.Vector2(self.origin) - image_rect.center
        
        # roatated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-self.angle)

        # roatetd image center
        rotated_image_center = (self.pos[0] - rotated_offset.x, self.pos[1] - rotated_offset.y)

        # get a rotated image
        self.image  = pygame.transform.rotate(self.original_image, self.angle)
        self.rect   = self.image.get_rect(center = rotated_image_center)
        self.angle += 10
  
pygame.init()
size = (400,400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

boomerang = SpriteRotate('Pygame-Tutorials-master\Game\standing.png', (200, 200), (48, 21))
all_sprites = pygame.sprite.Group(boomerang)

frame = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pos = (200 + math.cos(frame * 0.05)*100, 200 + math.sin(frame * 0.05)*50)
    boomerang.pos = pos
    all_sprites.update()

    screen.fill(0)
    
    all_sprites.draw(screen)
    #pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
    #pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
    #pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

    pygame.display.flip()
    frame += 1
    
pygame.quit()
exit()