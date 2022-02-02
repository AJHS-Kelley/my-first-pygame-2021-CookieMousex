# Simple Animation with PyGame, Rosemarie Staples, 2/1/22 11:54pm, v0.1

import pygame, sys, time
from pygame.locals import *

# Setup Pygame
pygame.init()

#Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')
