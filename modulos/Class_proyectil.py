from modulos.Configuraciones import *
from modulos.Class_objeto import Objeto

class Proyectil(Objeto):
    def __init__(self, animaciones, posicion_x_inicial, posicion_y_inicial) -> None:
        super().__init__(animaciones, posicion_x_inicial, posicion_y_inicial)

    def mover(self):
        pass  

    def actualizar(self, pantalla):
        self.animar(pantalla)
        self.mover()

class Bala(Proyectil):
    def __init__(self, animaciones, direccion_x, posicion_x_inicial, posicion_y_inicial) -> None:
        super().__init__(animaciones, posicion_x_inicial, posicion_y_inicial)
        self.direccion_x = direccion_x
        reescalar_imagenes(self.animaciones, 10,5)
        # Otros atributos específicos de la Bala si los hay

    def mover(self, posicion_inicial_x):
        if self.direccion_x >= posicion_inicial_x:
            self.direccion_x = 3000
            self.rectangulo_principal.x += 25
            self.animacion_actual  = self.animaciones["derecha"]
        elif self.direccion_x <= posicion_inicial_x:
            self.direccion_x = -100
            self.rectangulo_principal.x -= 25
            self.animacion_actual = self.animaciones["inicial"]

    def actualizar(self, pantalla):
        self.animar(pantalla)
        self.mover(self.rectangulo_principal.x)

    @staticmethod
    def actualizar_balas(lista_balas,screen,W):
        for i in range(len(lista_balas)):
            lista_balas[i].actualizar(screen)
            if lista_balas[i].rectangulo_principal.x >= W or lista_balas[i].rectangulo_principal.x <= 0:
                del lista_balas[i]
                break


class Bomba(Proyectil):
    def __init__(self, animaciones, posicion_x_inicial, posicion_y_inicial) -> None:
        super().__init__(animaciones, posicion_x_inicial, posicion_y_inicial)
        reescalar_imagenes(self.animaciones, 75,75)

    def mover(self):
        self.rectangulo_principal.y += 10 
    
    @staticmethod
    def actualizar_bomba(lista_bombas,screen,H):
        for i in range(len(lista_bombas)):
            lista_bombas[i].actualizar(screen)
        for i in range(len(lista_bombas)):
            if lista_bombas[i].rectangulo_principal.y >= H:
                del lista_bombas[i]
                break
