import pygame

from scene import Scene
from paddle import Paddle
from ball import Ball
from ai import AI
from text import Text


class GameScene(Scene):
    """Main game scene."""

    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director)

        self.background = background

        self.menu_scene = None

        self.ai_mode_on = False

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

        self.ai = AI(self.player_two, self.ball)

        self.intermission = True
        self.count_down = 300

        text_rect = pygame.Rect(0, 0, 500, 100)
        text_rect.center = self.screen_rect.center

        self.ready_text = Text(text_rect, 80, (0, 150, 0), director.screen,
                               "Ready?")
        self.set_text = Text(text_rect, 80, (0, 150, 0), director.screen,
                             "Set")
        self.go_text = Text(text_rect, 80, (0, 150, 0), director.screen, "Go!")

        self.player_one_score_rect = pygame.Rect(0, 30, 60, 60)
        self.player_one_score_rect.centerx = self.screen_rect.centerx - 80
        self.player_one_score_text = Text(self.player_one_score_rect, 80,
                                          (255, 255, 255), director.screen,
                                          "0")

        self.player_two_score_rect = pygame.Rect(0, 30, 60, 60)
        self.player_two_score_rect.centerx = self.screen_rect.centerx + 80
        self.player_two_score_text = Text(self.player_two_score_rect, 80,
                                          (255, 255, 255), director.screen,
                                          "0")

        self.play_up_to_text_rect = pygame.Rect(0, 120, 40, 40)
        self.play_up_to_text_rect.centerx = self.screen_rect.centerx
        self.play_up_to_text = Text(self.play_up_to_text_rect, 40, (140, 0, 0),
                                    director.screen, "7")

        self.player_one_score = 0
        self.player_two_score = 0
        self.play_up_to = 7

    def set_menu_scene(self, scene):
        self.menu_scene = scene

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

    def reset_board(self):
        for i in range(len(self.player_one)):
            self.player_one[i].reset()
        for i in range(len(self.player_two)):
            self.player_two[i].reset()

        self.ball.reset()

        self.count_down = 3000
        self.intermission = True

    def reset(self):
        self.reset_board()

        self.player_one_score = 0
        self.player_two_score = 0
        self.play_up_to = 7

        self.player_one_score_text.text = str(self.player_one_score)
        self.player_one_score_text.prep_img()

        self.player_two_score_text.text = str(self.player_two_score)
        self.player_two_score_text.prep_img()

        self.play_up_to_text.text = str(self.play_up_to)
        self.play_up_to_text.prep_img()

    def update(self):
        if self.intermission is False:
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
                if self.ball.rect.centerx > self.screen_rect.centerx:
                    self.player_one_score += 1
                    self.player_one_score_text.text = \
                        str(self.player_one_score)
                    self.player_one_score_text.prep_img()

                    if self.player_one_score is self.play_up_to:
                        self.menu_scene.reset()
                        self.director.scene = self.menu_scene
                else:
                    self.player_two_score += 1
                    self.player_two_score_text.text = \
                        str(self.player_two_score)
                    self.player_two_score_text.prep_img()

                    if self.player_two_score is self.play_up_to:
                        self.menu_scene.reset()
                        self.director.scene = self.menu_scene
                self.reset_board()

        else:
            if self.count_down is 0:
                self.intermission = False
            else:
                self.count_down -= 1

    def render(self):
        self.director.screen.fill(self.background)

        pygame.draw.line(self.director.screen, (200, 200, 200),
                         (self.screen_rect.centerx, 0),
                         (self.screen_rect.centerx, self.screen_rect.bottom))

        pygame.draw.rect(self.director.screen, (255, 255, 255),
                         self.player_one_score_rect, 1)
        self.player_one_score_text.render()

        pygame.draw.rect(self.director.screen, (255, 255, 255),
                         self.player_two_score_rect, 1)
        self.player_two_score_text.render()

        pygame.draw.rect(self.director.screen, (255, 255, 255),
                         self.play_up_to_text_rect, 1)
        self.play_up_to_text.render()

        for i in range(len(self.player_one)):
            self.player_one[i].render()
        for i in range(len(self.player_two)):
            self.player_two[i].render()

        self.ball.render()

        if self.intermission:
            if self.count_down > 2000:
                self.ready_text.render()
            elif self.count_down > 1000:
                self.set_text.render()
            else:
                self.go_text.render()
