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


