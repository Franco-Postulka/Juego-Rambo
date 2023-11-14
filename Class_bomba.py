from Configuraciones import *
# from Class_Personaje import*

class Bomba:
    def __init__(self, animaciones,posicion_x_incial,posicion_y_inicial) -> None:
        self.animaciones = animaciones
        self.velocidad_animacion = 1
        reescalar_imagenes(self.animaciones, 75,75)
        self.rectangulo_principal = self.animaciones["inicial"][0].get_rect()
        self.rectangulo_principal.x = posicion_x_incial
        self.rectangulo_principal.y = posicion_y_inicial
        self.pasos = 0
        self.animacion_actual = self.animaciones["inicial"]  
        

    def caer(self):
        self.rectangulo_principal.y += 10 
        return self.rectangulo_principal.y

    def animar(self, pantalla):
        largo = len(self.animacion_actual)

        if self.pasos >= largo:
            self.pasos = 0
        pantalla.blit(self.animacion_actual[self.pasos],self.rectangulo_principal )
        self.pasos +=  self.velocidad_animacion

    
    def actualizar(self,pantalla):
        self.animar(pantalla)
        self.caer()
            

    

