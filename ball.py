import pygame
import random

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

        self.reset()

        self.acceleration = 0

        direction = -1

        if random.randint(0, 1) is 1:
            direction = 1

        self.velocity_x = round(random.randint(0, 10) * 0.1 * direction, 1)
        self.velocity_y = round(random.randint(0, 10) * 0.1 * direction, 1)

        self.x = self.rect.centerx
        self.y = self.rect.centery

    def reset(self):
        self.rect.center = self.screen_rect.center

        self.x = self.rect.centerx
        self.y = self.rect.centery

        self.acceleration = 0

        direction = -1

        if random.randint(0, 1) is 1:
            direction = 1

        self.velocity_x = round(random.randint(0, 10) * 0.1 * direction, 1)
        self.velocity_y = round(random.randint(0, 10) * 0.1 * direction, 1)

    def update(self):
        for i in range(len(self.player_one_paddles)):
            if self.rect.colliderect(self.player_one_paddles[i].rect):
                if self.player_one_paddles[i].side is 1 or \
                   self.player_one_paddles[i].side is 5:
                    self.velocity_x = -1 * round(random.randrange(1, 10) * 0.1, 1)
                else:
                    self.velocity_y = -1 * round(random.randrange(1, 10) * 0.1, 1)
                break

        for i in range(len(self.player_two_paddles)):
            if self.rect.colliderect(self.player_two_paddles[i].rect):
                if self.player_two_paddles[i].side is 1 or \
                   self.player_two_paddles[i].side is 5:
                    self.velocity_x = -1 * round(random.randrange(1, 10) * 0.1, 1)
                else:
                    self.velocity_y = -1 * round(random.randrange(1, 10) * 0.1, 1)
                break

        self.x += self.velocity_x + self.acceleration
        self.y += self.velocity_y + self.acceleration

        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def render(self):
        self.director.screen.blit(self.image, self.rect)
