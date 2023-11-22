from modulos.Imagenes import *
from modulos.Elementos.Class_objeto import Objeto

class Personaje(Objeto):
    def __init__(self, animaciones, vida, velocidad_animacion, tamaño, pos_x, pos_y, velocidad):
        super().__init__(animaciones, pos_x, pos_y)
        reescalar_imagenes(self.animaciones, *tamaño)
        self.vida = vida
        self.velocidad_animacion = velocidad_animacion
        self.animacion_actual = self.animaciones["inicial"]
        self.rectangulo_principal = self.animaciones["inicial"][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.velocidad = velocidad
        