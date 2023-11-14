from Configuraciones import *
from Class_Personaje import*

class Enemigo:
    def __init__(self, animaciones:dict, vida:int) -> None:
        self.animaciones = animaciones
        self.velocidad_animacion = 0.35
        reescalar_imagenes(self.animaciones, 120,150)
        self.rectangulo_principal = self.animaciones["izquierda"][0].get_rect()
        self.rectangulo_principal.x = 900
        self.rectangulo_principal.y = 470
        self.vida = vida
        self.esta_muerto = False
        self.pasos = 0
        self.animacion_actual = self.animaciones["izquierda"]
        self.velocidad_actual = -5
        self.zona_tiro = False
        self.muriendo = False                                       

    # def avanzar(self):
    #     self.rectangulo_principal.x -= 3

    def avanzar(self,pantalla,personaje):
        if personaje.rectangulo_principal.bottom >= self.rectangulo_principal.y + 100:
            self.zona_tiro = True
            if personaje.rectangulo_principal.x > self.rectangulo_principal.x :
                self.velocidad_actual = 5 
                self.animacion_actual  = self.animaciones["derecha"]
            else:
                self.velocidad_actual = -5
                self.animacion_actual = self.animaciones["izquierda"]
            nueva_x = self.rectangulo_principal.x + self.velocidad_actual
            if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width:
                self.rectangulo_principal.x += self.velocidad_actual
        else:
            self.zona_tiro = False
            if self.rectangulo_principal.x <= 0:
                self.velocidad_actual = 5
                self.animacion_actual  = self.animaciones["derecha"]
            elif self.rectangulo_principal.x >= pantalla.get_width() - self.rectangulo_principal.width:
                self.velocidad_actual = -5
                self.animacion_actual = self.animaciones["izquierda"]
            self.rectangulo_principal.x += self.velocidad_actual

    def animar(self, pantalla):
        largo = len(self.animacion_actual)

        if self.pasos >= largo:
            self.pasos = 0
        pantalla.blit(self.animacion_actual[int(self.pasos)], self.rectangulo_principal)
        self.pasos += self.velocidad_animacion

        # if self.muriendo and self.pasos == largo:
        #     self.esta_muerto = True

    def actualizar(self, pantalla,personaje):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar(pantalla,personaje)

    

