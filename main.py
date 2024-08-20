from random import weibullvariate
from src.game_logic import Dealer, Player
from src.phil import Phil
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

    def reveal(self):
        # player 1's cards
        value = [item for card in self.player1.hand for item in card if isinstance(item, int)]
        p1_cards = ', '.join(f"{card[0]} of {card[2]}" for card in self.player1.hand)
        print(f"Player 1's cards: {p1_cards} | {value[0] + value[1]}")
        # player 2's cards
        value_p2 = [item for card in self.player2.hand for item in card if isinstance(item, int)]
        p2_cards = ', '.join(f"{card[0]} of {card[2]}" for card in self.player2.hand)
        print(f"Player 2's hand: {p2_cards} | {value_p2[0] + value_p2[1]}")
    
    def philsDecision(self):

        def read():
            return[self.player2.hand[0]]

        def hit():
            new_card = self.dealer.deal()
            self.player1.receive_card(new_card)
            new_card = ', '.join(f"{card[0]} of {card[2]}" for card in self.player1.hand)
            value = [item for card in self.player1.hand for item in card if isinstance(item, int)]
            print(f"Player 1 chose to hit. New hand: {new_card} | {value[0] + value[1] + value[2]}")

        def stand():
            print("Player 1 is standing.")

        phil = Phil(read, hit, stand)
        phil.decision()

if __name__ == "__main__":
    game = Round()
    game.start_round()
    game.reveal()
    game.philsDecision()

