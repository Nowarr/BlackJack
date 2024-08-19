import pygame

class Button:
    def __init__(self, screen, text, x, y, width, height, font, text_color, button_color):
        self.screen = screen
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.text_color = text_color
        self.button_color = button_color

    def draw(self):
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return self.rect.collidepoint(event.pos)

