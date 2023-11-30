import pygame as py
import os

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (ancho,alto))

def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes

base_path = os.path.join("recursos_rambo", "imagenes")

fondo_filename = "background.jpeg"
plataforma_1_filename = "roca_chica_flotante.png"
plataforma_2_filename = "roca.png"
plataforma_3_filename = "roca2.png"
personaje_quieto_filename = "rambo_quieto.png"
personaje_mirando_derecha = "rambo_quieto.png"


fondo = os.path.join(base_path,fondo_filename)
fondo_level_2 = os.path.join(base_path,"fondo_street_fighter.jpg")
fondo_level_3 = os.path.join(base_path,"castillo.jpg")

fondo_menu = os.path.join(base_path,"Inicio.jpg")
letra = os.path.join("recursos_rambo","letra.ttf")
rectangulo = os.path.join(base_path,"rectangulo.png")

plataforma_1 = os.path.join(base_path,plataforma_1_filename)
plataforma_2 = os.path.join(base_path,plataforma_2_filename)
plataforma_3 = os.path.join(base_path,plataforma_3_filename)

plataforma_base = os.path.join(base_path,"plataforma.png")
plataforma_hielo = os.path.join(base_path,"platafroma_hielo.png")
plataforma_hielo_chica = os.path.join(base_path,"plataforma_hielo_chica.png")

barril = os.path.join(base_path,"barril.png")
personaje_quieto = [py.image.load(os.path.join(base_path,personaje_quieto_filename))]
personaje_mirando_derecha = [py.image.load(os.path.join(base_path,personaje_quieto_filename))]
personaje_mirando_izquierda = rotar_imagen(personaje_quieto)
personaje_camina_derecha = [py.image.load(os.path.join(base_path, "camina1.png")),
                            py.image.load(os.path.join(base_path, "camina2.png")),
                            py.image.load(os.path.join(base_path, "camina3.png")),
                            py.image.load(os.path.join(base_path, "camina4.png")),
                            py.image.load(os.path.join(base_path, "camina5.png")),
                            py.image.load(os.path.join(base_path, "camina6.png"))]
personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)

personaje_salta =  [py.image.load(os.path.join(base_path, "salta5.png"))]
personaje_salta_derecha =  [py.image.load(os.path.join(base_path, "salta5.png"))]
personaje_salta_izquiera =  rotar_imagen(personaje_salta)


enemigo_quieto_inicial = [py.image.load(os.path.join(base_path, "terrorista_quieto.png"))]
enemigo_quieto_izquierda = rotar_imagen(enemigo_quieto_inicial) 

enemigo_camina = [py.image.load(os.path.join(base_path, "terrorista_corriendo1.png")),
                py.image.load(os.path.join(base_path, "terrorista_corriendo2.png")),
                py.image.load(os.path.join(base_path, "terrorista_corriendo3.png")),
                py.image.load(os.path.join(base_path, "terrorista_corriendo4.png")),
                py.image.load(os.path.join(base_path, "terrorista_corriendo5.png")),
                py.image.load(os.path.join(base_path, "terrorista_corriendo6.png")),]

enemigo_camina_derecha = enemigo_camina 
enemigo_camina_izquierda = rotar_imagen(enemigo_camina) 

ninja_camina = [py.image.load(os.path.join(base_path, "ninja1.png")),
                py.image.load(os.path.join(base_path, "ninja2.png")),
                py.image.load(os.path.join(base_path, "ninja3.png")),
                py.image.load(os.path.join(base_path, "ninja4.png")),
                py.image.load(os.path.join(base_path, "ninja5.png")),
                py.image.load(os.path.join(base_path, "ninja6.png")),]
enemigo_muerte = [py.image.load(os.path.join(base_path, "explosion1.png")),
                    py.image.load(os.path.join(base_path, "explosion2.png")),
                    py.image.load(os.path.join(base_path, "explosion3.png")),
                    py.image.load(os.path.join(base_path, "explosion4.png")),
                    py.image.load(os.path.join(base_path, "explosion5.png")),]

ninja_camina_derecha = ninja_camina 
ninja_camina_izquierda = rotar_imagen(ninja_camina_derecha) 

mago_camina = [py.image.load(os.path.join(base_path, "wizard1.png")),
                py.image.load(os.path.join(base_path, "wizard2.png")),
                py.image.load(os.path.join(base_path, "wizard3.png")),
                py.image.load(os.path.join(base_path, "wizard4.png")),
                py.image.load(os.path.join(base_path, "wizard5.png")),
                py.image.load(os.path.join(base_path, "wizard6.png")),
                py.image.load(os.path.join(base_path, "wizard7.png")),
                py.image.load(os.path.join(base_path, "wizard8.png")),]

mago_dispara = [py.image.load(os.path.join(base_path, "wizard_dispara1.png")),
                py.image.load(os.path.join(base_path, "wizard_dispara2.png")),
                py.image.load(os.path.join(base_path, "wizard_dispara3.png")),
                py.image.load(os.path.join(base_path, "wizard_dispara4.png")),
                py.image.load(os.path.join(base_path, "wizard_dispara5.png")),
                py.image.load(os.path.join(base_path, "wizard_dispara6.png")),
                py.image.load(os.path.join(base_path, "wizard_dispara7.png"))]

mago_dispara_izquierda = rotar_imagen(mago_dispara)
mago_dispara_derecha = rotar_imagen(mago_dispara_izquierda)
mago_camina_derecha = mago_camina
mago_camina_izquierda = rotar_imagen(mago_camina_derecha)



bala = [py.image.load(os.path.join(base_path, "bala.png"))]
bala_derecha = [py.image.load(os.path.join(base_path, "bala.png"))]
bala_izquierda = rotar_imagen(bala_derecha)

hielo = [py.image.load(os.path.join(base_path, "hielo.png"))]
hielo_derecha = hielo
hielo_izquierda = rotar_imagen(hielo_derecha)

bomba = [py.image.load(os.path.join(base_path, "bomba.png"))]
bomba_explosion = [py.image.load(os.path.join(base_path, "explosion1.png")),
                    py.image.load(os.path.join(base_path, "explosion2.png")),
                    py.image.load(os.path.join(base_path, "explosion3.png")),
                    py.image.load(os.path.join(base_path, "explosion4.png")),
                    py.image.load(os.path.join(base_path, "explosion5.png")),]

puerta = [py.image.load(os.path.join(base_path, "puerta.png"))]
puerta_abre =  [py.image.load(os.path.join(base_path, "puerta.png")),
                py.image.load(os.path.join(base_path, "puerta2.png")),
                py.image.load(os.path.join(base_path, "puerta3.png")),
                py.image.load(os.path.join(base_path, "puerta4.png"))]
puerta_abierta = [py.image.load(os.path.join(base_path, "puerta4.png"))]

llave = [py.image.load(os.path.join(base_path, "llave.png"))]

moneda = [py.image.load(os.path.join(base_path, "moneda1.png")),
            py.image.load(os.path.join(base_path, "moneda3.png")),
            py.image.load(os.path.join(base_path, "moneda3.png")),
            py.image.load(os.path.join(base_path, "moneda4.png")),
            py.image.load(os.path.join(base_path, "moneda5.png")),
            py.image.load(os.path.join(base_path, "moneda6.png")),
            py.image.load(os.path.join(base_path, "moneda7.png")),
            py.image.load(os.path.join(base_path, "moneda8.png")),
            py.image.load(os.path.join(base_path, "moneda9.png"))]

barra_vida = [py.image.load(os.path.join(base_path, "barra5.png")),
                py.image.load(os.path.join(base_path, "barra4.png")),
                py.image.load(os.path.join(base_path, "barra3.png")),
                py.image.load(os.path.join(base_path, "barra2.png")),
                py.image.load(os.path.join(base_path, "barra1.png"))]

shruriken = [py.image.load(os.path.join(base_path, "shuriken1.png")),
                py.image.load(os.path.join(base_path, "shuriken2.png"))]


bomba_hielo = [py.image.load(os.path.join(base_path, "hielo_falling.png"))]
hielo_explosion = [py.image.load(os.path.join(base_path, "explosion_hielo1.png")),
                    py.image.load(os.path.join(base_path, "explosion_hielo2.png")),
                    py.image.load(os.path.join(base_path, "explosion_hielo3.png")),
                    py.image.load(os.path.join(base_path, "explosion_hielo4.png")),
                    py.image.load(os.path.join(base_path, "explosion_hielo5.png")),
                    py.image.load(os.path.join(base_path, "explosion_hielo6.png")),
                    py.image.load(os.path.join(base_path, "explosion_hielo7.png")),
                    py.image.load(os.path.join(base_path, "explosion_hielo8.png")),]

