


"""
PHIL
TODO:
    - Must read revealed cards in main game loop
    - Must make decisions based on initial hand and sole
    revealed card of player 2
"""

import random

class Phil:
    def __init__(self, read, hit, stand):
        self.read = read
        self.hit = hit
        self.stand = stand
        self.is_soft = False

    def hit(self):
        card_value = random.randint(2, 11) 
        _, p1_cards = self.read()
        p1_hand = sum(p1_cards)
    

        # if phils cards are 11 or below, always hit. he can't bust no matter what
        if card_value == 11:
            if p1_hand + card_value > 21:
                card_value = 1
            else:
                self.is_soft = True

        p1_hand += card_value
        print(f"Player 1 draws a card worth {card_value} New hand value is {p1_hand}.")

        if p1_hand > 21 and self.is_soft:
            p1_hand -= 10
            self.is_soft = False
            print(f"Player 1 converts an Ace to 1. New hand value is {p1_hand}.")
        
        return p1_hand

    def decision(self):
        _, p1_cards = self.read()
        p1_hand = sum(p1_cards)
        
        if p1_hand == range(17, 22):
            print('Player 1 stands.')

        try:
            while p1_hand < 17:
                p1_hand = self.hit()
                if p1_hand > 21:
                    print('Player 1 busts!')
                    break
                elif p1_hand >= 17:
                    print("Player 1 stands!")
                    self.stand()
                    break
        except Exception as e:
            print(f"An error occured: {e}")
