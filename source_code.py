import pygame as py
import time
from pygame.locals import *
from Configuraciones import *
from os import system
system("cls")
from Class_Personaje import Personaje
from Modo import *
from Class_enemigo import Enemigo
from Class_bala import Bala
from Class_bomba import Bomba
from Class_plataforma import Plataforma
from Class_item import Item
import random

#ANCHO W - ALTO H
W,H = 1200, 680
FPS = 18 #Para desacelerar la pantalla

py.init()
RELOJ = py.time.Clock()
PANTALLA = py.display.set_mode((W,H)) # En pixeles
py.display.set_caption("Juego Mario")

#FONDO
fondo = py.image.load(r"recursos_rambo\background5.jpeg").convert()
fondo = py.transform.scale(fondo, (W,H))

contador_pasos = 0

diccionario = {}

diccionario["Quieto"] = personaje_quieto
diccionario["Mirando_izquirda"] = personaje_mirando_izquierda
diccionario["Mirando_derecha"] = personaje_mirando_derecha
diccionario["Derecha"] = personaje_camina_derecha
diccionario["Izquierda"] = personaje_camina_izquierda
diccionario["Salta"] = personaje_salta
diccionario["Salta_izquierda"] = personaje_salta_izquiera
diccionario["Salta_derecha"] = personaje_salta_derecha
rambo = Personaje(diccionario,(120,150),600,500,10)
reescalar_imagenes(diccionario, 120,150)

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


diccionario_animaciones_enemigo = {"izquierda": enemigo_camina_izquierda,"derecha":enemigo_camina_derecha,"muerte":enemigo_muerte}#, "quieto": enemigo_quieto_izquierda}
un_enemigo = Enemigo(diccionario_animaciones_enemigo, 100)
lista_enemigos = [un_enemigo]


diccionario_animaciones_bala = {"derecha": bala_derecha , "izquierda": bala_izquierda}
diccionario_animaciones_bomba = {"inicial": bomba, "explosion" : bomba_explosion}

#Personaje
x_inicial = W//2 - 400
y_inicial = 560
rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial
que_hace = "Quieto"


disparo = False
tiempo_ultimo_disparo = time.time()  # Inicializa el tiempo del último disparo
tiempo_ultimo_bomba = time.time()
intervalo_disparo = 1  # Establece el intervalo de tiempo entre disparos en segundos
lista_balas_enemigo = []
lista_balas_heroe = []
lista_bombas = []
intervalo_bomba = 2
flag = True
while flag:
    RELOJ.tick(FPS)
    for event in py.event.get():
        if event.type == QUIT:
            flag = False
        elif event.type == MOUSEBUTTONDOWN:
            abscisa = rambo.rectangulo_principal.x
            ordenada = rambo.rectangulo_principal.y + 50
            bala = Bala(diccionario_animaciones_bala,event.pos[0],abscisa,ordenada)
            if bala.direccion_x >= abscisa:
                bala.rectangulo_principal.x += 120 

            # lista_x_balas.append(abscisa)
            # lista_y_balas.append(ordenada)
            lista_balas_heroe.append(bala)
            disparo = True
        elif event.type == KEYDOWN:
            if event.key == K_TAB:
                cambiar_modo()


    PANTALLA.blit(fondo,(0,0))
    teclas = py.key.get_pressed()

    tiempo_actual_bomba = time.time()
    tiempo_transcurrido_bomba = tiempo_actual_bomba - tiempo_ultimo_bomba

    if tiempo_transcurrido_bomba >= intervalo_bomba:
        posicion_x = random.randrange(0, W)
        posicion_y = random.randrange(-100, -40)
        bomba = Bomba(diccionario_animaciones_bomba, posicion_x, posicion_y)
        lista_bombas.append(bomba)
        tiempo_ultimo_bomba = tiempo_actual_bomba

    if teclas[py.K_d]:
        rambo.que_hace = "Derecha"
    elif teclas[py.K_a]:
        rambo.que_hace = "Izquierda"
    elif(teclas[py.K_w]):
        rambo.que_hace = "Salta"
    else:
        rambo.que_hace = "Quieto"

    for plataforma in plataformas:
        plataforma.blit(PANTALLA)

    for i in range(len(diccionario_puertas)):
        PANTALLA.blit(diccionario_puertas["quieto"][i],(1050,H-220))


    rambo.actualizar(PANTALLA, plataformas)
    un_enemigo.actualizar(PANTALLA,rambo)
    llave.actualizar(PANTALLA)

    for i in range(len(lista_bombas)):
        lista_bombas[i].actualizar(PANTALLA)

    for i in range(len(lista_bombas)):
        if lista_bombas[i].rectangulo_principal.y >= H:
            del lista_bombas[i]
            break
    
    for i in range(len(lista_bombas)):
        if lista_bombas[i].rectangulo_principal.colliderect(rambo.rectangulo_principal):
            lista_bombas[i].velocidad_animacion = 0.05
            lista_bombas[i].animacion_actual = diccionario_animaciones_bomba["explosion"]
            lista_bombas[i].actualizar(PANTALLA)
            del lista_bombas[i]
            rambo.vida -= 30
            break
    

    if disparo == True:
        for i in range(len(lista_balas_heroe)):
            if lista_balas_heroe[i].rectangulo_principal.x >= W or lista_balas_heroe[i].rectangulo_principal.x <= 0:
                del lista_balas_heroe[i]
                break
        for j in range(len(lista_enemigos)):
            for i in range(len(lista_balas_heroe)):
                if lista_balas_heroe[i].rectangulo_principal.colliderect(lista_enemigos[j].rectangulo_principal):
                    del lista_balas_heroe[j]
                    lista_enemigos[j].vida -= 10
                    # print(lista_enemigos[j].vida)
                    break
        for i in range(len(lista_balas_heroe)):
            lista_balas_heroe[i].actualizar(PANTALLA)

        for i in range(len(lista_enemigos)):
            if lista_enemigos[i].vida <=0:
                lista_enemigos[i].velocidad_animacion = 0.10
                lista_enemigos[i].animacion_actual = diccionario_animaciones_enemigo["muerte"]
                lista_enemigos[i].actualizar(PANTALLA,rambo)
                lista_enemigos[i].esta_muerto = True
                del lista_enemigos[i]

    if un_enemigo.esta_muerto == False and un_enemigo.zona_tiro == True:
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_ultimo_disparo
        # print(f'Tiempo tardado: {tiempo_tardado}, Tiempo inicio:{tiempo_inicio/1000}, Tiempo anterior: {tiempor_anterior/1000}')
        if tiempo_transcurrido >= intervalo_disparo:
            bala2 = Bala(diccionario_animaciones_bala,rambo.rectangulo_principal.x,un_enemigo.rectangulo_principal.x,un_enemigo.rectangulo_principal.y + 50)
            if bala2.direccion_x >= un_enemigo.rectangulo_principal.x:
                    bala2.rectangulo_principal.x += 120
            lista_balas_enemigo.append(bala2)
            tiempo_ultimo_disparo = tiempo_actual  # Actualiza el tiempo del último disparo

    for i in range(len(lista_balas_enemigo)):
        if lista_balas_enemigo[i].rectangulo_principal.x >= W or lista_balas_enemigo[i].rectangulo_principal.x <= 0:
            del lista_balas_enemigo[i]
            break
    # for j in range(len(lista_enemigos)):
    for i in range(len(lista_balas_enemigo)):
        if lista_balas_enemigo[i].rectangulo_principal.colliderect(rambo.rectangulo_principal):
            del lista_balas_enemigo[i]
            rambo.vida -= 10
            # print(rambo.vida)
            break
    for i in range(len(lista_balas_enemigo)):
        lista_balas_enemigo[i].actualizar(PANTALLA)
        

    for i in range(len(lista_enemigos)):
        if rambo.vida <=0:
            print("moriste")
    
    if obtener_modo():
        py.draw.rect(PANTALLA, "blue", rambo.rectangulo_principal,3)

        py.draw.rect(PANTALLA, "red", un_enemigo.rectangulo_principal,3)

        for plataforma in plataformas:
            py.draw.rect(PANTALLA, "red", plataforma.rect, 3)

    py.display.update()

py.quit()