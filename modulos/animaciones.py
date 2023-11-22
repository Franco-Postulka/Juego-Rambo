from modulos.Imagenes import *
from modulos.Elementos.Class_item import Item

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


diccionario_puertas = {"inicial": puerta, "abierta": puerta_abre, "final": puerta_abierta}
# diccionario_puertas["inicial"] = puerta
# diccionario_puertas["abierta"] = puerta_abre
# reescalar_imagenes(diccionario_puertas, 140,150)

############## Item ###################
diccionario_llaves = {}
diccionario_llaves["inicial"] = llave

diccionario_animaciones_enemigo = {"inicial": enemigo_camina_izquierda,"derecha":enemigo_camina_derecha,"muerte":enemigo_muerte}

diccionario_animaciones_bala = { "inicial": bala_izquierda,"derecha": bala_derecha }
diccionario_animaciones_bomba = {"inicial": bomba, "explosion" : bomba_explosion}