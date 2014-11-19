import pygame, sys,
from Player import *
from Object import *
from Powerup import *

pygame.init()

clock = pygame.time.Clock

width = 100
height = 800
size = width, height

screen = pygame.display.set_mode(size)

player1 = Player()
player2 = Player()

