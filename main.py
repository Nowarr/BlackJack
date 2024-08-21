from src.game_logic import Dealer, Player
from src.phil import Phil
from src.mark import Mark

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
        # player 2's initially revealed card
        value_p2 = [item for card in self.player2.hand for item in card if isinstance(item, int)]
        p2_first_card = self.player2.hand[0]
        p2_initial_hand = f"{p2_first_card[0]} of {p2_first_card[2]}"
        print(f"Player 2's revealed card: {p2_initial_hand} | {value_p2[0]}")
    
    def philsDecision(self):

        def read():
            # the dealers initially reveled card is read by phil
            p2_revealed_card = self.player2.hand[0][1]
            # phil also reads his current hand before making a decison
            p1_hand = [item for card in self.player1.hand for item in card if isinstance(item, int)]
            return p2_revealed_card, p1_hand

        def hit():
            # deal new card to player 1
            new_card = self.dealer.deal()
            self.player1.receive_card(new_card) # this updates the players current hand
            
            # format the new hand
            new_hand = ', '.join(f"{card[0]} of {card[2]}" for card in self.player1.hand) 
            
            # extract int values and calculate the total
            value = [item for card in self.player1.hand for item in card if isinstance(item, int)]
            total_value = sum(value)

            # print the new hand
            print(f"Player 1 chose to hit. New hand: {new_hand} | {total_value}")
            
            return total_value

        def stand():
            pass

        phil = Phil(read, hit, stand)
        phil.decision()

    def markResponse(self):

        def read():
            p1_final_hand = [item for card in self.player1.hand for item in card if isinstance(item, int)]
            return p1_final_hand
        def response():

            new_card = self.dealer.deal()
            self.player2.receive_card(new_card) # update player 2's hand
                
            # format new hand and extract int value
            new_hand = ', '.join(f"{card[0]} of {card[2]}" for card in self.player2.hand)
            value = [item for card in self.player2.hand for item in card if isinstance(item, int)]
            total_value = sum(value)

            # print new hand
            print(f"Player 2's revealed hand: {new_hand} | {total_value}")
            
            return new_hand, total_value

        mark = Mark(read, response)
        mark.response()

if __name__ == "__main__":
    game = Round()
    game.start_round()
    game.reveal()
    game.philsDecision()
    game.markResponse()
