import pygame as py 
from modulos.Configuraciones import *
from modulos.Class_heroe import Heroe
from modulos.Class_enemigo import Enemigo
from modulos.Class_proyectil import*
from modulos.Class_item import Item

W = 1200
H = 680


diccionario_rambo = {}
diccionario_rambo["inicial"] = personaje_quieto
diccionario_rambo["Mirando_izquirda"] = personaje_mirando_izquierda
diccionario_rambo["Mirando_derecha"] = personaje_mirando_derecha
diccionario_rambo["Derecha"] = personaje_camina_derecha
diccionario_rambo["Izquierda"] = personaje_camina_izquierda
diccionario_rambo["Salta"] = personaje_salta
diccionario_rambo["Salta_izquierda"] = personaje_salta_izquiera
diccionario_rambo["Salta_derecha"] = personaje_salta_derecha
# rambo = Heroe(diccionario_rambo,100,0.5,(120,150),600,500,10)
# reescalar_imagenes(diccionario_rambo, 120,150)

diccionario_puertas = {}
diccionario_puertas["quieto"] = puerta
reescalar_imagenes(diccionario_puertas, 140,150)

############## Item ###################
diccionario_llaves = {}
diccionario_llaves["inicial"] = llave
llave = Item(diccionario_llaves,150,H-450)

diccionario_animaciones_enemigo = {"inicial": enemigo_camina_izquierda,"derecha":enemigo_camina_derecha,"muerte":enemigo_muerte}
# un_enemigo = Enemigo(diccionario_animaciones_enemigo,100,0.35,(120,150),900,470,5)
# lista_enemigos = [un_enemigo]

diccionario_animaciones_bala = { "inicial": bala_izquierda,"derecha": bala_derecha }
diccionario_animaciones_bomba = {"inicial": bomba, "explosion" : bomba_explosion}