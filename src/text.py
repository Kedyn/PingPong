import pygame.font


class Text():
    """Draws a text to the screen."""

    def __init__(self, rect, size, forecolor, screen, text):
        self.screen = screen
        self.rect = rect

        self.forecolor_color = forecolor
        self.font = pygame.font.SysFont(None, size)

        self.prep_msg(text)

    def prep_msg(self, text):
        """Turn msg into a rendered image, and center text on the button."""
        self.text_image = self.font.render(text, True, self.forecolor_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def render(self):
        self.screen.blit(self.text_image, self.text_image_rect)
