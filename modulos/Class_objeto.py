from modulos.Configuraciones import *

class Objeto:
    def __init__(self, animaciones, x, y) -> None:
        self.animaciones = animaciones
        self.velocidad_animacion = 1
        self.rectangulo_principal = self.animaciones["inicial"][0].get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["inicial"]  

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rectangulo_principal)
        self.contador_pasos += self.velocidad_animacion

