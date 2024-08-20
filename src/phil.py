


"""
PHIL
TODO:
    - Must read revealed cards in main game loop
    - Must make decisions based on initial hand and sole
    revealed card of player 2
"""

class Phil:
    def __init__(self, read, hit, stand):
        self.read = read
        self.hit = hit
        self.stand = stand 

    def decision(self):
        revealed_cards = self.read()

        revealed_card_value = revealed_cards[0][1]

        if revealed_card_value < 7:
            self.hit()
        else:
            self.stand()

