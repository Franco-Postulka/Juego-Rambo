
from Niveles.game_2 import Game_2
from modulos.sonidos import*

game = Game_2((1200, 680), 18)
game.set_caption('Nivel 2')
game.set_music(sonido_fondo)
game.set_volume(0.2)
game.play_music()
game.run()
