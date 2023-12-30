import pygame
import sys

ROJO = (255, 0, 0) 
VERDE = (0, 255, 0) 
AZUL = (0, 0, 255)

pygame.init()#inisialisa pygame

ventana = pygame.display.set_mode((600, 400))#crea una ventana

ventana2 = pygame.display.set_mode((600, 400))#crea una ventana

pygame.display.set_caption('minesspearwere')

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
