import pygame as py
from pygame.locals import *
from os import system
system("cls")
from modulos.Imagenes import *
from modulos.Elementos.Class_heroe import Heroe
from modulos.Elementos.Class_enemigo import Enemigo
from modulos.Elementos.Class_proyectil import*
from modulos.Elementos.Class_plataforma import Plataforma
from modulos.Elementos.Class_item import Item
from modulos.Elementos.Class_puerta import Puerta
from modulos.Modo import*
from modulos.animaciones import*
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
        self.FPS = FPS
        self.RELOJ = py.time.Clock()
        self.set_background_image(fondo)
        self.screen = py.display.set_mode(self.size)
        self.lista_balas_heroe = []
        self.lista_balas_enemigo = []
        self.lista_bombas = []
        self.intervalo_bomba = 2
        self.intervalo_disparo = 1
        self.tiempo_ultimo_bomba = 0
        self.tiempo_ultimo_disparo = 0
        self.set_heroe()
        self.set_enemigo()
        self.set_plataformas()
        self.set_item()
        self.set_puerta()
        self.disparo = False
        self.running = True

    def set_plataformas(self):
        piso = Plataforma(False, (W, 135), 0, H-70)
        plataforma_roca_grande = Plataforma(False, (200, 20), 140, H-170)
        plataforma_roca_chica = Plataforma(False, (35, 20), 850, H-175)
        plataforma_roca_flotante = Plataforma(True, (250, 10), 380, H-280, plataforma_1,(350, H-300))
        plataforma_roca_flotante2 = Plataforma(True, (250, 10), 730, H-380, plataforma_2,(700, H-400))
        plataforma_roca_flotante3 = Plataforma(True, (180, 10), 45, H-380, plataforma_3,(25, H-400))
        self.plataformas = [piso, plataforma_roca_grande, plataforma_roca_chica, plataforma_roca_flotante,plataforma_roca_flotante2,plataforma_roca_flotante3]

    def set_item(self):
        reescalar_imagenes(diccionario_llaves, 30,30)
        llave = Item(diccionario_llaves,150,self.y -460)
        self.lista_llave = [llave]
    
    def set_puerta(self):
        reescalar_imagenes(diccionario_puertas, 160,195)
        puerta = Puerta(diccionario_puertas,1050,self.y-265)
        self.puerta = puerta

    def set_enemigo(self):
        self.enemigo =  Enemigo(diccionario_animaciones_enemigo,100,0.35,(120,150),900,470,5)

    def set_heroe(self):
        reescalar_imagenes(diccionario_rambo, 120,150)
        self.heroe = Heroe(diccionario_rambo,100,0.5,(120,150),600,500,10)

    def move_heroe(self):
        teclas = py.key.get_pressed()
        if teclas[py.K_d]:
            self.heroe.que_hace = "Derecha"
        elif teclas[py.K_a]:
            self.heroe.que_hace = "Izquierda"
        elif(teclas[py.K_w]):
            self.heroe.que_hace = "Salta"
        else:
            self.heroe.que_hace = "inicial"

    def fill_screen(self, color=None):
        if color != None:
            self.screen.fill(color)
        else:
            self.screen.blit(self.background_image, (0, 0))

    
    def crear_bomba(self):
        tiempo_actual_bomba = py.time.get_ticks() / 1000  # Obtiene el tiempo actual en segundos
        tiempo_transcurrido_bomba = tiempo_actual_bomba - self.tiempo_ultimo_bomba

        if tiempo_transcurrido_bomba >= self.intervalo_bomba:
            posicion_x = random.randrange(0, self.y)
            posicion_y = random.randrange(-100, -40)
            bomba = Bomba(diccionario_animaciones_bomba, posicion_x, posicion_y)
            self.lista_bombas.append(bomba)
            self.tiempo_ultimo_bomba = tiempo_actual_bomba

    def crear_bala_enemigo(self):
        if self.enemigo.esta_muerto == False and self.enemigo.zona_tiro == True:
                tiempo_actual = time.time()
                tiempo_transcurrido = tiempo_actual - self.tiempo_ultimo_disparo
                if tiempo_transcurrido >= self.intervalo_disparo:
                    bala = Bala(diccionario_animaciones_bala,self.heroe.rectangulo_principal.x,self.enemigo.rectangulo_principal.x,self.enemigo.rectangulo_principal.y + 50)
                    if bala.direccion_x >= self.enemigo.rectangulo_principal.x:
                            bala.rectangulo_principal.x += 120
                    self.lista_balas_enemigo.append(bala)
                    self.tiempo_ultimo_disparo = tiempo_actual

    def manejar_eventos(self):
        for event in py.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == MOUSEBUTTONDOWN:
                    self.heroe.disparar(diccionario_animaciones_bala,event.pos[0],self.lista_balas_heroe)
                    self.disparo = True
                elif event.type == KEYDOWN:
                    if event.key == K_TAB:
                        cambiar_modo()

    def actualizar_elementos(self):
        for plataforma in self.plataformas:
                plataforma.blit(self.screen)
        self.heroe.actualizar(self.screen, self.plataformas)
        self.enemigo.actualizar(self.screen,self.heroe)
        Bomba.actualizar_bomba(self.lista_bombas,self.screen,self.y)
        self.heroe.colisionar_bombas(self.lista_bombas,diccionario_animaciones_bomba,self.screen)

        if self.disparo == True:
            Bala.actualizar_balas(self.lista_balas_heroe,self.screen,self.x)
            Enemigo.verificar_muerte(self.enemigo,diccionario_animaciones_enemigo,self.screen,self.heroe,self.lista_balas_heroe)
        
        self.crear_bala_enemigo()
        Bala.actualizar_balas(self.lista_balas_enemigo,self.screen,self.x)
        self.heroe.colisionar_balas(self.lista_balas_enemigo)
        Item.actualizar_items(self.lista_llave,self.screen)
        self.heroe.agarrar_elementos(self.lista_llave,self.puerta)
            
    def dibujar_rectangulos(self):
        if obtener_modo():
            py.draw.rect(self.screen, "blue", self.heroe.rectangulo_principal,3)
            py.draw.rect(self.screen, "blue", self.heroe.smaller_rect,3)

            py.draw.rect(self.screen, "red", self.enemigo.rectangulo_principal,3)

            for plataforma in self.plataformas:
                py.draw.rect(self.screen, "red", plataforma.rect, 3)
        pass

    def run(self):
        py.init()
        while self.running:
            self.RELOJ.tick(self.FPS)
            self.manejar_eventos()
            self.move_heroe()
            self.fill_screen()
            self.crear_bomba()
            ###parte a agregarle funcioonalidad
            # for i in range(len(diccionario_puertas)):
            #     self.screen.blit(diccionario_puertas["quieto"][i],(1050,self.y-220))
            self.puerta.animar(self.screen)
            self.actualizar_elementos()
            self.dibujar_rectangulos()
            py.display.update()
            py.display.flip()

        py.quit()
