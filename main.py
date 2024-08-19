import random
from src.game_logic import Dealer, Player

class Round:
    def __init__(self):
        self.dealer = Dealer()
        self.player1 = Player()
        self.player2 = Player()  # This is our "dealer"
        self.start_round()

    def start_round(self):
        # Reset players' hands for each round
        self.player1.hand = []
        self.player2.hand = []

        # Initial hand to player 1
        for _ in range(2):
            card = self.dealer.deal()
            if card:  # Ensure card is available
                self.player1.receive_card(card)

        # Initial hand with one card revealed for "dealer" or player 2
        card = self.dealer.deal()
        if card:  # Ensure card is available
            self.player2.receive_card(card)

if __name__ == "__main__":
    game = Round()

