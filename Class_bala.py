from Configuraciones import *
# from Class_Personaje import*

class Bala:
    def __init__(self, animaciones, direccion_x,posicion_x_incial,posicion_y_inicial) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, 10,5)
        self.rectangulo_principal = self.animaciones["derecha"][0].get_rect()
        self.rectangulo_principal.x = posicion_x_incial
        self.rectangulo_principal.y = posicion_y_inicial
        self.pasos = 0
        self.animacion_actual = self.animaciones["derecha"]  
        self.direccion_x = direccion_x
        

    def avanzar(self, posicion_inicial_x):
        if self.direccion_x >= posicion_inicial_x:
            self.direccion_x = 3000
            self.rectangulo_principal.x += 25
            self.animacion_actual  = self.animaciones["derecha"]
        elif self.direccion_x <= posicion_inicial_x:
            self.direccion_x = -100
            self.rectangulo_principal.x -= 25
            self.animacion_actual = self.animaciones["izquierda"]
        return self.rectangulo_principal.x
        
    def animar(self, pantalla):
        largo = len(self.animacion_actual)

        if self.pasos >= largo:
            self.pasos = 0
        pantalla.blit(self.animacion_actual[self.pasos],self.rectangulo_principal )
        self.pasos += 1

        # if self.muriendo and self.pasos == largo:
        #     self.esta_muerto = True

    
    def actualizar(self,pantalla):
        # if self.esta_muerto == False:
        self.animar(pantalla)
        self.avanzar(self.rectangulo_principal.x)
            

    

