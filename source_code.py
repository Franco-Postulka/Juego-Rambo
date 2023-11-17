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

#ANCHO W - ALTO H
W,H = 1200, 680
FPS = 18 #Para desacelerar la pantalla

py.init()
RELOJ = py.time.Clock()
PANTALLA = py.display.set_mode((W,H)) # En pixeles
py.display.set_caption("Juego Mario")

#FONDO
fondo = py.image.load(r"recursos_rambo\background.jpeg").convert()
fondo = py.transform.scale(fondo, (W,H))

# archivo de animaciones (que sea un atributo del personaje)
diccionario_rambo = {}
diccionario_rambo["inicial"] = personaje_quieto
diccionario_rambo["Mirando_izquirda"] = personaje_mirando_izquierda
diccionario_rambo["Mirando_derecha"] = personaje_mirando_derecha
diccionario_rambo["Derecha"] = personaje_camina_derecha
diccionario_rambo["Izquierda"] = personaje_camina_izquierda
diccionario_rambo["Salta"] = personaje_salta
diccionario_rambo["Salta_izquierda"] = personaje_salta_izquiera
diccionario_rambo["Salta_derecha"] = personaje_salta_derecha
rambo = Heroe(diccionario_rambo,100,0.5,(120,150),600,500,10)
reescalar_imagenes(diccionario_rambo, 120,150)

diccionario_puertas = {}
diccionario_puertas["quieto"] = puerta
reescalar_imagenes(diccionario_puertas, 140,150)

############## Item ###################
diccionario_llaves = {}
diccionario_llaves["inicial"] = llave
llave = Item(diccionario_llaves,150,H-450)

############## PLatafromas ################
piso = Plataforma(False, (W, 135), 0, H-70)
plataforma_roca_grande = Plataforma(False, (200, 20), 140, H-170)
plataforma_roca_chica = Plataforma(False, (35, 20), 850, H-175)
plataforma_roca_flotante = Plataforma(True, (250, 10), 380, H-280, r"recursos_rambo\roca_chica_flotante.png",(350, H-300))
plataforma_roca_flotante2 = Plataforma(True, (250, 10), 730, H-380, r"recursos_rambo\roca.png",(700, H-400))
plataforma_roca_flotante3 = Plataforma(True, (180, 10), 45, H-380, r"recursos_rambo\roca2.png",(25, H-400))
plataformas = [piso, plataforma_roca_grande, plataforma_roca_chica, plataforma_roca_flotante,plataforma_roca_flotante2,plataforma_roca_flotante3]


diccionario_animaciones_enemigo = {"inicial": enemigo_camina_izquierda,"derecha":enemigo_camina_derecha,"muerte":enemigo_muerte}
un_enemigo = Enemigo(diccionario_animaciones_enemigo,100,0.35,(120,150),900,470,5)
lista_enemigos = [un_enemigo]

diccionario_animaciones_bala = { "inicial": bala_izquierda,"derecha": bala_derecha }
diccionario_animaciones_bomba = {"inicial": bomba, "explosion" : bomba_explosion}

disparo = False
tiempo_ultimo_disparo = time.time()  # Inicializa el tiempo del último disparo
tiempo_ultimo_bomba = time.time()
intervalo_disparo = 1  # Establece el intervalo de tiempo entre disparos en segundos
intervalo_bomba = 2
lista_balas_enemigo = []
lista_balas_heroe = []
lista_bombas = []
flag = True
while flag:
    RELOJ.tick(FPS)
    for event in py.event.get():
        if event.type == QUIT:
            flag = False
        elif event.type == MOUSEBUTTONDOWN:
            rambo.disparar(diccionario_animaciones_bala,event.pos[0],lista_balas_heroe)
            disparo = True
        elif event.type == KEYDOWN:
            if event.key == K_TAB:
                cambiar_modo()

    teclas = py.key.get_pressed()

    if teclas[py.K_d]:
        rambo.que_hace = "Derecha"
    elif teclas[py.K_a]:
        rambo.que_hace = "Izquierda"
    elif(teclas[py.K_w]):
        rambo.que_hace = "Salta"
    else:
        rambo.que_hace = "inicial"

    PANTALLA.blit(fondo,(0,0))

    ######## Metodo de Bomba para crear la bomba y appendear a la lista (metodo de la clase game)
    tiempo_actual_bomba = time.time()
    tiempo_transcurrido_bomba = tiempo_actual_bomba - tiempo_ultimo_bomba
    if tiempo_transcurrido_bomba >= intervalo_bomba:
        posicion_x = random.randrange(0, W)
        posicion_y = random.randrange(-100, -40)
        bomba = Bomba(diccionario_animaciones_bomba, posicion_x, posicion_y)
        lista_bombas.append(bomba)
        tiempo_ultimo_bomba = tiempo_actual_bomba


    for plataforma in plataformas:
        plataforma.blit(PANTALLA)

    for i in range(len(diccionario_puertas)):
        PANTALLA.blit(diccionario_puertas["quieto"][i],(1050,H-220))


    llave.animar(PANTALLA)
    un_enemigo.actualizar(PANTALLA,rambo)
    rambo.actualizar(PANTALLA, plataformas)
    Bomba.actualizar_bomba(lista_bombas,PANTALLA,H)
    rambo.colisionar_bombas(lista_bombas,diccionario_animaciones_bomba,PANTALLA)
    

    if disparo == True:
        Bala.actualizar_balas(lista_balas_heroe,PANTALLA,W)
        Enemigo.verificar_muerte(lista_enemigos,diccionario_animaciones_enemigo,PANTALLA,rambo,lista_balas_heroe)

    ############Metodo de bala para crear la bala y appendear a la lista (metodo de la clase game)
    if un_enemigo.esta_muerto == False and un_enemigo.zona_tiro == True:
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_ultimo_disparo
        if tiempo_transcurrido >= intervalo_disparo:
            bala = Bala(diccionario_animaciones_bala,rambo.rectangulo_principal.x,un_enemigo.rectangulo_principal.x,un_enemigo.rectangulo_principal.y + 50)
            if bala.direccion_x >= un_enemigo.rectangulo_principal.x:
                    bala.rectangulo_principal.x += 120
            lista_balas_enemigo.append(bala)
            tiempo_ultimo_disparo = tiempo_actual  # Actualiza el tiempo del último disparo

    Bala.actualizar_balas(lista_balas_enemigo,PANTALLA,W)
    rambo.colisionar_balas(lista_balas_enemigo)
    
    if obtener_modo():
        py.draw.rect(PANTALLA, "blue", rambo.rectangulo_principal,3)

        py.draw.rect(PANTALLA, "red", un_enemigo.rectangulo_principal,3)

        for plataforma in plataformas:
            py.draw.rect(PANTALLA, "red", plataforma.rect, 3)

    py.display.update()

py.quit()

