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

    # def verificar_muerte(lista_enemigos,diccionario_animaciones_enemigo,screen,rambo,lista_balas_heroe):
    #     for j in range(len(lista_enemigos)):
    #         if lista_enemigos[j].vida <=0:
    #             lista_enemigos[j].velocidad_animacion = 0.10
    #             lista_enemigos[j].animacion_actual = diccionario_animaciones_enemigo["muerte"]
    #             lista_enemigos[j].actualizar(screen,rambo)
    #             lista_enemigos[j].esta_muerto = True
    #             del lista_enemigos[j]
    #             break
    #         for i in range(len(lista_balas_heroe)):
    #             if lista_balas_heroe[i].rectangulo_principal.colliderect(lista_enemigos[j].rectangulo_principal):
    #                 del lista_balas_heroe[j]
    #                 lista_enemigos[j].vida -= 10
    #                 break

    def verificar_muerte(self,diccionario_animaciones_enemigo,screen,rambo,lista_balas_heroe):
        if self.vida <=0:
            self.velocidad_animacion = 0.10
            self.animacion_actual = diccionario_animaciones_enemigo["muerte"]
            self.actualizar(screen,rambo)
            self.esta_muerto = True
            # del self
            self.esta_muerto = True
        for i in range(len(lista_balas_heroe)):
            if lista_balas_heroe[i].rectangulo_principal.colliderect(self.rectangulo_principal):
                del lista_balas_heroe[i]
                self.vida -= 10
                break

