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

        self.acceleration = 0

        self.velocity_x = 0
        self.velocity_y = 0

        self.x = 0
        self.y = 0

        self.reset()

    def reset(self):
        self.rect.center = self.screen_rect.center

        self.x = self.rect.centerx
        self.y = self.rect.centery

        self.acceleration = 0

        self.velocity_x = round(random.choice((-1, 1)) * 0.2, 1)
        self.velocity_y = round(random.choice((-1, 1)) * 0.2, 1)

    def check_collision(self, paddles):
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                if paddle.side is 1 or paddle.side is 5:
                    self.velocity_x *= -1
                    if paddle.side is 1:
                        self.rect.left = paddle.rect.right
                    else:
                        self.rect.right = paddle.rect.left
                else:
                    self.velocity_y *= -1
                    if paddle.side is 2 or paddle.side is 4:
                        self.rect.top = paddle.rect.bottom
                    else:
                        self.rect.bottom = paddle.rect.top
                self.x = self.rect.centerx
                self.y = self.rect.centery
                break

    def update(self):
        self.check_collision(self.player_one_paddles)
        self.check_collision(self.player_two_paddles)

        self.x += self.velocity_x + self.acceleration
        self.y += self.velocity_y + self.acceleration

        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def render(self):
        self.director.screen.blit(self.image, self.rect)
