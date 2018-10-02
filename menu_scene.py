import pygame
import random

from scene import Scene
from text import Text


class MenuScene(Scene):
    """Menu scene."""

    def __init__(self, director, game_scene, background=(0, 0, 0)):
        super().__init__(director)

        self.game_scene = game_scene

        self.background = background

        text_rect = pygame.Rect(0, 0, 300, 140)
        text_rect.centerx = director.screen.get_rect().centerx

        self.logo = Text(text_rect, 140, (255, 255, 255), director.screen,
                         "PONG")

        text_rect.centery = 120

        self.header = Text(text_rect, 50, (0, 140, 0), director.screen,
                           "AI -- NO WALLS")

        text_rect.centerx = self.header.rect.left + 40
        text_rect.centery += 2

        self.subheader = Text(text_rect, 60, (140, 0, 0), director.screen,
                              "X")

        play_rect = pygame.Rect(0, 0, 100, 30)
        play_rect.center = director.screen.get_rect().center
        play_rect.centery -= 20

        self.play_human_text = Text(play_rect, 30, (255, 255, 255),
                                    director.screen, "PLAY AGAINST HUMAN")

        play_rect.centery += 40

        self.play_ai_text = Text(play_rect, 30, (255, 255, 255),
                                 director.screen, "PLAY AGAINST AI")

        play_rect.centery += 80
        play_rect.centerx -= 100

        self.play_difficulty_text = Text(play_rect, 30, (200, 200, 200),
                                         director.screen, "Difficulty Level:")

        play_rect.centerx += 130

        self.play_easy = Text(play_rect, 30, (140, 0, 0), director.screen,
                              "EASY")

        play_rect.centerx += 100

        self.play_avg = Text(play_rect, 30, (255, 255, 255), director.screen,
                             "AVERAGE")

        play_rect.centerx += 130

        self.play_hard = Text(play_rect, 30, (255, 255, 255), director.screen,
                              "DIFFICULT")

        play_rect.centerx -= 334
        play_rect.centery += 40

        self.play_up_to_text = Text(play_rect, 30, (200, 200, 200),
                                    director.screen, "Play up to:")

        play_rect.centerx += 80

        self.up_to_seven = Text(play_rect, 30, (140, 0, 0),
                                director.screen, "7")

        play_rect.centerx += 80

        self.up_to_eleven = Text(play_rect, 30, (255, 255, 255),
                                 director.screen, "11")

        play_rect.centerx += 80

        self.up_to_fifteen = Text(play_rect, 30, (255, 255, 255),
                                  director.screen, "15")

        play_rect.centerx += 80

        self.up_to_twentyone = Text(play_rect, 30, (255, 255, 255),
                                    director.screen, "21")

        self.mouse_on = None
        self.difficulty = "easy"
        self.play_up_to = 7

    def reset(self):
        self.mouse_on = None
        self.difficulty = "easy"
        self.play_up_to = 7

        self.play_human_text.color = (255, 255, 255)
        self.play_human_text.prep_img()
        self.play_ai_text.color = (255, 255, 255)
        self.play_ai_text.prep_img()
        self.play_easy.color = (140, 0, 0)
        self.play_easy.prep_img()
        self.play_avg.color = (255, 255, 255)
        self.play_avg.prep_img()
        self.play_hard.color = (255, 255, 255)
        self.play_hard.prep_img()
        self.up_to_seven.color = (140, 0, 0)
        self.up_to_seven.prep_img()
        self.up_to_eleven.color = (255, 255, 255)
        self.up_to_eleven.prep_img()
        self.up_to_fifteen.color = (255, 255, 255)
        self.up_to_fifteen.prep_img()
        self.up_to_twentyone.color = (255, 255, 255)
        self.up_to_twentyone.prep_img()

    def __changedifficulty(self):
        if self.difficulty is "easy":
            self.play_easy.color = (255, 255, 255)
            self.play_easy.prep_img()
        elif self.difficulty is "average":
            self.play_avg.color = (255, 255, 255)
            self.play_avg.prep_img()
        elif self.difficulty is "hard":
            self.play_hard.color = (255, 255, 255)
            self.play_hard.prep_img()

    def __changepoints(self):
        if self.play_up_to is 7:
            self.up_to_seven.color = (255, 255, 255)
            self.up_to_seven.prep_img()
        elif self.play_up_to is 11:
            self.up_to_eleven.color = (255, 255, 255)
            self.up_to_eleven.prep_img()
        elif self.play_up_to is 15:
            self.up_to_fifteen.color = (255, 255, 255)
            self.up_to_fifteen.prep_img()
        elif self.play_up_to is 21:
            self.up_to_twentyone.color = (255, 255, 255)
            self.up_to_twentyone.prep_img()

    def mousebuttondown(self, button, point):
        self.mouse_on = None

        if self.play_human_text.text_image_rect.collidepoint(point[0],
                                                             point[1]):
            self.game_scene.ai_mode_on = False
            self.game_scene.play_up_to = self.play_up_to
            self.game_scene.reset()
            self.director.scene = self.game_scene
        elif self.play_ai_text.text_image_rect.collidepoint(point[0],
                                                            point[1]):
            self.game_scene.ai_mode_on = True
            self.game_scene.play_up_to = self.play_up_to
            self.game_scene.ai.set_difficulty(self.difficulty)
            self.game_scene.reset()
            self.director.scene = self.game_scene
        elif self.play_human_text.text_image_rect.collidepoint(point[0],
                                                               point[1]):
            self.mouse_on = self.play_human_text
        elif self.play_ai_text.text_image_rect.collidepoint(point[0],
                                                            point[1]):
            self.mouse_on = self.play_ai_text
        elif self.difficulty is not "easy" and \
                self.play_easy.text_image_rect.collidepoint(point[0],
                                                            point[1]):
            self.__changedifficulty()
            self.difficulty = "easy"
            self.play_easy.color = (140, 0, 0)
            self.play_easy.prep_img()
        elif self.difficulty is not "average" and \
                self.play_avg.text_image_rect.collidepoint(point[0],
                                                           point[1]):
            self.__changedifficulty()
            self.difficulty = "average"
            self.play_avg.color = (140, 0, 0)
            self.play_avg.prep_img()
        elif self.difficulty is not "hard" and \
                self.play_hard.text_image_rect.collidepoint(point[0],
                                                            point[1]):
            self.__changedifficulty()
            self.difficulty = "hard"
            self.play_hard.color = (140, 0, 0)
            self.play_hard.prep_img()
        elif self.play_up_to is not 7 and \
                self.up_to_seven.text_image_rect.collidepoint(point[0],
                                                              point[1]):
            self.__changepoints()
            self.play_up_to = 7
            self.up_to_seven.color = (140, 0, 0)
            self.up_to_seven.prep_img()
        elif self.play_up_to is not 11 and \
                self.up_to_eleven.text_image_rect.collidepoint(point[0],
                                                               point[1]):
            self.__changepoints()
            self.play_up_to = 11
            self.up_to_eleven.color = (140, 0, 0)
            self.up_to_eleven.prep_img()
        elif self.play_up_to is not 15 and \
                self.up_to_fifteen.text_image_rect.collidepoint(point[0],
                                                                point[1]):
            self.__changepoints()
            self.play_up_to = 15
            self.up_to_fifteen.color = (140, 0, 0)
            self.up_to_fifteen.prep_img()
        elif self.play_up_to is not 21 and \
                self.up_to_twentyone.text_image_rect.collidepoint(point[0],
                                                                  point[1]):
            self.__changepoints()
            self.play_up_to = 21
            self.up_to_twentyone.color = (140, 0, 0)
            self.up_to_twentyone.prep_img()

    def update(self):
        point = pygame.mouse.get_pos()

        if self.mouse_on is not None:
            self.mouse_on.color = (255, 255, 255)
            self.mouse_on.prep_img()
            self.mouse_on = None

        if self.play_human_text.text_image_rect.collidepoint(point[0],
                                                             point[1]):
            self.mouse_on = self.play_human_text
        elif self.play_ai_text.text_image_rect.collidepoint(point[0],
                                                            point[1]):
            self.mouse_on = self.play_ai_text
        elif self.difficulty is not "easy" and \
                self.play_easy.text_image_rect.collidepoint(point[0],
                                                            point[1]):
            self.mouse_on = self.play_easy
        elif self.difficulty is not "average" and \
                self.play_avg.text_image_rect.collidepoint(point[0],
                                                           point[1]):
            self.mouse_on = self.play_avg
        elif self.difficulty is not "hard" and \
                self.play_hard.text_image_rect.collidepoint(point[0],
                                                            point[1]):
            self.mouse_on = self.play_hard
        elif self.play_up_to is not 7 and \
                self.up_to_seven.text_image_rect.collidepoint(point[0],
                                                              point[1]):
            self.mouse_on = self.up_to_seven
        elif self.play_up_to is not 11 and \
                self.up_to_eleven.text_image_rect.collidepoint(point[0],
                                                               point[1]):
            self.mouse_on = self.up_to_eleven
        elif self.play_up_to is not 15 and \
                self.up_to_fifteen.text_image_rect.collidepoint(point[0],
                                                                point[1]):
            self.mouse_on = self.up_to_fifteen
        elif self.play_up_to is not 21 and \
                self.up_to_twentyone.text_image_rect.collidepoint(point[0],
                                                                  point[1]):
            self.mouse_on = self.up_to_twentyone

    def render(self):
        self.director.screen.fill(self.background)

        self.logo.render()
        self.header.render()

        if random.randint(0, 1) is 1:
            self.subheader.render()

        if self.mouse_on is not None:
            self.mouse_on.color = (140, 0, 0)
            self.mouse_on.prep_img()

        self.play_human_text.render()
        self.play_ai_text.render()
        self.play_difficulty_text.render()
        self.play_easy.render()
        self.play_avg.render()
        self.play_hard.render()
        self.play_up_to_text.render()
        self.up_to_seven.render()
        self.up_to_eleven.render()
        self.up_to_fifteen.render()
        self.up_to_twentyone.render()
