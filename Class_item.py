from Configuraciones import *
# from Class_Personaje import*

class Item:
    def __init__(self, animaciones,x,y) -> None:
        self.animaciones = animaciones
        self.velocidad_animacion = 1
        reescalar_imagenes(self.animaciones, 30,30)
        self.rectangulo_principal = self.animaciones["inicial"][0].get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.pasos = 0
        self.animacion_actual = self.animaciones["inicial"]  
        

    def actualizar(self, pantalla):
        largo = len(self.animacion_actual)

        if self.pasos >= largo:
            self.pasos = 0
        pantalla.blit(self.animacion_actual[self.pasos],self.rectangulo_principal )
        self.pasos +=  self.velocidad_animacion
    

    

