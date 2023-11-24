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

fondo = r"recursos_rambo\imagenes\background.jpeg"

plataforma_1 = r"recursos_rambo\imagenes\roca_chica_flotante.png"
plataforma_2 = r"recursos_rambo\imagenes\roca.png"
plataforma_3 = r"recursos_rambo\imagenes\roca2.png"

personaje_quieto = [py.image.load(r"recursos_rambo\imagenes\rambo_quieto.png")]
personaje_mirando_derecha = [py.image.load(r"recursos_rambo\imagenes\rambo_quieto.png")]
personaje_mirando_izquierda = rotar_imagen(personaje_quieto)
personaje_camina_derecha = [py.image.load(r"recursos_rambo\imagenes\camina1.png"),
                            py.image.load(r"recursos_rambo\imagenes\camina2.png"),
                            py.image.load(r"recursos_rambo\imagenes\camina3.png"),
                            py.image.load(r"recursos_rambo\imagenes\camina4.png"),
                            py.image.load(r"recursos_rambo\imagenes\camina5.png"),
                            py.image.load(r"recursos_rambo\imagenes\camina6.png")]
personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)

personaje_salta =  [py.image.load(r"recursos_rambo\imagenes\salta5.png")]
personaje_salta_derecha =  [py.image.load(r"recursos_rambo\imagenes\salta5.png")]
personaje_salta_izquiera =  rotar_imagen(personaje_salta)


enemigo_quieto_inicial = [py.image.load(r"recursos_rambo\imagenes\terrorista_quieto.png")]
enemigo_quieto_izquierda = rotar_imagen(enemigo_quieto_inicial) 

enemigo_camina = [py.image.load(r"recursos_rambo\imagenes\terrorista_corriendo1.png"),
                py.image.load(r"recursos_rambo\imagenes\terrorista_corriendo2.png"),
                py.image.load(r"recursos_rambo\imagenes\terrorista_corriendo3.png"),
                py.image.load(r"recursos_rambo\imagenes\terrorista_corriendo4.png"),
                py.image.load(r"recursos_rambo\imagenes\terrorista_corriendo5.png"),
                py.image.load(r"recursos_rambo\imagenes\terrorista_corriendo6.png"),]

enemigo_camina_derecha = enemigo_camina 
enemigo_camina_izquierda = rotar_imagen(enemigo_camina) 


enemigo_muerte = [py.image.load(r"recursos_rambo\imagenes\explosion1.png"),
                    py.image.load(r"recursos_rambo\imagenes\explosion2.png"),
                    py.image.load(r"recursos_rambo\imagenes\explosion3.png"),
                    py.image.load(r"recursos_rambo\imagenes\explosion4.png"),
                    py.image.load(r"recursos_rambo\imagenes\explosion5.png"),]

bala = [py.image.load(r"recursos_rambo\imagenes\bala.png")]
bala_derecha = [py.image.load(r"recursos_rambo\imagenes\bala.png")]
bala_izquierda = rotar_imagen(bala_derecha)

bomba = [py.image.load(r"recursos_rambo\imagenes\bomba.png")]
bomba_explosion = [py.image.load(r"recursos_rambo\imagenes\explosion1.png"),
                    py.image.load(r"recursos_rambo\imagenes\explosion2.png"),
                    py.image.load(r"recursos_rambo\imagenes\explosion3.png"),
                    py.image.load(r"recursos_rambo\imagenes\explosion4.png"),
                    py.image.load(r"recursos_rambo\imagenes\explosion5.png"),]

puerta = [py.image.load(r"recursos_rambo\imagenes\puerta.png")]
puerta_abre =  [py.image.load(r"recursos_rambo\imagenes\puerta.png"),
                py.image.load(r"recursos_rambo\imagenes\puerta2.png"),
                py.image.load(r"recursos_rambo\imagenes\puerta3.png"),
                py.image.load(r"recursos_rambo\imagenes\puerta4.png")]
puerta_abierta = [py.image.load(r"recursos_rambo\imagenes\puerta4.png")]

llave = [py.image.load(r"recursos_rambo\imagenes\llave.png")]

barra_vida = [py.image.load(r"recursos_rambo\imagenes\barra5.png"),
                py.image.load(r"recursos_rambo\imagenes\barra4.png"),
                py.image.load(r"recursos_rambo\imagenes\barra3.png"),
                py.image.load(r"recursos_rambo\imagenes\barra2.png"),
                py.image.load(r"recursos_rambo\imagenes\barra1.png")]

