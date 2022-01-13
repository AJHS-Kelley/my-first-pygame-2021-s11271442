#PyGame Collision Practice, Ryan Kelley, January 04, 2022, 8:48am, v0.5

import pygame, sys, random
from pgame.locals import *

#Setup Pygame
pygame.init()
mainClock = pygame.time.Clock()

#Setup the Pygame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection 2022')

#Setup colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

#Setup the player and food data structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH = FOODSIZE), random.randint(0, WINDOWHEIGHT = FOODSIZE), FOODSIZE, FOODSIZE))

    #Movement Variables
    moveLeft = False
    moveRight = False
    MoveUp = False
    MoveDown = False

    MOVESPEED = 6