import pygame
import os 

def cargar_cartas (Cartas_solitario):

    cartas = {} #Se crea un diccionario vacio para almacenar las cartas
    
    for carpeta in os.listdir(Cartas_solitario):
        
        if carpeta[-4:] == (".jpg"):

            """utilizo el slicing para verificar que la extension de la imagen sea la .jpg """

            nombre = carpeta[0:-4]

            """Saca del nombre de la imagen la extension, en este caso .jpg"""

            ruta = os.path.join(Cartas_solitario, carpeta)

            """crea la ruta de la imagen"""

            imagen = pygame.image.load(ruta)

            cartas[nombre] = pygame.transform.scale(imagen, (120, 160))

    return cartas







#profe le agrego una consulta, estuve viendo sobre algun metodo para cargar todas las imagenes sin que sea manualmente una por una y encontre esta libreria llamada os
#que ayuda a poder cargar una carpeta en vez de que cargue imagen por imagen, puedo utilizarla? o debo cargar
#de la manera de la ppt: 
#pygame.image.load("su directorio")