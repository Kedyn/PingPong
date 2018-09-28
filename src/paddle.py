import pygame

from pygame.sprite import Sprite


class Paddle(Sprite):
    """"""

    def __init__(self, director, side, color, keys):
        self.director = director
        self.color = color
        self.keys = keys

        self.image = pygame.image.load('assets/images/' + color +
                                       '_paddle.png')
        self.screen_rect = director.screen.get_rect()

        self.rect = pygame.Rect(0, 0, 40, 100)

        # self.rect.centery = self.screen_rect.centery

    def render(self):
        self.director.screen.blit(self.image, pygame.Rect(10, 0, 40, 100))
