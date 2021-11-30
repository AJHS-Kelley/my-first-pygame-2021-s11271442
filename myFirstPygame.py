# My First PyGame, Isiah Carter, 11/30/21, 2:25PM, v0.2

import pygame, sys
from pygame.locals import *

# Start Pygame
pygame.init()

# Setup the game window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')