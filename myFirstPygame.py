# My First PyGame, Isiah Carter, 11/30/21, 2:34PM, v0.3

import pygame, sys
from pygame.locals import *

# Start Pygame
pygame.init()

# Setup the game window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup color values.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)