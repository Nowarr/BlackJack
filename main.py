"""BlackJack game - CLI implementation."""

from typing import Tuple

from src.bettor import Bettor
from src.dummy import Dummy
from src.manager import GameManager

# ANSI escape sequences for colors
RESET: str = "\033[0m"
BLUE: str = "\033[34m"
RED: str = "\033[31m"


class Round:
    """Represents a single round of BlackJack.

    Manages the game flow including dealing cards, player decisions,
    and determining the winner.
    """

    def __init__(self) -> None:
        """Initialize a new round with fresh game state."""
        self.manager: GameManager = GameManager()
        self.dummy: Dummy = Dummy(self.manager)
        self.bettor: Bettor = Bettor(self.manager, self.dummy)
        self.is_running: bool = True

    def start_round(self) -> None:
        """Start a new round by dealing initial cards."""
        # Fresh hands at start of round
        self.bettor.reset_hand()
        self.dummy.reset_hand()

        # Initial cards are dealt
        for _ in range(2):
            self.bettor.receive_card(self.manager.dealer.deal())
            self.dummy.receive_card(self.manager.dealer.deal())

    def reveal(self) -> None:
        """Display the initial cards for both players.

        For the dummy (dealer), only one card is shown to the bettor.
        """
        bettor_cards = ", ".join(f"{card[0]} of {card[2]}" for card in self.bettor.hand)
        bettor_value = self.bettor.calculate_hand_value()
        print("------------------------------------------------")
        print(f"{BLUE}Bettor's cards{RESET}: {bettor_cards} | {bettor_value}")

        dummy_first_card: Tuple[str, int, str] = self.dummy.hand[0]
        dummy_initial_hand = (
            f"{dummy_first_card[0]} of {dummy_first_card[2]}"  # Only show first card
        )
        print(
            f"{RED}Dummy's revealed card{RESET}: "
            f"{dummy_initial_hand} | {dummy_first_card[1]}"
        )
        print("------------------------------------------------")

    def game_loop(self) -> None:
        """Execute the main game loop for a single round."""
        while self.is_running:
            print("\n\n")
            self.reveal()
            self.bettor.decision()
            self.dummy.response()

            if self.manager.check_game_over(self.bettor, self.dummy):
                print("Game Over")
                self.is_running = False
                break


def main() -> None:
    """Run the main game loop."""
    while True:
        for _ in range(3):
            round_instance = Round()
            round_instance.start_round()
            round_instance.game_loop()

        inp = input("\n\nSimulation over. Run again? (y/n): ")
        if inp.lower() != "y":
            break


if __name__ == "__main__":
    main()
