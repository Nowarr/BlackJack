from src.colors import YELLOW, BLUE, RESET

'''
This is our bettor. Rule sets are lightly developed based on general good practice when playing a dealer in Blackjack. 

'''
class Bettor:
    def __init__(self, manager, dummy):
        self.manager = manager
        self.dummy = dummy
        self.hand = []
        self.is_soft = False 

    # fresh hand 
    def reset_hand(self):
        self.hand = []
        self.is_soft = False 

    # receives his initial cards
    def receive_card(self, card):
        self.hand.append(card)
    
    # he reads his initial cards before making a decision
    def calculate_hand_value(self):
        value = [item for card in self.hand for item in card if isinstance(item, int)]
        return sum(value)

    def hit(self):
        new_card = self.manager.dealer.deal()
        self.receive_card(new_card)

        value = self.calculate_hand_value()
        if value > 21 and self.is_soft:
            value -= 10
            self.is_soft = False

        return value

    def decision(self):
        dealer_revealed_card_value = self.dummy.hand[0][1]  # Extract the value from the dummy's revealed card

        current_value = self.calculate_hand_value()

        # RULE # 0: If Bettor has a hand of 21, always stand
        if current_value == 21:
            print(f"{YELLOW}Bettor stands with a hand of 21.{RESET}")
            return

        # RULE # 1: If Bettor's hand value is 11 or lower, keep hitting until a better hand or bust
        while current_value <= 11:
            current_value = self.hit()
            print(f"{YELLOW}Bettor hits. New hand value: {current_value}{RESET}")
            if current_value > 21:
                return

        # RULE # 2: Between 12 and 16
        while 12 <= current_value <= 16:
            if dealer_revealed_card_value >= 7:
                current_value = self.hit()
                print(f"{YELLOW}Bettor hits based on strong dealer card. New hand value: {current_value}{RESET}")
            else:
                print(f"{YELLOW}Bettor stands on the basis that the dealer is likely to bust.{RESET}")
                return
            if current_value > 21:
                return

        # RULE # 3: 17 or higher
        while current_value >= 17:
            if not self.is_soft:
                print(f"{YELLOW}Bettor stands on a hard {current_value}.{RESET}")
                return
            else:
                if dealer_revealed_card_value >= 7:
                    current_value = self.hit()
                    print(f"{YELLOW}Bettor hits on a soft 17. New hand value: {current_value}{RESET}")
                else:
                    print(f"{YELLOW}Bettor stands on a soft {current_value}.{RESET}")
                    return
            if current_value > 21:
                return

        # RULE # 4: Dealer has 10 or Ace
        while dealer_revealed_card_value in (10, 11):
            if current_value <= 17:
                current_value = self.hit()
                print(f"{YELLOW}Bettor hits based on strong dealer hand. New hand value: {current_value}{RESET}")
                if current_value > 21:
                    return
            else:
                print(f"{YELLOW}Bettor stands on {current_value}.{RESET}")
                return
