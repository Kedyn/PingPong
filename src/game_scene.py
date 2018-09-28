import pygame

from scene import Scene
from paddle import Paddle


class GameScene(Scene):
    """Main game scene."""

    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director)

        self.background = background

        self.player_one = Paddle(director, 1, "blue", (pygame.K_w, pygame.K_s))

    def update(self):
        pass

    def render(self):
        self.director.screen.fill(self.background)

        self.player_one.render()
