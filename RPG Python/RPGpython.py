from abc import ABC , abstractclassmethod
import pygame
import sys
from pygame.locals import *


WHITE = (255,255,255)
GREEN = (0,255,93)
BLUE = (0,39,255)
RED = (255,0,0)
BLACK = (0,0,0)


def main():
    pass


pygame.init
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("RPG game")

window.fill(WHITE)

rectangulo1 = pygame.draw.rect(window, RED, (300, 100, 100, 50))
print(rectangulo1)


linea1 = pygame.draw.line(window,GREEN, (600,600) , (0,0), 10)
print(linea1)

circulo = pygame.draw.circle(window,BLACK, (300,300), 100, 10)
print(circulo)

elipse = pygame.draw.ellipse(window,BLACK, (100,100,40,80), 10)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

