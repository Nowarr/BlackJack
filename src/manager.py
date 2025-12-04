"""Game manager module for BlackJack."""

from typing import TYPE_CHECKING

from src.card_dealer import Dealer

if TYPE_CHECKING:
    from src.bettor import Bettor
    from src.dummy import Dummy


class GameManager:
    """Manages the game state and orchestrates game flow.

    The GameManager handles checking for game over conditions
    and manages the card dealer.
    """

    def __init__(self) -> None:
        """Initialize the game manager with a card dealer."""
        self.dealer: Dealer = Dealer()

    def check_game_over(self, bettor: "Bettor", dummy: "Dummy") -> bool:
        """Check if the game is over and determine the winner.

        Args:
            bettor: The player making strategic decisions.
            dummy: The dealer/house player.

        Returns:
            True if the game is over, False otherwise.
        """
        bettor_value = bettor.calculate_hand_value()
        dummy_value = dummy.calculate_hand_value()

        if bettor_value > 21:
            print("Bettor busts. Dummy wins.")
            return True
        elif dummy_value > 21:
            print("Dummy busts. Bettor wins.")
            return True
        elif bettor_value == dummy_value:
            print("Push!")
            return True
        elif dummy_value > bettor_value:
            print("Dummy wins.")
            return True
        elif bettor_value > dummy_value:
            print("Bettor wins.")
            return True
        return False
