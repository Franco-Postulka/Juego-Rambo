import os
import pygame as py

py.mixer.init()
# Obtener la ruta base del directorio de sonidos
base_path = os.path.join("recursos_rambo", "sonidos")


# Definir los nombres de los archivos de sonido
disparo_filename = "disparo.wav"
bomba_filename = "granada.wav"
salto_filename = "jump.wav"
caida_salto_filename = "land.wav"
recibo_disparo_filename = "gunhit.wav"
visto_filename = "visto.wav"
llave_filename = "llave.wav"
fondo_filename = "war_machines.wav"


sonido_fondo = os.path.join(base_path,fondo_filename)
sonido_fondo_inicio = os.path.join(base_path,"badlands.wav")
sonido_fondo_samurai = os.path.join(base_path,"musica_samurai.wav")
sonido_fondo_mago = os.path.join(base_path,"musica_mago.wav")

# Cargar los sonidos usando las rutas completas
sonido_disparo = py.mixer.Sound(os.path.join(base_path, disparo_filename))
sonido_disparo.set_volume(0.3)

sonido_disparo_enemigo = py.mixer.Sound(os.path.join(base_path, disparo_filename))
sonido_disparo_enemigo.set_volume(0.35)

sonido_bomba = py.mixer.Sound(os.path.join(base_path, bomba_filename))
sonido_bomba.set_volume(0.30)

sonido_salto = py.mixer.Sound(os.path.join(base_path, salto_filename))
sonido_salto.set_volume(0.6)

sonido_caida_salto = py.mixer.Sound(os.path.join(base_path, caida_salto_filename))

sonido_recibo_disparo = py.mixer.Sound(os.path.join(base_path, recibo_disparo_filename))
sonido_recibo_disparo.set_volume(0.6)

sonido_visto = py.mixer.Sound(os.path.join(base_path, visto_filename))
sonido_visto.set_volume(0.5)

sonido_llave = py.mixer.Sound(os.path.join(base_path, llave_filename))
sonido_llave.set_volume(0.5)

sonido_moneda = py.mixer.Sound(os.path.join(base_path, "moneda.wav"))
sonido_moneda.set_volume(0.15)

sonido_espada = py.mixer.Sound(os.path.join(base_path, "espada.wav"))
sonido_espada.set_volume(0.5)

sonido_disparo_mago = py.mixer.Sound(os.path.join(base_path, "mago_dispara2.ogg"))
sonido_disparo_mago.set_volume(0.5)

sonido_congelado = py.mixer.Sound(os.path.join(base_path, "congelamiento.ogg"))
sonido_congelado.set_volume(0.5)

sonido_colision_hielo = py.mixer.Sound(os.path.join(base_path, "explosion_hielo.ogg"))
sonido_congelado.set_volume(0.5)






# py.mixer.init()
# sonido_disparo = py.mixer.Sound(r"recursos_rambo\sonidos\diaparo.wav")
# sonido_disparo.set_volume(0.3)  

# sonido_disparo_enemigo = py.mixer.Sound(r"recursos_rambo\sonidos\diaparo.wav")
# sonido_disparo_enemigo.set_volume(0.35)  

# sonido_bomba = py.mixer.Sound(r"recursos_rambo\sonidos\granada.wav")
# sonido_bomba.set_volume(0.30)


# sonido_salto = py.mixer.Sound(r"recursos_rambo\sonidos\jump.wav")
# sonido_salto.set_volume(0.6)
# sonido_caida_salto = py.mixer.Sound(r"recursos_rambo\sonidos\land.wav")

# sonido_recibo_disparo = py.mixer.Sound(r"recursos_rambo\sonidos\gunhit.wav")
# sonido_recibo_disparo.set_volume(0.6)


# sonido_visto = py.mixer.Sound(r"recursos_rambo\sonidos\visto.wav")
# sonido_visto.set_volume(0.5)

# sonido_llave = py.mixer.Sound(r"recursos_rambo\sonidos\moneda.wav")
# sonido_llave.set_volume(0.5)


