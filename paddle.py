import pygame

from pygame.sprite import Sprite


class Paddle(Sprite):
    """Basic paddle control."""

    def __init__(self, director, side, color, keys):
        super().__init__()
        self.director = director
        self.side = side
        self.color = color
        self.keys = keys

        self.image = pygame.image.load('assets/images/' + color +
                                       '_paddle.png')
        self.image = pygame.transform.scale(self.image, (20, 100))

        if side is not 1 and side is not 5:
            self.image = pygame.transform.rotate(self.image, 90)

        self.screen_rect = director.screen.get_rect()

        self.rect = self.image.get_rect()

        self.moving_positive = False
        self.moving_negative = False

        self.reset()

        self.speed_factor = 1

        self.x = self.rect.centerx
        self.y = self.rect.centery

    def reset(self):
        if self.side is 1:
            self.rect.centery = self.screen_rect.centery
            self.rect.left = self.screen_rect.left
        elif self.side is 2:
            self.rect.centerx = self.screen_rect.centerx - 50
            self.rect.top = 0
        elif self.side is 3:
            self.rect.centerx = self.screen_rect.centerx - 50
            self.rect.bottom = self.screen_rect.bottom
        elif self.side is 4:
            self.rect.centerx = self.screen_rect.centerx + 50
            self.rect.top = 0
        elif self.side is 5:
            self.rect.centery = self.screen_rect.centery
            self.rect.right = self.screen_rect.right
        elif self.side is 6:
            self.rect.centerx = self.screen_rect.centerx + 50
            self.rect.bottom = self.screen_rect.bottom

        self.moving_positive = False
        self.moving_negative = False

        self.x = self.rect.centerx
        self.y = self.rect.centery

    def keydown(self, key):
        if key is self.keys[0]:
            self.moving_negative = True
        elif key is self.keys[1]:
            self.moving_positive = True

    def keyup(self, key):
        if key is self.keys[0]:
            self.moving_negative = False
        elif key is self.keys[1]:
            self.moving_positive = False

    def update(self):
        if self.side is 1 or self.side is 5:
            if self.moving_negative and self.rect.top > 0:
                self.y -= self.speed_factor
            if self.moving_positive and \
               self.rect.bottom < self.screen_rect.bottom:
                self.y += self.speed_factor
        else:
            if self.side is 2 or self.side is 3:
                if self.moving_negative and self.rect.left > 0:
                    self.x -= self.speed_factor
                if self.moving_positive and \
                   self.rect.right < self.screen_rect.centerx:
                    self.x += self.speed_factor
            else:
                if self.moving_negative and \
                   self.rect.left > self.screen_rect.centerx:
                    self.x -= self.speed_factor
                if self.moving_positive and \
                   self.rect.right < self.screen_rect.right:
                    self.x += self.speed_factor

        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def render(self):
        self.director.screen.blit(self.image, self.rect)
