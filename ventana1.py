# pip install pygame

import pygame
import sys
import time

pygame.init()

size = (480,340)
screen = pygame.display.set_mode(size)


while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()


