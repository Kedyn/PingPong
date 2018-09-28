import pygame

from director import Director
from game_scene import GameScene

pygame.init()

game_director = Director((800, 450), "Ping Pong")
game_scene = GameScene(game_director, True)
game_director.change_scene(game_scene)
game_director.loop()
