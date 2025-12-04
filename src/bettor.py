"""Bettor (player) module for BlackJack."""

from typing import TYPE_CHECKING, List, Tuple

from src.colors import RESET, YELLOW

if TYPE_CHECKING:
    from src.dummy import Dummy
    from src.manager import GameManager


class Bettor:
    """Represents the player making strategic decisions in BlackJack.

    The Bettor follows a set of strategy rules based on the current hand
    value and the dealer's revealed card.
    """

    def __init__(self, manager: "GameManager", dummy: "Dummy") -> None:
        """Initialize the Bettor player.

        Args:
            manager: The game manager instance.
            dummy: The dealer/house player instance.
        """
        self.manager: "GameManager" = manager
        self.dummy: "Dummy" = dummy
        self.hand: List[Tuple[str, int, str]] = []
        self.is_soft: bool = False

    def reset_hand(self) -> None:
        """Clear the hand for a new round."""
        self.hand = []
        self.is_soft = False

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

    def hit(self) -> int:
        """Draw a new card and update hand value.

        Returns:
            The new hand value after hitting.
        """
        new_card = self.manager.dealer.deal()
        self.receive_card(new_card)

        value = self.calculate_hand_value()
        if value > 21 and self.is_soft:
            value -= 10
            self.is_soft = False

        return value

    def decision(self) -> None:
        """Make strategic decisions based on hand value and dealer's card.

        Implements basic BlackJack strategy:
        - Stand on 21
        - Hit on 11 or lower
        - Strategic decisions between 12-16 based on dealer's card
        - Stand on hard 17+, strategic play on soft 17
        - Aggressive play against dealer's 10 or Ace
        """
        dealer_revealed_card_value = self.dummy.hand[0][1]
        current_value = self.calculate_hand_value()

        # RULE #0: If Bettor has a hand of 21, always stand
        if current_value == 21:
            print(f"{YELLOW}Bettor stands with a hand of 21.{RESET}")
            return

        # RULE #1: If Bettor's hand value is 11 or lower, keep hitting
        while current_value <= 11:
            current_value = self.hit()
            print(f"{YELLOW}Bettor hits. New hand value: {current_value}{RESET}")
            if current_value > 21:
                return

        # RULE #2: Between 12 and 16
        while 12 <= current_value <= 16:
            if dealer_revealed_card_value >= 7:
                current_value = self.hit()
                print(
                    f"{YELLOW}Bettor hits based on strong dealer card. "
                    f"New hand value: {current_value}{RESET}"
                )
            else:
                print(
                    f"{YELLOW}Bettor stands on the basis that "
                    f"the dealer is likely to bust.{RESET}"
                )
                return
            if current_value > 21:
                return

        # RULE #3: 17 or higher
        while current_value >= 17:
            if not self.is_soft:
                print(f"{YELLOW}Bettor stands on a hard {current_value}.{RESET}")
                return
            else:
                if dealer_revealed_card_value >= 7:
                    current_value = self.hit()
                    print(
                        f"{YELLOW}Bettor hits on a soft 17. "
                        f"New hand value: {current_value}{RESET}"
                    )
                else:
                    print(f"{YELLOW}Bettor stands on a soft {current_value}.{RESET}")
                    return
            if current_value > 21:
                return

        # RULE #4: Dealer has 10 or Ace
        while dealer_revealed_card_value in (10, 11):
            if current_value <= 17:
                current_value = self.hit()
                print(
                    f"{YELLOW}Bettor hits based on strong dealer hand. "
                    f"New hand value: {current_value}{RESET}"
                )
                if current_value > 21:
                    return
            else:
                print(f"{YELLOW}Bettor stands on {current_value}.{RESET}")
                return
