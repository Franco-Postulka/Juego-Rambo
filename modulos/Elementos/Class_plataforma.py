import pygame as py 

class Plataforma():
    def __init__(self, visible, tamaño, x, y, path="",posicion_imagen = (0,0)):
        self.visible = visible
        self.posicion = posicion_imagen

        if visible:
            if path:
                self.image_sin_escalar = py.image.load(path)
                self.image = py.transform.scale(self.image_sin_escalar, tamaño)
            else:
                self.image = py.Surface(tamaño)
        else:
            self.image = py.Surface(tamaño)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blit(self, pantalla):
        if self.visible:
            pantalla.blit(self.image_sin_escalar, self.posicion)
