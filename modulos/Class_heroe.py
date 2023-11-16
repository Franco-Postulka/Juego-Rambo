from modulos.Configuraciones import *
from modulos.Class_personaje import Personaje

class Heroe(Personaje):
    def __init__(self, animaciones, vida, velocidad_animacion, tamaño, pos_x, pos_y, velocidad):
        super().__init__(animaciones, vida, velocidad_animacion, tamaño, pos_x, pos_y, velocidad)
        self.que_hace = "inicial"
        self.contador_pasos = 0

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
                self.animacion_actual  = self.animaciones["inicial"]
                self.animar(pantalla)

            case "Salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
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
    
    def aplicar_gravedad(self, pantalla, plataformas):
        tocando_plataforma = False
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
            
        for plataforma in plataformas:
            for i in range(self.rectangulo_principal.width):
                if plataforma.rect.collidepoint(self.rectangulo_principal.x + i ,self.rectangulo_principal.bottom):
                    self.desplazamiento_y = 0
                    self.esta_saltando = False
                    self.rectangulo_principal.bottom = plataforma.rect.top
                    tocando_plataforma = True  
                    break
        if not tocando_plataforma:
            self.esta_saltando = True
    
    