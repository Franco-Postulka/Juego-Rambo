from game import Game
from modulos.sonidos import sonido_fondo

game = Game((1200, 680),18)

game.set_caption('POO Game')
game.set_music(sonido_fondo)
game.set_volume(0.2)
game.play_music()

game.run()