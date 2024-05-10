import pygame, sys, time
import numpy as np
pygame.init()

# Colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coord_list = []
for i in range(60):
    x = np.random.randint(0,800)
    y = np.random.randint(0,500)

    coord_list.append([x,y])

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    ### -- zona de dibujo

    ## - logica del juego
    for coord in coord_list:
        x = coord[0]
        y = coord[1]

        pygame.draw.circle(screen, RED, (x,y), 2)        
        coord[1]+=1

        if coord[1]>=500:
            coord[1]=0
    ### -- zona de dibujo

    # actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
