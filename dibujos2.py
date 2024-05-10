# pip install pygame

import pygame
import sys
import time

pygame.init()

size = (800,540)
screen = pygame.display.set_mode(size)

# Colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    ### -- zona de dibujo
    for i in range(100,700,100):
        pygame.draw.rect(screen, BLACK, (i,100,80,80))
        pygame.draw.line(screen, RED, (i,0),(i,100),5 )

    ### -- zona de dibujo

    # actualizar pantalla
    pygame.display.flip()

