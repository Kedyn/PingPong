import pygame

from scene import Scene
from paddle import Paddle
from ball import Ball
from ai import AI
from text import Text


class GameScene(Scene):
    """Main game scene."""

    def __init__(self, director, ai=False, background=(0, 0, 0)):
        super().__init__(director)

        self.background = background

        self.ai_mode_on = ai

        self.screen_rect = director.screen.get_rect()

        self.player_one = [Paddle(director, 1, "blue",
                                  [pygame.K_w, pygame.K_s]),
                           Paddle(director, 2, "blue",
                                  [pygame.K_a, pygame.K_d]),
                           Paddle(director, 3, "blue",
                                  [pygame.K_a, pygame.K_d])]

        self.player_two = [Paddle(director, 4, "red",
                                  [pygame.K_j, pygame.K_l]),
                           Paddle(director, 5, "red",
                                  [pygame.K_i, pygame.K_k]),
                           Paddle(director, 6, "red",
                                  [pygame.K_j, pygame.K_l])]

        self.ball = Ball(director, self.player_one, self.player_two)

        if ai:
            self.ai = AI(self.player_two, self.ball)

        self.intermision = True
        self.count_down = 300

        text_rect = pygame.Rect(0, 0, 500, 100)
        text_rect.center = self.screen_rect.center

        self.ready_text = Text(text_rect, 80, (0, 150, 0), director.screen,
                               "Ready?")
        self.set_text = Text(text_rect, 80, (0, 150, 0), director.screen, "Set")
        self.go_text = Text(text_rect, 80, (0, 150, 0), director.screen, "Go!")

    def keydown(self, key):
        for i in range(len(self.player_one)):
            self.player_one[i].keydown(key)
        for i in range(len(self.player_two)):
            self.player_two[i].keydown(key)

    def keyup(self, key):
        for i in range(len(self.player_one)):
            self.player_one[i].keyup(key)
        for i in range(len(self.player_two)):
            self.player_two[i].keyup(key)

    def update(self):
        if self.intermision is False:
            for i in range(len(self.player_one)):
                self.player_one[i].update()
            for i in range(len(self.player_two)):
                self.player_two[i].update()

            if self.ai_mode_on:
                self.ai.update()

            self.ball.update()

            if self.ball.rect.top <= 0 or \
               self.ball.rect.bottom >= self.screen_rect.bottom or \
               self.ball.rect.left <= 0 or \
               self.ball.rect.right >= self.screen_rect.right:
                for i in range(len(self.player_one)):
                    self.player_one[i].reset()
                for i in range(len(self.player_two)):
                    self.player_two[i].reset()

                self.ball.reset()

                self.count_down = 300
                self.intermision = True

        else:
            if self.count_down is 0:
                self.intermision = False
            else:
                self.count_down -= 1

    def render(self):
        self.director.screen.fill(self.background)

        for i in range(len(self.player_one)):
            self.player_one[i].render()
        for i in range(len(self.player_two)):
            self.player_two[i].render()

        self.ball.render()

        if self.intermision:
            if self.count_down > 200:
                self.ready_text.render()
            elif self.count_down > 100:
                self.set_text.render()
            else:
                self.go_text.render()
