from modulos.Imagenes import *
from modulos.sonidos import*
from modulos.Elementos.Class_personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, animaciones, vida, velocidad_animacion,tamaño,pos_x,pos_y,velocidad,top_izquierda,top_derecha):
        super().__init__(animaciones, vida, velocidad_animacion,tamaño, pos_x, pos_y,velocidad)
        self.esta_muerto = False
        self.animacion_actual = self.animaciones["derecha"]
        self.zona_tiro = False
        self.muriendo = False 
        self.top_izquierda = top_izquierda
        self.top_derecha = top_derecha
        self.velocidad = velocidad
        self.velocidad_actual = velocidad 

    def avanzar(self,personaje, sonido:None):
        if (personaje.rectangulo_principal.bottom >= self.rectangulo_principal.y + 100 and
            personaje.rectangulo_principal.top <= self.rectangulo_principal.bottom and
            personaje.rectangulo_principal.x >= self.top_izquierda and personaje.rectangulo_principal.x <= self.top_derecha):
            if self.zona_tiro == False:
                if sonido != None: 
                    sonido.play()
            self.zona_tiro = True
            if personaje.rectangulo_principal.x > self.rectangulo_principal.x :
                self.velocidad_actual = self.velocidad *1
                self.animacion_actual  = self.animaciones["derecha"]
            else:
                self.velocidad_actual = self.velocidad *-1
                self.animacion_actual = self.animaciones["inicial"]
            self.rectangulo_principal.x += self.velocidad_actual *1.5
        else:
            self.zona_tiro = False
            if self.rectangulo_principal.x <= self.top_izquierda:
                self.velocidad_actual = self.velocidad *1
                self.animacion_actual  = self.animaciones["derecha"]
            elif self.rectangulo_principal.x >= self.top_derecha - self.rectangulo_principal.width:
                self.velocidad_actual = self.velocidad *-1
                self.animacion_actual = self.animaciones["inicial"]
            self.rectangulo_principal.x += self.velocidad_actual

    def actualizar(self, pantalla, personaje, sonido = None):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar(personaje, sonido)

    def verificar_muerte(self,diccionario_animaciones_enemigo,screen,rambo,lista_balas_heroe,lista_enemigos,sonido):
        if self.vida <=0 and self.esta_muerto ==False:
            sonido.play()
            self.velocidad_animacion = 0.10
            self.animacion_actual = diccionario_animaciones_enemigo["muerte"]
            self.actualizar(screen,rambo)
            self.esta_muerto = True
            del lista_enemigos[0]
            self.score += 300
        for i in range(len(lista_balas_heroe)):
            if lista_balas_heroe[i].rectangulo_principal.colliderect(self.rectangulo_principal):
                del lista_balas_heroe[i]
                self.vida -= 15
                break


class Jefe(Enemigo):
    def __init__(self, animaciones, vida, velocidad_animacion, tamaño, pos_x, pos_y, velocidad, top_izquierda, top_derecha):
        super().__init__(animaciones, vida, velocidad_animacion, tamaño, pos_x, pos_y, velocidad, top_izquierda, top_derecha)

    def avanzar_jefe(self, personaje, sonido=None):
        if (personaje.rectangulo_principal.bottom >= self.rectangulo_principal.y + 100):
            if self.zona_tiro == False:
                if sonido != None: 
                    sonido.play()
            self.zona_tiro = True
            if personaje.rectangulo_principal.x > self.rectangulo_principal.x :
                self.animacion_actual  = self.animaciones["dispara derecha"]
            else:
                # self.velocidad_actual = 0
                self.animacion_actual = self.animaciones["dispara izquierda"]
            # self.rectangulo_principal.x += self.velocidad_actual 
        else:
            self.zona_tiro = False
            if self.velocidad_actual <=0:
                self.animacion_actual = self.animaciones["inicial"]
            elif self.velocidad_actual >=0:
                self.animacion_actual  = self.animaciones["derecha"]
            if self.rectangulo_principal.x <= self.top_izquierda:
                self.velocidad_actual = self.velocidad *1
                self.animacion_actual  = self.animaciones["derecha"]
            elif self.rectangulo_principal.x >= self.top_derecha - self.rectangulo_principal.width:
                self.velocidad_actual = self.velocidad *-1
                self.animacion_actual = self.animaciones["inicial"]
            self.rectangulo_principal.x += self.velocidad_actual


    def actualizar(self, pantalla, personaje, sonido = None):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar_jefe(personaje, sonido)


