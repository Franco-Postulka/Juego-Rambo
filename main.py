import pygame, sys 
from boton import*
from Niveles.game import Game
from Niveles.game_2 import Game_2
from Niveles.game_3 import Game_3
from modulos.sonidos import*
from modulos.Imagenes import*
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((1200, 680))
pygame.display.set_caption("Menu")

fondo_menu = pygame.image.load(fondo_menu)
fondo_menu = pygame.transform.scale(fondo_menu,(1200,680))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(letra, size)

def play_level_1():
    game = Game((1200, 680), 18)
    game.set_caption('Nivel 1')
    game.set_music(sonido_fondo)
    game.set_volume(0.2)
    game.play_music()
    game.run()

def play_level_2():
    game = Game_2((1200, 680), 18)
    game.set_caption('Nivel 2')
    game.set_music(sonido_fondo_samurai)
    game.set_volume(0.1)
    game.play_music()
    game.run()

def play_level_3():
    game = Game_3((1200, 680), 18)
    game.set_caption('Nivel 2')
    game.set_music(sonido_fondo_mago)
    game.set_volume(0.1)
    game.play_music()
    game.run()
    



def main_menu():
    pygame.mixer.init()
    background = pygame.mixer.Sound(sonido_fondo_inicio)
    background.play(-1)
    while True:
        
        SCREEN.blit(fondo_menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(rectangulo), pos=(640, 250), 
                            text_input="NIVEL 1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(rectangulo), pos=(640, 400), 
                            text_input="NIVEL 2", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(rectangulo), pos=(640, 550), 
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
                    background.stop()
                    play_level_2()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    background.stop()
                    play_level_3()

        pygame.display.update()


while True:
    main_menu()