"""
PHIL
TODO:
    - Must read revealed cards in main game loop.
    - Must make decisions based on initial hand and the sole revealed card of Mark.
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
        _, phil_cards = self.read()
        phil_hand = sum(phil_cards)

        # Phil's strategy: hit if the hand is low, considering soft hands.
        if card_value == 11:
            if phil_hand + card_value > 21:
                card_value = 1
            else:
                self.is_soft = True

        phil_hand += card_value
        print(f"Phil draws a card worth {card_value}. New hand value is {phil_hand}.")

        if phil_hand > 21 and self.is_soft:
            phil_hand -= 10
            self.is_soft = False
            print(f"Phil converts an Ace to 1. New hand value is {phil_hand}.")
        
        return phil_hand

    def decision(self):
        _, phil_cards = self.read()
        phil_hand = sum(phil_cards)
        
        try:
            while phil_hand < 17:
                phil_hand = self.hit()
                if phil_hand > 21:
                    print('Phil busts!')
                    break
                elif phil_hand >= 17:
                    print("Phil stands!")
                    self.stand()
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
