import pygame

from director import Director
from game_scene import GameScene
from menu_scene import MenuScene

pygame.init()

game_director = Director((800, 450), "Simple Ping Pong")

game_scene = GameScene(game_director, True)
menu_scene = MenuScene(game_director, game_scene)

game_scene.set_menu_scene(menu_scene)

game_director.change_scene(menu_scene)
game_director.loop()
