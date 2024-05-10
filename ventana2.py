# pip install pygame

import pygame
import sys
import time

pygame.init()

size = (480,340)
screen = pygame.display.set_mode(size)

# Colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    ### -- zona de dibujo
    pygame.draw.line(screen, GREEN, [0,100], [200,300], 5)

    ### -- zona de dibujo

    # actualizar pantalla
    pygame.display.flip()


