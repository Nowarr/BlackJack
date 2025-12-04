"""Pygame implementation of BlackJack game."""

import sys
from typing import Optional, Tuple

import pygame

from src.bettor import Bettor
from src.dummy import Dummy
from src.game_visual.button import Button
from src.manager import GameManager


class BlackJackGame:
    """Main game class for the pygame implementation of BlackJack.

    Manages the pygame window, game state, and rendering.
    """

    # Color constants (RGB tuples)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    GREEN: Tuple[int, int, int] = (34, 139, 34)
    RED: Tuple[int, int, int] = (220, 20, 60)
    BLUE: Tuple[int, int, int] = (70, 130, 180)
    GOLD: Tuple[int, int, int] = (255, 215, 0)

    def __init__(self) -> None:
        """Initialize the pygame BlackJack game."""
        pygame.init()

        # Screen setup
        self.width: int = 1200
        self.height: int = 800
        self.screen: pygame.Surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("BlackJack")

        # Load fonts
        try:
            self.title_font: pygame.font.Font = pygame.font.Font(
                "resources/EBG-Reg.ttf", 72
            )
            self.font: pygame.font.Font = pygame.font.Font("resources/EBG-Reg.ttf", 36)
            self.small_font: pygame.font.Font = pygame.font.Font(
                "resources/EBG-Reg.ttf", 24
            )
        except FileNotFoundError:
            # Fallback to default font if custom fonts not found
            self.title_font = pygame.font.Font(None, 72)
            self.font = pygame.font.Font(None, 36)
            self.small_font = pygame.font.Font(None, 24)

        # Game state
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
        self.game_state: str = "menu"  # menu, playing, game_over
        self.manager: Optional[GameManager] = None
        self.bettor: Optional[Bettor] = None
        self.dummy: Optional[Dummy] = None
        self.message: str = ""
        self.round_active: bool = False

        # Create buttons (initialized in _create_buttons)
        self.start_button: Button
        self.hit_button: Button
        self.stand_button: Button
        self.play_again_button: Button
        self.quit_button: Button
        self._create_buttons()

    def _create_buttons(self) -> None:
        """Create all buttons used in the game."""
        # Menu buttons
        self.start_button = Button(
            self.screen,
            "Start Game",
            self.width // 2 - 100,
            self.height // 2,
            200,
            60,
            self.font,
            self.WHITE,
            self.GREEN,
        )
        self.quit_button = Button(
            self.screen,
            "Quit",
            self.width // 2 - 100,
            self.height // 2 + 100,
            200,
            60,
            self.font,
            self.WHITE,
            self.RED,
        )

        # Game buttons
        self.hit_button = Button(
            self.screen,
            "Hit",
            self.width // 2 - 220,
            self.height - 100,
            200,
            60,
            self.font,
            self.WHITE,
            self.BLUE,
        )
        self.stand_button = Button(
            self.screen,
            "Stand",
            self.width // 2 + 20,
            self.height - 100,
            200,
            60,
            self.font,
            self.WHITE,
            self.RED,
        )

        # Game over button
        self.play_again_button = Button(
            self.screen,
            "Play Again",
            self.width // 2 - 100,
            self.height - 150,
            200,
            60,
            self.font,
            self.WHITE,
            self.GREEN,
        )

    def start_new_game(self) -> None:
        """Initialize a new game round."""
        self.manager = GameManager()
        self.dummy = Dummy(self.manager)
        self.bettor = Bettor(self.manager, self.dummy)

        # Deal initial cards
        self.bettor.reset_hand()
        self.dummy.reset_hand()
        for _ in range(2):
            self.bettor.receive_card(self.manager.dealer.deal())
            self.dummy.receive_card(self.manager.dealer.deal())

        self.game_state = "playing"
        self.round_active = True
        self.message = "Your turn!"

        # Check for immediate blackjack
        if self.bettor.calculate_hand_value() == 21:
            self.message = "BlackJack! You win!"
            self.game_state = "game_over"

    def handle_hit(self) -> None:
        """Handle player hitting (drawing a card)."""
        if not self.bettor or not self.round_active:
            return

        value = self.bettor.hit()
        if value > 21:
            self.message = "Bust! You lose!"
            self.game_state = "game_over"
            self.round_active = False
        elif value == 21:
            self.handle_stand()

    def handle_stand(self) -> None:
        """Handle player standing (dealer's turn)."""
        if (
            not self.dummy
            or not self.bettor
            or not self.round_active
            or not self.manager
        ):
            return

        # Dealer plays
        while self.dummy.calculate_hand_value() < 17:
            self.dummy.receive_card(self.manager.dealer.deal())

        # Determine winner
        bettor_value = self.bettor.calculate_hand_value()
        dummy_value = self.dummy.calculate_hand_value()

        if dummy_value > 21:
            self.message = "Dealer busts! You win!"
        elif bettor_value > dummy_value:
            self.message = "You win!"
        elif bettor_value < dummy_value:
            self.message = "Dealer wins!"
        else:
            self.message = "Push! It's a tie!"

        self.game_state = "game_over"
        self.round_active = False

    def draw_card(
        self, x: int, y: int, card: Tuple[str, int, str], hidden: bool = False
    ) -> None:
        """Draw a card on the screen.

        Args:
            x: X coordinate for the card.
            y: Y coordinate for the card.
            card: Tuple of (card_name, card_value, suit).
            hidden: If True, draw card face-down.
        """
        # Card rectangle
        card_rect = pygame.Rect(x, y, 100, 140)
        pygame.draw.rect(self.screen, self.WHITE, card_rect)
        pygame.draw.rect(self.screen, self.BLACK, card_rect, 2)

        if not hidden:
            # Draw card name and suit
            card_text = self.small_font.render(card[0].title(), True, self.BLACK)
            suit_text = self.small_font.render(card[2].title(), True, self.BLACK)
            self.screen.blit(card_text, (x + 10, y + 10))
            self.screen.blit(suit_text, (x + 10, y + 110))

            # Draw suit symbol in the middle
            suit_symbol = {"hearts": "♥", "diamonds": "♦", "clubs": "♣", "spades": "♠"}
            symbol = suit_symbol.get(card[2], "")
            suit_color = self.RED if card[2] in ["hearts", "diamonds"] else self.BLACK
            symbol_text = self.font.render(symbol, True, suit_color)
            symbol_rect = symbol_text.get_rect(center=(x + 50, y + 70))
            self.screen.blit(symbol_text, symbol_rect)
        else:
            # Draw card back
            back_text = self.title_font.render("?", True, self.BLUE)
            back_rect = back_text.get_rect(center=(x + 50, y + 70))
            self.screen.blit(back_text, back_rect)

    def draw_menu(self) -> None:
        """Draw the main menu screen."""
        self.screen.fill(self.GREEN)

        # Title
        title_text = self.title_font.render("BlackJack", True, self.GOLD)
        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 3))
        self.screen.blit(title_text, title_rect)

        # Buttons
        self.start_button.draw()
        self.quit_button.draw()

    def draw_playing(self) -> None:
        """Draw the playing screen."""
        self.screen.fill(self.GREEN)

        if not self.bettor or not self.dummy:
            return

        # Title
        title_text = self.font.render("BlackJack", True, self.GOLD)
        self.screen.blit(title_text, (20, 20))

        # Dealer's hand
        dealer_text = self.small_font.render("Dealer's Hand", True, self.WHITE)
        self.screen.blit(dealer_text, (50, 100))

        # Draw dealer's cards (hide second card if round active)
        for i, card in enumerate(self.dummy.hand):
            hidden = i == 1 and self.round_active
            self.draw_card(50 + i * 120, 140, card, hidden=hidden)

        # Show dealer's value (only first card if round active)
        if self.round_active:
            dealer_value = self.dummy.hand[0][1]
            value_text = self.small_font.render(
                f"Showing: {dealer_value}", True, self.WHITE
            )
        else:
            dealer_value = self.dummy.calculate_hand_value()
            value_text = self.small_font.render(
                f"Total: {dealer_value}", True, self.WHITE
            )
        self.screen.blit(value_text, (50, 300))

        # Player's hand
        player_text = self.small_font.render("Your Hand", True, self.WHITE)
        self.screen.blit(player_text, (50, 450))

        # Draw player's cards
        for i, card in enumerate(self.bettor.hand):
            self.draw_card(50 + i * 120, 490, card)

        # Show player's value
        player_value = self.bettor.calculate_hand_value()
        player_value_text = self.small_font.render(
            f"Total: {player_value}", True, self.WHITE
        )
        self.screen.blit(player_value_text, (50, 650))

        # Message
        if self.message:
            message_text = self.font.render(self.message, True, self.GOLD)
            message_rect = message_text.get_rect(
                center=(self.width // 2, self.height - 180)
            )
            self.screen.blit(message_text, message_rect)

        # Buttons
        if self.round_active:
            self.hit_button.draw()
            self.stand_button.draw()

    def draw_game_over(self) -> None:
        """Draw the game over screen."""
        self.draw_playing()  # Show final state
        self.play_again_button.draw()
        self.quit_button.draw()

    def handle_events(self) -> None:
        """Process pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_state == "menu":
                    if self.start_button.is_clicked(event):
                        self.start_new_game()
                    elif self.quit_button.is_clicked(event):
                        self.running = False

                elif self.game_state == "playing" and self.round_active:
                    if self.hit_button.is_clicked(event):
                        self.handle_hit()
                    elif self.stand_button.is_clicked(event):
                        self.handle_stand()

                elif self.game_state == "game_over":
                    if self.play_again_button.is_clicked(event):
                        self.start_new_game()
                    elif self.quit_button.is_clicked(event):
                        self.running = False

    def run(self) -> None:
        """Main game loop."""
        while self.running:
            self.handle_events()

            # Draw based on game state
            if self.game_state == "menu":
                self.draw_menu()
            elif self.game_state == "playing":
                self.draw_playing()
            elif self.game_state == "game_over":
                self.draw_game_over()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


def main() -> None:
    """Entry point for the pygame version."""
    game = BlackJackGame()
    game.run()


if __name__ == "__main__":
    main()
