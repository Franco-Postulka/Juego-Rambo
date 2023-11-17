import pygame as py
from pygame.locals import *
from os import system
system("cls")
from modulos.Configuraciones import *
from modulos.Class_heroe import Heroe
from modulos.Class_enemigo import Enemigo
from modulos.Class_proyectil import*
from modulos.Class_plataforma import Plataforma
from modulos.Class_item import Item
from Modo import *
import time
import random
from config import Config

from config import Config
import pygame as py

class Game(Config):
    def __init__(self, size, FPS, caption="Title", icon=""):
        super().__init__(size, FPS, caption, icon)
        self.x = size[0]
        self.y = size[1]
        # ... (otras configuraciones específicas del juego)

    def manejar_eventos(self):
        # Tu lógica para manejar eventos aquí
        pass

    def actualizar_elementos(self):
        # Lógica para actualizar elementos del juego (personajes, balas, enemigos, etc.)
        # ...
        pass


    def dibujar_elementos(self):
        # Lógica para dibujar elementos del juego en la pantalla
        # ...
        pass

    @staticmethod
    def crear_bomba(diccionario_animaciones_bomba, lista_bombas):
        tiempo_actual_bomba = py.time.get_ticks() / 1000  # Obtiene el tiempo actual en segundos
        tiempo_transcurrido_bomba = tiempo_actual_bomba - Game.tiempo_ultimo_bomba

        if tiempo_transcurrido_bomba >= Game.intervalo_bomba:
            posicion_x = random.randrange(0, Game.y)
            posicion_y = random.randrange(-100, -40)
            bomba = Bomba(diccionario_animaciones_bomba, posicion_x, posicion_y)
            lista_bombas.append(bomba)
            Game.tiempo_ultimo_bomba = tiempo_actual_bomba

    def run(self):
        flag = True
        while flag:
            self.clock.tick(self.FPS)
            flag = self.manejar_eventos()

            self.fill_screen()  # Utilizando el método de Config para dibujar el fondo

            self.actualizar_elementos()
            self.dibujar_elementos()

            py.display.update()

        py.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
