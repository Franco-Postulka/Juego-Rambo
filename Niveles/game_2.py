import pygame as py
from pygame.locals import *
from os import system
system("cls")
from modulos.Imagenes import *
from modulos.sonidos import* 
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
import sqlite3
from Niveles.game_3 import Game_3

py.init()
py.font.init()

class Game_2(Config):
    def __init__(self, size, FPS, caption="Title", icon=""):
        super().__init__(size, FPS, caption, icon)
        self.x = size[0]
        self.y = size[1]
        self.FPS = FPS
        self.RELOJ = py.time.Clock()
        self.set_background_image(fondo_level_2)
        self.screen = py.display.set_mode(self.size)
        self.lista_balas_heroe = []
        self.lista_balas_enemigo = []
        self.lista_shurikens = []
        self.intervalo_shuriken = 1
        self.intervalo_apuñalada = 1.5
        self.tiempo_ultimo_bomba = 0
        self.tiempo_ultima_apuñalada = 0
        self.set_heroe()
        self.set_enemigo()
        self.set_plataformas()
        self.set_llave()
        self.set_puerta()
        self.set_moneda()
        self.disparo = False
        self.running = True
        self.score = 0
        self.tiempo_finalizacion = None
        self.font = self.font = py.font.SysFont("Roboto", 36)
        self.tiempo_inicio = py.time.get_ticks()
        self.tiempo_tardado = 0
        self.tiempor_anterior = 0
        self.tiempo_nivel = 60
        # self.jugador = jugador

    def bajar_timer(self):
        self.tiempor_anterior = self.tiempo_inicio
        self.tiempo_inicio = py.time.get_ticks()
        self.tiempo_tardado += self.tiempo_inicio/1000 - self.tiempor_anterior/1000
        self.tiempo_nivel -= self.tiempo_inicio/1000 - self.tiempor_anterior/1000
        rendered_text = self.font.render(f"00: {round(self.tiempo_nivel)}", True, (255,255,255))
        self.screen.blit(rendered_text, (self.x//2-40,20))
        if self.tiempo_tardado >= 60:
            self.running = False
    
    def actualizar_score(self):
        self.score = self.heroe.score + self.enemigo.score + self.enemigo_2.score
        rendered_text = self.font.render(f"Score: {self.score}", True, (255,255,255))
        self.screen.blit(rendered_text, (self.x-150,20))

    def verificar_fin_juego(self):
        if self.heroe.vida <= 0 :
            self.music.stop()
            game = Game_3((1200, 680), 18)
            game.set_caption('Nivel 2')
            game.set_music(sonido_fondo_mago)
            game.set_volume(0.1)
            game.play_music()
            game.run()
            # self.running = False
        elif self.puerta.animacion_actual == diccionario_puertas["final"] and self.puerta.rectangulo_principal.colliderect(self.heroe.smaller_rect):
            if self.tiempo_finalizacion is None:
                self.tiempo_finalizacion = time.time()
            else:
                # Si ya se estableció el tiempo, verifica si han pasado 2 segundos
                tiempo_transcurrido = time.time() - self.tiempo_finalizacion
                if tiempo_transcurrido >= 2:  # Cambia este valor por el tiempo deseado
                    # self.guardar_db("score.db")
                    self.music.stop()
                    game = Game_3((1200, 680), 18)
                    game.set_caption('Nivel 2')
                    game.set_music(sonido_fondo_mago)
                    game.set_volume(0.1)
                    game.play_music()
                    game.run()
                    # self.running = False

    def guardar_db(self,path):
        with sqlite3.connect(path) as conexion:
            try:
                cursor = conexion.cursor() #cursor es un objeto que permite ejecutar comandos SQL y manejar los resultados
                # Verificar si la tabla 'Jugadores' existe en sqlite_master
                cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='Jugadores' ''')
                tabla_existe = cursor.fetchone() ## fetchone devuelve None si no enu¿cuentra la table 
                if tabla_existe:
                    print("La tabla 'Jugadores' ya existe en la base de datos")
                else:
                    # Si la tabla no existe, se crea
                    sentencia = '''
                        create table Jugadores
                        (
                            id integer primary key autoincrement,
                            nombre text,
                            score integer
                        )
                        '''
                    conexion.execute(sentencia)
                    print("Tabla 'Jugadores' creada con éxito")
            except Exception as e:
                print("Error:", e)
            try:
                sentencia = '''
                insert into Jugadores(nombre,score) values (?,?)
                '''
                conexion.execute(sentencia,("Franco", self.score))
                print("tabla completada")
            except Exception as e:
                print("Error:", e)

    def set_plataformas(self):
        piso = Plataforma(False, (self.x, 135), 0, self.y-65)
        plataforma = Plataforma(True, (200, 10), 380,  self.y-260, plataforma_base,(350,  self.y-270))
        otra_plataforma = Plataforma(True, (200, 10), 580,  self.y-260, plataforma_base,(550,  self.y-270))
        otra_plataforma_2 = Plataforma(True, (230, 10), 780,  self.y-260, plataforma_base,(780,  self.y-270))

        otra_plataforma_3 = Plataforma(True, (200, 10), 0,  self.y-440, plataforma_base,(-10,  self.y-450))
        otra_plataforma_4 = Plataforma(True, (200, 10), 200,  self.y-440, plataforma_base,(150,  self.y-450))

        plataforma_barril = Plataforma(True, (50, 10), 1100,  self.y-180, barril,(1070,  self.y-200))
        plataforma_barri2 = Plataforma(True, (50, 10), 470,  self.y-370, barril,(440,  self.y-390))
        self.plataformas = [plataforma_barril,plataforma_barri2, piso,plataforma,otra_plataforma,otra_plataforma_2,otra_plataforma_3,otra_plataforma_4]

    def set_enemigo(self):
        self.enemigo =  Enemigo(diccionario_animaciones_ninja,100,0.35,(120,150),900,self.y -410 , 7,340,self.x -200)
        self.enemigo_2 =  Enemigo(diccionario_animaciones_ninja,100,0.35,(120,150),100,85,7,0,390)
        self.lista_enemigos = [self.enemigo,self.enemigo_2]

    def set_llave(self):
        reescalar_imagenes(diccionario_llaves, 30,30)
        llave = Item(diccionario_llaves,80,self.y -520)
        self.lista_llave = [llave]
    
    def set_moneda(self):
        reescalar_imagenes(diccionario_monedas, 20,20)
        moneda1 = Item(diccionario_monedas,750,self.y-150)
        moneda2 = Item(diccionario_monedas,790,self.y-150)
        moneda3 = Item(diccionario_monedas,830,self.y-150)

        moneda4 = Item(diccionario_monedas,self.x-85,self.y-250)

        moneda5 = Item(diccionario_monedas,250,self.y-150)
        moneda6 = Item(diccionario_monedas,280,self.y-150)
        # moneda7 = Item(diccionario_monedas,self.x-520,self.y-150)

        moneda8 = Item(diccionario_monedas,self.x-800,self.y-350)
        moneda9 = Item(diccionario_monedas,self.x-830,self.y-350)

        moneda10 = Item(diccionario_monedas,self.x-500,self.y-350)
        moneda11 = Item(diccionario_monedas,self.x-530,self.y-350)
        moneda12 = Item(diccionario_monedas,self.x-560,self.y-350)
        self.lista_monedas = [moneda1,moneda2,moneda3,moneda4,moneda5,moneda6,moneda8,moneda9,moneda10,moneda11,moneda12]
    
    def set_puerta(self):
        reescalar_imagenes(diccionario_puertas, 160,195)
        puerta = Puerta(diccionario_puertas,30,self.y-255)
        self.puerta = puerta


    def set_heroe(self):
        reescalar_imagenes(diccionario_rambo, 120,150)
        self.heroe = Heroe(diccionario_rambo,5,0.5,(120,150),300,500,10)
    
    def bajar_vida(self):
        if self.heroe.vida > 0 :
            barra = py.transform.scale(barra_vida[self.heroe.vida -1], (200,60))
            self.screen.blit(barra,(20,20))

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
        tiempo_actual_shuriken = py.time.get_ticks() / 1000  # Obtiene el tiempo actual en segundos
        tiempo_transcurrido_shuriken = tiempo_actual_shuriken - self.tiempo_ultimo_bomba

        if tiempo_transcurrido_shuriken >= self.intervalo_shuriken:
            posicion_x = random.randrange(0, self.x)
            posicion_y = random.randrange(-100, -40)
            bomba = Bomba(diccionario_animaciones_shuriken, posicion_x, posicion_y,50,50)
            self.lista_shurikens.append(bomba)
            self.tiempo_ultimo_bomba = tiempo_actual_shuriken

    def enemigo_apuñalar(self,enemigo):
        if enemigo.esta_muerto == False and enemigo.rectangulo_principal.colliderect(self.heroe.smaller_rect):
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - self.tiempo_ultima_apuñalada
            if tiempo_transcurrido >= self.intervalo_apuñalada:
                sonido_espada.play()
                self.heroe.vida -= 1
                self.tiempo_ultima_apuñalada = tiempo_actual
        else:
            pass

    def manejar_eventos(self):
        for event in py.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == MOUSEBUTTONDOWN:
                    self.heroe.disparar(diccionario_animaciones_bala,event.pos[0],self.lista_balas_heroe,12,7)
                    self.disparo = True
                elif event.type == KEYDOWN:
                    if event.key == K_TAB:
                        cambiar_modo()

    def actualizar_elementos(self):
        for plataforma in self.plataformas:
                plataforma.blit(self.screen)
        self.bajar_vida()
        self.heroe.actualizar(self.screen, self.plataformas)
        Item.actualizar_items(self.lista_llave,self.screen)
        Item.actualizar_items(self.lista_monedas,self.screen)
        self.heroe.agarrar_llave(self.lista_llave,self.puerta,self.lista_enemigos)
        self.heroe.agarrar_monedas(self.lista_monedas)
        Bomba.actualizar_bomba(self.lista_shurikens,self.screen,self.y)
        self.heroe.colisionar_bombas(self.lista_shurikens,diccionario_animaciones_shuriken,self.screen,sonido_espada)
        self.enemigo.actualizar(self.screen,self.heroe)
        self.enemigo_2.actualizar(self.screen,self.heroe)

        if self.disparo == True:
            Bala.actualizar_balas(self.lista_balas_heroe,self.screen,self.x)
        Enemigo.verificar_muerte(self.enemigo,diccionario_animaciones_enemigo,self.screen,self.heroe,self.lista_balas_heroe, self.lista_enemigos,sonido_bomba)
        Enemigo.verificar_muerte(self.enemigo_2,diccionario_animaciones_enemigo,self.screen,self.heroe,self.lista_balas_heroe,self.lista_enemigos,sonido_bomba)
            
        self.enemigo_apuñalar(self.enemigo)
        self.enemigo_apuñalar(self.enemigo_2)
        # self.heroe.colisionar_balas(self.lista_balas_enemigo)
            
    def dibujar_rectangulos(self):
        if obtener_modo():
            py.draw.rect(self.screen, "blue", self.heroe.rectangulo_principal,3)
            py.draw.rect(self.screen, "blue", self.heroe.smaller_rect,3)

            py.draw.rect(self.screen, "red", self.enemigo.rectangulo_principal,3)
            py.draw.rect(self.screen, "red", self.enemigo_2.rectangulo_principal,3)
            py.draw.rect(self.screen, "red", self.puerta.rectangulo_principal,3)

            for bombas in self.lista_shurikens:
                py.draw.rect(self.screen, "red",bombas.rectangulo_principal,3)

            for plataforma in self.plataformas:
                py.draw.rect(self.screen, "red", plataforma.rect, 3)
        pass

    def run(self):
        while self.running:
            self.RELOJ.tick(self.FPS)
            self.manejar_eventos()
            self.move_heroe()
            self.fill_screen()
            self.crear_bomba()
            self.puerta.animar(self.screen)
            self.actualizar_elementos()
            self.dibujar_rectangulos()
            self.actualizar_score()
            self.bajar_timer()
            self.verificar_fin_juego()
            py.display.update()
            py.display.flip()
        py.quit()
