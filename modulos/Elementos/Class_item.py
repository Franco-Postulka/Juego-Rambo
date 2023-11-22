from modulos.Imagenes import *
from modulos.Elementos.Class_objeto import Objeto

class Item(Objeto):
    def __init__(self, animaciones, x, y) -> None:
        super().__init__(animaciones, x, y)
        self.animaciones = animaciones
        self.velocidad_animacion = 1
        self.rectangulo_principal = self.animaciones["inicial"][0].get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["inicial"]  

    @staticmethod
    def actualizar_items(lista_items,screen):
        for i in range(len(lista_items)):
            lista_items[i].animar(screen)