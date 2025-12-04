"""Dummy (dealer) player module for BlackJack."""

from typing import TYPE_CHECKING, List, Tuple

from src.colors import RED, RESET

if TYPE_CHECKING:
    from src.manager import GameManager


class Dummy:
    """Represents the dealer/house player in BlackJack.

    The Dummy follows standard dealer rules: hits on 16 or below,
    stands on 17 or above.
    """

    def __init__(self, manager: "GameManager") -> None:
        """Initialize the Dummy player.

        Args:
            manager: The game manager instance.
        """
        self.manager: "GameManager" = manager
        self.hand: List[Tuple[str, int, str]] = []

    def reset_hand(self) -> None:
        """Clear the hand for a new round."""
        self.hand = []

    def receive_card(self, card: Tuple[str, int, str]) -> None:
        """Add a card to the hand.

        Args:
            card: A tuple of (card_name, card_value, suit).
        """
        self.hand.append(card)

    def calculate_hand_value(self) -> int:
        """Calculate the total value of the hand.

        Returns:
            The sum of all card values in the hand.
        """
        value = [item for card in self.hand for item in card if isinstance(item, int)]
        return sum(value)

    def response(self) -> None:
        """Execute dealer's turn following standard dealer rules.

        Dealer hits on 16 or below and stands on 17 or above.
        """
        while self.calculate_hand_value() < 17:
            new_card = self.manager.dealer.deal()
            self.receive_card(new_card)
            new_value = self.calculate_hand_value()
            print(f"{RED}Dummy hits. New hand value: {new_value}{RESET}")

        final_value = self.calculate_hand_value()
        if final_value > 21:
            print(f"{RED}Dummy busts.{RESET}")
        else:
            print(f"{RED}Dummy stands with {final_value}.{RESET}")
