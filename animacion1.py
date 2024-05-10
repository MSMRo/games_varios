# pip install pygame

import pygame
import sys
import time

pygame.init()

size = (800,540)

#crear ventana
screen = pygame.display.set_mode(size)
#controlar FPS
clock = pygame.time.Clock()

# Colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

# coordinadas
cord_x = 400
cord_y = 200

#velocidad
speed_x = 3
speed_y = 3

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    ### -- zona de dibujo

    ## - logica del juego
    if (cord_x > 720 or cord_x<0):
        speed_x *= -1
    if (cord_y >=460 or cord_y<0):
        speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y

    pygame.draw.rect(screen, GREEN, (cord_x, cord_y,80,80))
    

    ### -- zona de dibujo

    # actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
