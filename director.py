# based on:
#   https://nicolasivanhoe.wordpress.com/2014/03/10/game-scene-manager-in-python-pygame/

import pygame
import sys


class Director:
    """Main game object.

    Manages scenes, events, and updates."""

    def __init__(self, resolution, title):
        self.screen = pygame.display.set_mode(resolution)

        pygame.display.set_caption(title)

        self.scene = None
        self.quit = False

    def loop(self):
        """Main game loop."""

        if self.scene is not None:
            while not self.quit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit = True
                    elif event.type == pygame.KEYDOWN:
                        self.scene.keydown(event.key)
                    elif event.type == pygame.KEYUP:
                        self.scene.keyup(event.key)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.scene.mousebuttondown(event.button, event.pos)

                self.scene.update()
                self.scene.render()

                pygame.display.flip()

            if self.quit:
                sys.exit()

    def change_scene(self, scene):
        self.scene = scene
