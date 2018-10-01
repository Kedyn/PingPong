import pygame
# import random

from pygame.sprite import Sprite


class Ball(Sprite):
    """Basic ball control."""

    def __init__(self, director, player_one_paddles, player_two_paddles):
        super().__init__()

        self.director = director
        self.player_one_paddles = player_one_paddles
        self.player_two_paddles = player_two_paddles

        self.image = pygame.image.load('assets/images/ball.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.screen_rect = director.screen.get_rect()

        self.rect = self.image.get_rect()

        self.direction_x = 0
        self.direction_y = 0

        self.reset()

        self.speed_factor = 1

    def reset(self):
        self.rect.center = self.screen_rect.center

        self.direction_x = 1
        self.direction_y = 1

    def update(self):
        for i in range(len(self.player_one_paddles)):
            if self.rect.colliderect(self.player_one_paddles[i].rect):
                if self.player_one_paddles[i].side is 1 or \
                   self.player_one_paddles[i].side is 5:
                    self.direction_x *= -1
                else:
                    self.direction_y *= -1
                break

        for i in range(len(self.player_two_paddles)):
            if self.rect.colliderect(self.player_two_paddles[i].rect):
                if self.player_two_paddles[i].side is 1 or \
                   self.player_two_paddles[i].side is 5:
                    self.direction_x *= -1
                else:
                    self.direction_y *= -1
                break

        self.rect.centerx += self.direction_x * self.speed_factor
        self.rect.centery += self.direction_y * self.speed_factor

    def render(self):
        self.director.screen.blit(self.image, self.rect)
