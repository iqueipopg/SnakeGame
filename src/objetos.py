import pygame
import funciones as f
from pygame import Vector2  # representa vectores con coord x e y
import random

ALTO = 480
ANCHO = 720
VENTANA = pygame.display.set_mode((ANCHO, ALTO))


class serp:
    def __init__(self) -> None:
        self.cuerpo = [Vector2(300, 200), Vector2(300, 210), Vector2(300, 220)]
        self.dir = Vector2(0, -10)
        self.booleano_serp = False

    def dibujar(self) -> None:
        """
        Dibuja la serpiente en la pantalla.
        """
        for bloque in self.cuerpo:
            # pygame.draw.rect(VENTANA, (78, 118, 27), (bloque.x, bloque.y, 10, 10))
            pygame.draw.circle(VENTANA, (78, 118, 27), (bloque.x, bloque.y), 5)

    def mover(self) -> None:
        """
        Se encarga del movimiento de la serpiente. Va a tomar todos los valores del cuerpo salvo el último
        y los va a adelantar una posición de manera que cada bloque del cuerpo avanza a la posición del
        anterior en cada movimiento.
        """
        if (
            self.booleano_serp == True
        ):  # se convierte en True en la función de comer del objeto fruta
            # copio la lista con las posiciones de todos los bloques del cuerpo
            cuerpo_copy = self.cuerpo
            # inserto en el elemento 0 de la lista la nueva posición de la serpiente
            cuerpo_copy.insert(0, cuerpo_copy[0] + self.dir)
            # actualizo el cuerpo de la serpiente
            self.cuerpo = cuerpo_copy
            self.booleano_serp = False
        else:
            cuerpo_copy = self.cuerpo[:-1]
            cuerpo_copy.insert(0, cuerpo_copy[0] + self.dir)
            self.cuerpo = cuerpo_copy

    def arriba(self) -> None:
        """
        Mueve la serpiente hacia arriba.
        """
        self.dir = Vector2(0, -10)

    def abajo(self) -> None:
        """
        Mueve la serpiente hacia abajo.
        """
        self.dir = Vector2(0, 10)

    def derecha(self) -> None:
        """
        Mueve la serpiente hacia la derecha.
        """
        self.dir = Vector2(10, 0)

    def izquierda(self) -> None:
        """
        Mueve la serpiente hacia la izquierda.
        """
        self.dir = Vector2(-10, 0)

    def morir(self) -> bool:
        """
        Función para detrminar la muerte de la serpiente. Morirá en caso de que la cabeza toque los finales de la ventana o
        en caso de que toque su propio cuerpo.

        Return:
            - booleano (bool): True en caso de que muera.
        """
        ALTO = 480
        ANCHO = 720
        booleano = False
        # self.cuerpo[0] es el primer elemento de la lista de manera que es la cabeza de la serpiente
        if (
            self.cuerpo[0].x >= ANCHO + 10
            or self.cuerpo[0].y >= ALTO + 10
            or self.cuerpo[0].x <= -10
            or self.cuerpo[0].y <= -10
        ):
            booleano = True

        for bloque in self.cuerpo[1:]:  # quitamos el elemento 0 que es la cabeza
            if self.cuerpo[0] == bloque:
                booleano = True
        return booleano


class fruta:
    def __init__(self) -> None:
        self.aparecer()

    def dibujar_rojo(self) -> None:
        """
        Dibuja la manzana roja en pantalla.
        """
        pygame.draw.circle(VENTANA, (255, 0, 0), (self.posicion.x, self.posicion.y), 5)

    def dibujar_morado(self) -> None:
        """
        Dibuja la manzana morada en pantalla.
        """
        pygame.draw.circle(
            VENTANA, (170, 12, 249), (self.posicion.x, self.posicion.y), 5
        )

    def dibujar_azul(self) -> None:
        """
        Dibuja la manzana azul en pantalla.
        """
        pygame.draw.circle(
            VENTANA, (0, 120, 255), (self.posicion.x, self.posicion.y), 5
        )

    def dibujar_naranja(self) -> None:
        """
        Dibuja la manzana naranja en pantalla.
        """
        pygame.draw.circle(
            VENTANA, (252, 200, 6), (self.posicion.x, self.posicion.y), 5
        )

    def dibujar_rosa(self) -> None:
        """
        Dibuja la manzana rosa en pantalla.
        """
        pygame.draw.circle(
            VENTANA, (254, 134, 248), (self.posicion.x, self.posicion.y), 5
        )

    def aparecer(self) -> None:
        """
        Da una posición aleatoria a la manzana dentro de los límites de la pantalla.
        """
        ALTO = 480
        ANCHO = 720
        # divido y multiplico para que sea multiplo de 10 que es el tamaño de la serpiente
        self.x = random.randint(1, (ANCHO // 10) - 10)
        self.y = random.randint(1, (ALTO // 10) - 10)
        self.posicion = Vector2(self.x * 10, self.y * 10)

    def comer(self, serpiente: object) -> bool:
        """
        Verifica que la manzana ha sido comida.

        Return:
            - booleano (bool): True si ha sido comida.
        """
        booleano = False
        if serpiente.cuerpo[0] == self.posicion:
            serpiente.booleano_serp = True
            booleano = True
        return booleano
