"""Button UI component for pygame interface."""

from typing import Tuple

import pygame


class Button:
    """A clickable button widget for pygame interfaces.

    Attributes:
        screen: The pygame surface to draw on.
        text: The text to display on the button.
        rect: The rectangular area of the button.
        font: The font to use for text rendering.
        text_color: RGB tuple for text color.
        button_color: RGB tuple for button background color.
    """

    def __init__(
        self,
        screen: pygame.Surface,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        font: pygame.font.Font,
        text_color: Tuple[int, int, int],
        button_color: Tuple[int, int, int],
    ) -> None:
        """Initialize a button.

        Args:
            screen: The pygame surface to draw on.
            text: The text to display on the button.
            x: X coordinate of the button's top-left corner.
            y: Y coordinate of the button's top-left corner.
            width: Width of the button.
            height: Height of the button.
            font: The font to use for text rendering.
            text_color: RGB tuple for text color.
            button_color: RGB tuple for button background color.
        """
        self.screen = screen
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.text_color = text_color
        self.button_color = button_color

    def draw(self) -> None:
        """Draw the button on the screen."""
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, event: pygame.event.Event) -> bool:
        """Check if the button was clicked.

        Args:
            event: The pygame event to check.

        Returns:
            True if the button was clicked, False otherwise.
        """
        return self.rect.collidepoint(event.pos)
