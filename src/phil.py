"""
PHIL
TODO:
    - Must read revealed cards in main game loop.
    - Must make decisions based on initial hand and the sole revealed card of Mark.
"""

import random
from src.colors import BLUE, YELLOW, RESET

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

        # RULE # 0: If Phil has a hand of 21, always stand
        if phil_hand == 21:
            self.stand()
            print(f"{YELLOW}Phil stands with a hand of 21.{RESET}")
            return

        # If Phil's hand value is 11 or lower, he should keep hitting until he gets a better hand or busts
        while phil_hand <= 11:
            phil_hand = self.hit()
            if phil_hand > 21:
                print(f"{BLUE} Phil busts!{RESET}")
                return
        
        # Loss set
        if phil_hand > 21:
            print(f"{BLUE} Phil busts!{RESET}")
            return
        
        # RULE # 1: Between 12 and 16
        if 12 <= phil_hand <= 16:
            if _ >= 7:
                phil_hand = self.hit()
                print(f"{YELLOW}Phil hits on the basis that the dealer has a strong potential hand so Phil needs to improve his hand.{RESET}")
            elif _ <= 6:
                self.stand()
                print(f"{YELLOW}Phil stands on the basis that the dealer is likely to bust.{RESET}")
            if phil_hand > 21:
                print(f"{BLUE}Phil busts!{RESET}")
            return
        
        # RULE # 2: 17 or higher
        if phil_hand >= 17:
            if not self.is_soft:
                self.stand()
                print(f"{YELLOW}Phil stands on the basis that there is little risk to win on a hard 17 or above.{RESET}")
            elif self.is_soft:
                if _ >= 7:
                    phil_hand = self.hit()
                    print(f"{YELLOW}Phil hits on the basis that a soft 17 is weaker than a strong dealer card.{RESET}")
                elif _ <= 6:
                    self.stand()
                    print(f"{YELLOW}Phil stands on the basis that the dealer is likely to bust.{RESET}")
                if phil_hand > 21:
                    print(f"{BLUE}Phil busts!{RESET}")
            return
        
        # RULE # 3: Dealer has 10 or Ace
        if _ in (10, 11):
            if phil_hand <= 17:
                phil_hand = self.hit()
                print(f"{YELLOW}Phil hits on the basis that the dealer has a strong chance of having a good hand and must retaliate.{RESET}")
                if phil_hand > 21:
                    print("Bust!")
            elif phil_hand >= 18:
                self.stand()
                print(f"{YELLOW}Phil stands on the basis that he has a good chance of winning or pushing without risking a bust.{RESET}")
            return
