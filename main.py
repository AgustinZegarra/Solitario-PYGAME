import pygame
from funciones.Graficos import *

pygame.init()



pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)


pygame.display.set_icon(icono)

pygame.display.set_caption("El Solitario")

ejecutar = True

while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    pantalla.fill (VERDECASINO)

    pygame.display.update()