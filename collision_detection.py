#PyGame Collision Practice, Ryan Kelley, January 04, 2022, 8:33am, v0.2

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