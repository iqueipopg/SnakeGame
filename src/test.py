import pygame
import funciones as f
import objetos as ob

COLOR_VERDE = "\033[1;32m"
COLOR_ROJO = "\033[1;31m"
COLOR_DEFECTO = "\033[0m"

OK = COLOR_VERDE + "OK" + COLOR_DEFECTO
ERROR = COLOR_ROJO + "ERROR" + COLOR_DEFECTO

### necesarios para el test
pygame.init()
serpiente = ob.serp()
manzana1 = ob.fruta()
manzana2 = ob.fruta()
fps = pygame.time.Clock()
s_game_over = pygame.mixer.Sound('extras\sonidos\game_over.mp3')
s_victoria = pygame.mixer.Sound('extras\sonidos\win.mp3')


print(f"Ejecutando tests....\n")
try:
    print(f"-   Función pantalla: ", end = "") 
    VENTANA = f.pantalla()
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Función check objeto w/ serpiente: ", end = "") 
    f.check_objwserp(serpiente, manzana1)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Función check objeto w/ objeto: ", end = "") 
    f.check_objwobj(manzana1, manzana2)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Función power up azul: ", end = "") 
    f.power_up_azul(2, fps)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Función pop rosa: ", end = "") 
    f.pop_rosa([1,2,3,4])
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Función lista morado: ", end = "") 
    f.lista_morado([1,2,3,4], serpiente)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Función fin: ", end = "") 
    f.fin(True, False, s_game_over, s_victoria, VENTANA)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Función draw cuadrícula: ", end = "") 
    f.draw_cuadricula(VENTANA)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Función pantalla instrucciones: ", end = "") 
    f.pantalla_instrucciones(VENTANA)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Función pantalla inicio: ", end = "") 
    f.pantalla_inicio(VENTANA)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Funciones del objeto serpiente: ", end = "") 
    serpiente.dibujar()
    serpiente.mover()
    serpiente.arriba()
    serpiente.abajo()
    serpiente.derecha()
    serpiente.izquierda()
    serpiente.morir()
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print(f"-   Funcies del objeto fruta: ", end = "") 
    manzana1.dibujar_rojo()
    manzana1.dibujar_morado()
    manzana1.dibujar_azul()
    manzana1.dibujar_naranja()
    manzana1.dibujar_rosa()
    manzana1.aparecer()
    manzana1.comer(serpiente)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

print(f"\nFin de los tests")