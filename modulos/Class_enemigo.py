from modulos.Configuraciones import *
from modulos.Class_personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, animaciones, vida, velocidad_animacion,tamaño,pos_x,pos_y,velocidad):
        super().__init__(animaciones, vida, velocidad_animacion,tamaño, pos_x, pos_y,velocidad)
        self.esta_muerto = False
        self.animacion_actual = self.animaciones["inicial"]
        self.zona_tiro = False
        self.muriendo = False  

    def avanzar(self,pantalla,personaje):
        if personaje.rectangulo_principal.bottom >= self.rectangulo_principal.y + 100:
            self.zona_tiro = True
            if personaje.rectangulo_principal.x > self.rectangulo_principal.x :
                self.velocidad_actual = self.velocidad *1
                self.animacion_actual  = self.animaciones["derecha"]
            else:
                self.velocidad_actual = self.velocidad *-1
                self.animacion_actual = self.animaciones["inicial"]
            nueva_x = self.rectangulo_principal.x + self.velocidad_actual
            if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width:
                self.rectangulo_principal.x += self.velocidad_actual
        else:
            self.zona_tiro = False
            if self.rectangulo_principal.x <= 0:
                self.velocidad_actual = self.velocidad *1
                self.animacion_actual  = self.animaciones["derecha"]
            elif self.rectangulo_principal.x >= pantalla.get_width() - self.rectangulo_principal.width:
                self.velocidad_actual = self.velocidad *-1
                self.animacion_actual = self.animaciones["inicial"]
            self.rectangulo_principal.x += self.velocidad_actual

    def actualizar(self, pantalla, personaje):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar(pantalla,personaje)