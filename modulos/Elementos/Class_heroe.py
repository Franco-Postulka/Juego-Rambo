from modulos.Imagenes import *
from modulos.sonidos import* 
from modulos.Elementos.Class_personaje import Personaje
from modulos.Elementos.Class_proyectil import Bala
import pygame


class Heroe(Personaje):
    def __init__(self, animaciones, vida, velocidad_animacion, tamaño, pos_x, pos_y, velocidad):
        super().__init__(animaciones, vida, velocidad_animacion, tamaño, pos_x, pos_y, velocidad)
        self.tamaño =  tamaño
        self.que_hace = "inicial"
        self.contador_pasos = 0
        self.new_width = self.tamaño[0] // 2
        self.new_height = self.tamaño[1] // 2

        # Calcular las coordenadas para centrar el nuevo rectángulo en el centro del rectángulo original
        self.new_x = self.rectangulo_principal.x + self.new_width // 2
        self.new_y = self.rectangulo_principal.y + self.new_height // 2
        # Crear el nuevo rectángulo más pequeño y centrado
        self.smaller_rect = pygame.Rect(self.new_x, self.new_y, self.new_width, self.new_height) 

        self.desplazamiento_y = 0
        self.potencia_salto = -25
        self.limite_velocidad_salto = 15
        self.gravedad = 3
        self.esta_saltando =False

    def actualizar(self, pantalla, piso):
        match self.que_hace:
            case "Derecha":
                if not self.esta_saltando:

                    self.animacion_actual  = self.animaciones["Derecha"]
                    self.animaciones["inicial"] = self.animaciones['Mirando_derecha']
                    self.animaciones["Salta"] = self.animaciones['Salta_derecha']
                    self.animar(pantalla)
                self.caminar(pantalla)

            case "Izquierda":
                if not self.esta_saltando:
                    self.animacion_actual  = self.animaciones["Izquierda"]
                    self.animaciones["inicial"] = self.animaciones['Mirando_izquirda']
                    self.animaciones["Salta"] = self.animaciones['Salta_izquierda']
                    self.animar(pantalla)
                self.caminar(pantalla)

            case "inicial":
                if not self.esta_saltando:
                    self.animacion_actual  = self.animaciones["inicial"]
                    self.animar(pantalla)

            case "Salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    sonido_salto.play()
                    self.desplazamiento_y = self.potencia_salto 
                    self.animacion_actual  = self.animaciones["Salta"]
                    self.animar(pantalla)
        self.aplicar_gravedad(pantalla, piso)


    def caminar(self, pantalla):
        velocidad_actual = self.velocidad
        if self.que_hace == "Izquierda":
            velocidad_actual *= -1
        nueva_x = self.rectangulo_principal.x + velocidad_actual
        if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width:
            self.rectangulo_principal.x += velocidad_actual
            self.smaller_rect.x+= velocidad_actual
    
    def aplicar_gravedad(self, pantalla, plataformas):
        tocando_plataforma = False
        if self.esta_saltando:
            # self.animacion_actual  = self.animaciones["Salta"]
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y
            self.smaller_rect.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
            
        for plataforma in plataformas:
            for i in range(self.rectangulo_principal.width):
                if plataforma.rect.collidepoint(self.rectangulo_principal.x + i ,self.rectangulo_principal.bottom):
                    self.desplazamiento_y = 0
                    self.esta_saltando = False
                    self.rectangulo_principal.bottom = plataforma.rect.top
                    self.smaller_rect.y = self.rectangulo_principal.y + self.new_height // 2

                    tocando_plataforma = True  
                    break
        if not tocando_plataforma:
            self.esta_saltando = True
    
    def disparar(self,diccionario_animaciones_bala,direccion_x,lista_balas_heroe):
        abscisa = self.rectangulo_principal.x
        ordenada = self.rectangulo_principal.y + 50
        bala = Bala(diccionario_animaciones_bala,direccion_x,abscisa,ordenada)
        if bala.direccion_x >= abscisa:
            bala.rectangulo_principal.x += 120 
        lista_balas_heroe.append(bala)
        sonido_disparo.play()

    def colisionar_bombas(self,lista_bombas,diccionario_animaciones_bomba,screen):
        for i in range(len(lista_bombas)):
            if lista_bombas[i].rectangulo_principal.colliderect(self.rectangulo_principal):
                sonido_recibo_disparo.play()
                sonido_bomba.play()
                lista_bombas[i].velocidad_animacion = 0.05
                lista_bombas[i].animacion_actual = diccionario_animaciones_bomba["explosion"]
                lista_bombas[i].actualizar(screen)
                del lista_bombas[i]
                self.vida -= 1
                break

    def colisionar_balas(self,lista_balas_enemigo):
        for i in range(len(lista_balas_enemigo)):
            if lista_balas_enemigo[i].rectangulo_principal.colliderect(self.rectangulo_principal):
                sonido_recibo_disparo.play()
                del lista_balas_enemigo[i]
                self.vida -= 1
                break

    def agarrar_llave(self, lista_items,puerta,enemigo):
        if len(lista_items) > 0:
            for i in range(len(lista_items)):
                if lista_items[i].rectangulo_principal.colliderect(self.smaller_rect):
                    sonido_llave.play()
                    del lista_items[i]
                    break
        elif len(lista_items) == 0  and enemigo.esta_muerto == True:
            puerta.animacion_actual = puerta.animaciones["abierta"]  
            puerta.animacion_actual = puerta.animaciones["final"]

    def agarrar_monedas(self, lista_items):
        if len(lista_items) > 0:
            for i in range(len(lista_items)):
                if lista_items[i].rectangulo_principal.colliderect(self.smaller_rect):
                    self.score += 100
                    sonido_moneda.play()
                    del lista_items[i]
                    break

