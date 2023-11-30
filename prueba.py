
from Niveles.game_3 import Game_3
from modulos.sonidos import*

game = Game_3((1200, 680), 18)
game.set_caption('Nivel 2')
game.set_music(sonido_fondo_samurai)
game.set_volume(0.1)
game.play_music()
game.run()
