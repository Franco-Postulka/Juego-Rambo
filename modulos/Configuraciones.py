import pygame as py

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


personaje_quieto = [py.image.load(r"recursos_rambo\rambo_quieto.png")]
personaje_mirando_derecha = [py.image.load(r"recursos_rambo\rambo_quieto.png")]
personaje_mirando_izquierda = rotar_imagen(personaje_quieto)
personaje_camina_derecha = [py.image.load(r"recursos_rambo\camina1.png"),
                            py.image.load(r"recursos_rambo\camina2.png"),
                            py.image.load(r"recursos_rambo\camina3.png"),
                            py.image.load(r"recursos_rambo\camina4.png"),
                            py.image.load(r"recursos_rambo\camina5.png"),
                            py.image.load(r"recursos_rambo\camina6.png")]
personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)

personaje_salta =  [py.image.load(r"recursos_rambo\salta5.png")]
personaje_salta_derecha =  [py.image.load(r"recursos_rambo\salta5.png")]
personaje_salta_izquiera =  rotar_imagen(personaje_salta)


enemigo_quieto_inicial = [py.image.load(r"recursos_rambo\terrorista_quieto.png")]
enemigo_quieto_izquierda = rotar_imagen(enemigo_quieto_inicial) 

enemigo_camina = [py.image.load(r"recursos_rambo\terrorista_corriendo1.png"),
                py.image.load(r"recursos_rambo\terrorista_corriendo2.png"),
                py.image.load(r"recursos_rambo\terrorista_corriendo3.png"),
                py.image.load(r"recursos_rambo\terrorista_corriendo4.png"),
                py.image.load(r"recursos_rambo\terrorista_corriendo5.png"),
                py.image.load(r"recursos_rambo\terrorista_corriendo6.png"),]
# enemigo_camina = [py.image.load(r"recursos_rambo\ninja1.png"),
#                 py.image.load(r"recursos_rambo\ninja2.png"),
#                 py.image.load(r"recursos_rambo\ninja3.png"),
#                 py.image.load(r"recursos_rambo\ninja4.png"),
#                 py.image.load(r"recursos_rambo\ninja5.png"),
#                 py.image.load(r"recursos_rambo\ninja6.png"),]

enemigo_camina_derecha = enemigo_camina 
enemigo_camina_izquierda = rotar_imagen(enemigo_camina) 


enemigo_muerte = [py.image.load(r"recursos_rambo\explosion1.png"),
                    py.image.load(r"recursos_rambo\explosion2.png"),
                    py.image.load(r"recursos_rambo\explosion3.png"),
                    py.image.load(r"recursos_rambo\explosion4.png"),
                    py.image.load(r"recursos_rambo\explosion5.png"),]

bala = [py.image.load(r"recursos_rambo\bala.png")]
bala_derecha = [py.image.load(r"recursos_rambo\bala.png")]
bala_izquierda = rotar_imagen(bala_derecha)

bomba = [py.image.load(r"recursos_rambo\bomba.png")]
bomba_explosion = [py.image.load(r"recursos_rambo\explosion1.png"),
                    py.image.load(r"recursos_rambo\explosion2.png"),
                    py.image.load(r"recursos_rambo\explosion3.png"),
                    py.image.load(r"recursos_rambo\explosion4.png"),
                    py.image.load(r"recursos_rambo\explosion5.png"),]

puerta = [py.image.load("recursos_rambo\puerta.png")]

llave = [py.image.load(r"recursos_rambo\llave.png")]

