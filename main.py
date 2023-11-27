import pygame, sys 
from boton import*
from Niveles.game import Game
from modulos.sonidos import sonido_fondo
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((1200, 680))
pygame.display.set_caption("Menu")

BG = pygame.image.load("recursos_rambo\imagenes\Inicio.jpg")
BG = pygame.transform.scale(BG,(1200,680))

BG1 = pygame.image.load(r"recursos_rambo\imagenes\rambos_revange.jpeg")
BG1 = pygame.transform.scale(BG,(1200,680))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("recursos_rambo\.ttf", size)

def play_level_1():
    game = Game((1200, 680), 18)
    game.set_caption('Nivel 1')
    game.set_music(sonido_fondo)
    game.set_volume(0.2)
    game.play_music()
    game.run()

def main_menu():
    pygame.mixer.init()
    background = pygame.mixer.Sound(r'recursos_rambo\sonidos\badlands.wav')
    background.play(-1)
    while True:
        
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(r"recursos_rambo\imagenes\rectangulo.png"), pos=(640, 250), 
                            text_input="NIVEL 1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(r"recursos_rambo\imagenes\rectangulo.png"), pos=(640, 400), 
                            text_input="NIVEL 2", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(r"recursos_rambo\imagenes\rectangulo.png"), pos=(640, 550), 
                            text_input="NIVEL 3", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    background.stop()
                    play_level_1()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_level_1()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_level_1()

        pygame.display.update()

main_menu()