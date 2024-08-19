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
            card_p1 = self.dealer.deal()
	    card_p2 = self.dealer.deal()

            self.player1.receive_card(card_p1)
            self.player2.receive_card(card_p2)    
        #if card:  # Ensure card is available


if __name__ == "__main__":
    game = Round()

