import pygame.font


class Button():

    def __init__(self, rect, background, forecolor, screen, text):
        """Initialize button attributes."""
        self.screen = screen
        self.rect = rect

        self.background_color = background
        self.forecolor_color = forecolor
        self.font = pygame.font.SysFont(None, 48)

        self.prep_msg(text)

    def prep_msg(self, text):
        """Turn msg into a rendered image, and center text on the button."""
        self.text_image = self.font.render(text, True, self.forecolor_color,
                                           self.background_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
