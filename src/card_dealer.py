"""Card dealer module for BlackJack game."""

import random
from typing import Dict, List, Tuple


class Dealer:
    """Handles card dealing for the BlackJack game.

    Maintains a deck of cards and tracks dealt cards to ensure
    no more than 4 of each card type are dealt.
    """

    def __init__(self) -> None:
        """Initialize the dealer with a standard deck."""
        self.deck: Dict[str, int] = {
            "ace": 11,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "jack": 10,
            "queen": 10,
            "king": 10,
        }
        self.suits: List[str] = ["hearts", "clubs", "spades", "diamonds"]
        self.dealt_cards: Dict[Tuple[str, int, str], int] = {}

    def deal(self) -> Tuple[str, int, str]:
        """Deal a random card from the deck.

        Returns:
            A tuple containing (card_name, card_value, suit).

        Raises:
            ValueError: If the deck is empty (all cards dealt).
        """
        while True:
            card, value = random.choice(list(self.deck.items()))
            suit = random.choice(self.suits)
            dealt_card: Tuple[str, int, str] = (card, value, suit)

            if self.dealt_cards.get(dealt_card, 0) < 4:
                self.dealt_cards[dealt_card] = self.dealt_cards.get(dealt_card, 0) + 1
                return dealt_card

            if sum(self.dealt_cards.values()) == len(self.deck) * 4:
                raise ValueError("No more cards to deal. The deck is empty.")
