# Simple Animation with PyGame, Isiah Carter, 1/5/22, 8:53AM, v0.1

import pygame, sys, time
from pygame.locals import *

#Setup Pygame
pygame.init()

#Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')