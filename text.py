import pygame.font
import copy


class Text:
    """Draws a text to the screen."""

    def __init__(self, rect, size, color, screen, text):
        self.screen = screen
        self.rect = copy.deepcopy(rect)
        self.text = text

        self.color = color
        self.font = pygame.font.SysFont(None, size)

        self.text_image = None
        self.text_image_rect = None

        self.prep_img()

    def prep_img(self):
        """Turn msg into a rendered image, and center text on the button."""
        self.text_image = self.font.render(self.text, True,
                                           self.color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def render(self):
        self.screen.blit(self.text_image, self.text_image_rect)
