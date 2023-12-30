from abc import ABC , abstractclassmethod
import pygame
import sys

class personaje(ABC):
    @abstractclassmethod
    def __init__(self,nombre,vida,daño):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
    @abstractclassmethod
    def pegar(self):
        self.vida = self.vida - self.daño

class elayer(personaje):
    def __init__(self,nombre,vida,daño):
        super().__init__(nombre,vida,daño)


class enemigo(personaje):
    def __init__(self,nombre,vida,daño):
        super().__init__(nombre,vida,daño)


        
pygame.init()#inisialisa pygame
ventana = pygame.display.set_mode((600, 400))#crea una ventana
pygame.display.set_caption('minesspearwere')

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
