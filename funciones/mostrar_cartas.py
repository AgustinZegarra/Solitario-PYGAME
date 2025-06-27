def mostrar_cartas(pantalla, cartas, x_inicial=50, y_inicial=100, cartas_por_fila=10, separacion_x=130, separacion_y=170):
    
    lista_de_cartas = list(cartas.values())  

    """CREAMOS UNA LISTA CON LAS CARTAS"""

    for filas in range((len(lista_de_cartas) + cartas_por_fila - 1) // cartas_por_fila):
        
        """CALCULAMOS LAS FILAS QUE NECESITAMOS PARA MOSTRAR TODAS LAS CARTAS"""

        for columna in range(cartas_por_fila):

            indice = filas * cartas_por_fila + columna

            if indice >= len(lista_de_cartas):

                break                        

            x = x_inicial + columna * separacion_x

            y = y_inicial + filas * separacion_y

            """CALCULAMOS LA POSICION QUE VA A TENER LA CARTA EN PANTALLA"""

            pantalla.blit(lista_de_cartas[indice], (x, y))
