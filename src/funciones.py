import pygame
from pygame import Vector2
import random
import objetos as ob

ALTO = 480
ANCHO = 720
def pantalla(): # -> Surface
    '''
    Crea la pantalla donde se desarrolla todo el juego.
    '''
    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    return VENTANA

def check_objwserp(serpiente: object, objeto: object) -> bool:
    '''
    Informa si el objeto generado se encuentra en la posición de la serpiente.

    Return:
        - booleano (bool): True si está en la serpiente.
    '''
    for bloque in serpiente.cuerpo:   # para que en caso de que se genere una manzana en el cuerpo de la serpiente, se genere otra
            if bloque == objeto.posicion:
                objeto.aparecer()

def check_objwobj(objeto1: object, objeto2: object) -> None:
    '''
    Cambia la posición del segundo objeto si comparten posición.
    '''
    if objeto1.posicion == objeto2.posicion:
        objeto2.aparecer()

def power_up_azul(cont_azul: int, fps: object) -> None:
    '''
    Ralentiza durante 3 turnos si la manzana azul es comida.
    '''
    if cont_azul > 2:
        fps.tick(30)
    if cont_azul <= 2:
        fps.tick(20)

def pop_rosa(lista: list) -> list:
    '''
    Elimina un objeto de la lista proporcionada de forma aleatoria.
    '''
    lista_popped = []
    indice = random.randint(0, len(lista)-1)
    elemento_extraido = lista[indice]
    for i in range(len(lista)):
        if lista[i] != elemento_extraido:
            lista_popped.append(lista[i])
    return lista_popped

def lista_morado(lista_manzanas_moradas: list, serpiente: object) -> list:
    '''
    Crea una nueva lista igual que la anterior pero con un nuevo objeto.
    '''
    lista_manzanas_moradas_copy = lista_manzanas_moradas.copy()
    manzana_morada = ob.fruta()
    if check_objwserp(serpiente, manzana_morada):
        manzana_morada.aparecer()
    lista_manzanas_moradas_copy.append(manzana_morada)
    lista_manzanas_moradas = lista_manzanas_moradas_copy.copy()
    return lista_manzanas_moradas

def fin(game_over: bool, win:bool, sonido1: object, sonido2: object, VENTANA: object) -> None:
    '''
    Muestra la pantalla de victoria o game over según el jugador gana o pierde.
    '''
    draw_cuadricula(VENTANA)
    titulo = pygame.font.Font('extras\letra.ttf', 40)
    press = pygame.font.Font('extras\letra.ttf', 10)
    texto_press = press.render('Press space bar and try again', 1 ,(30, 33, 27))
    if win:
        game_over = False  # para que no me salte cuando la serpiente llegue a la pared
        texto_titulo = titulo.render('VICTORY', 1, (30, 33, 27))
        VENTANA.blit(texto_titulo, (500-texto_titulo.get_width()-10, 190))
        sonido1.play()
    if game_over:
        texto_titulo = titulo.render('GAME OVER', 1, (30, 33, 27))
        VENTANA.blit(texto_titulo, (550-texto_titulo.get_width()-10, 190))
        sonido2.play()
    VENTANA.blit(texto_press, (500-texto_press.get_width()-10, 400))

def draw_cuadricula(VENTANA: object):   # funcion que crea las lineas verticales y horizontales
    '''
    Crea la cuadícula del juego.
    '''
    VENTANA.fill((211, 255, 152))
    range_x = int(ALTO/10)
    range_y = int(ANCHO/10)
    # i filas, j columnas
    for i in range(range_x+1):
        pygame.draw.line(VENTANA, (176, 220, 116), (0, i*10-5), (ANCHO, i*10-5))  # lineas horizontales
        for j in range(range_y):
            pygame.draw.line(VENTANA, (176, 220, 116), (j*10-5, 0), (j*10-5, ALTO))  # lineas verticales

def pantalla_inicio(VENTANA: object) -> None:
    '''
    Muestra la pantalla de inicio.
    '''
    draw_cuadricula(VENTANA)
    titulo = pygame.font.Font('extras\letra.ttf', 40)
    press = pygame.font.Font('extras\letra.ttf', 10)
    texto_titulo = titulo.render('SNAKE GAME', 1, (30, 33, 27))
    texto_bar = press.render('Press space bar to start', 1 ,(30, 33, 27))
    texto_key = press.render('Press enter for instructions', 1, (30, 33, 27))
    VENTANA.blit(texto_titulo, (570-texto_titulo.get_width()-10, 190))
    VENTANA.blit(texto_key, (498-texto_key.get_width()-10, 370))
    VENTANA.blit(texto_bar, (475-texto_bar.get_width()-10, 400))

def pantalla_instrucciones(VENTANA: object) -> None:
    '''
    Muestra la pantalla de instrucciones.
    '''
    draw_cuadricula(VENTANA)
    cont = 150
    press = pygame.font.Font('extras\letra.ttf', 10)
    with open('instrucciones.txt', encoding = 'utf-8') as instrucciones:
        while cont < 150 + 160:
            linea = instrucciones.readline().rstrip()
            texto = press.render(linea, 1, (30, 33, 27))
            VENTANA.blit(texto, (80, cont))
            cont += 15
    pygame.display.update()