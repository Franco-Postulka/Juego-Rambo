import pygame as py

py.mixer.init()
sonido_disparo = py.mixer.Sound(r"recursos_rambo\sonidos\diaparo.wav")
sonido_disparo.set_volume(0.3)  

sonido_disparo_enemigo = py.mixer.Sound(r"recursos_rambo\sonidos\diaparo.wav")
sonido_disparo_enemigo.set_volume(0.35)  

sonido_bomba = py.mixer.Sound(r"recursos_rambo\sonidos\granada.wav")
sonido_bomba.set_volume(0.30)


sonido_salto = py.mixer.Sound(r"recursos_rambo\sonidos\jump.wav")
sonido_salto.set_volume(0.6)
sonido_caida_salto = py.mixer.Sound(r"recursos_rambo\sonidos\land.wav")

sonido_recibo_disparo = py.mixer.Sound(r"recursos_rambo\sonidos\gunhit.wav")
sonido_recibo_disparo.set_volume(0.6)


sonido_visto = py.mixer.Sound(r"recursos_rambo\sonidos\visto.wav")
sonido_visto.set_volume(0.5)

sonido_llave = py.mixer.Sound(r"recursos_rambo\sonidos\moneda.wav")
sonido_llave.set_volume(0.5)


