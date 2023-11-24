from game import Game

game = Game((1200, 680),18)

game.set_caption('POO Game')
game.set_music(r'recursos_rambo\sonidos\war_machines.wav')
game.set_volume(0.2)
game.play_music()

game.run()