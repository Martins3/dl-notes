import pygame, sys, os
from pygame.locals import *
source = "/home/martin/AllWorkStation/Atom/learnPython/pygame/source"
cat = os.path.join(source, "cat.png")
pygame.init()

FPS = 40 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((600, 900), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
catImg = pygame.image.load(cat)
catx = 10
caty = 10
direction = 'right'

fontobj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontobj.render("gan", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (100, 150)

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
