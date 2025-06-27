import pygame
import pygame.mixer as mixer
from paquete.Graficos import *
from funciones.cargar_cartas import cargar_cartas
from funciones.mostrar_cartas import mostrar_cartas

pygame.init()

mixer.init()

mixer.music.load("Solitario/Multimedia/Casino Jazz - New York Jazz Lounge.mp3")

mixer.music.set_volume(0.1)

mixer.music.play()

pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)

pygame.display.set_icon(icono)

pygame.display.set_caption("El Solitario")

cartas = cargar_cartas("Solitario/Cartas_solitario")

ejecutar = True

print (cartas.keys())

while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    pantalla.fill (VERDECASINO)

    mostrar_cartas(pantalla, cartas)

    pygame.display.update()

    
    
    
    
    
    
    
    
    
    
    
    
    # pantalla.blit(cartas["1 de basto"], (100, 100))
    # pantalla.blit(cartas["1 de copa"], (200, 100))
    # pantalla.blit(cartas["1 de espada"], (300, 100))
    # pantalla.blit(cartas["1 de oro"], (400, 100))
    
