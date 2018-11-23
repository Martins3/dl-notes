import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1300, 960))
pygame.display.set_caption('Hello World!')

Black = (0, 0, 0)
Red = (255, 0, 0)
White = (255, 255, 255)
DISPLAYSURF.fill(White)
pygame.draw.polygon(DISPLAYSURF, Red, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, Red, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, Red, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, Red, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, Red, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, Red, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, Red, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
for i in range(100):
    for j in range(100):
        pixObj[i][j] = Black
del pixObj

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
