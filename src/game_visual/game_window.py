from src.colors import YELLOW, BLUE, RESET

class Bettor:
    def __init__(self, manager):
        self.manager = manager
        self.hand = []
        self.is_soft = False

    def reset_hand(self):
        self.hand = []
        self.is_soft = False

    def receive_card(self, card):
        self.hand.append(card)

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
        dealer_revealed_card = self.manager.dealer.deal()[1]  # Extract the value from the dealer's revealed card

        current_value = self.calculate_hand_value()

        # RULE # 0: If Phil has a hand of 21, always stand
        if current_value == 21:
            print(f"{YELLOW}Bettor stands with a hand of 21.{RESET}")
            return

        # If Phil's hand value is 11 or lower, he should keep hitting until he gets a better hand or busts
        while current_value <= 11:
            current_value = self.hit()
            print(f"{YELLOW}Bettor hits. New hand value: {current_value}{RESET}")
            if current_value > 21:
                print(f"{BLUE}Bettor busts!{RESET}")
                return

        # RULE # 1: Between 12 and 16
        if 12 <= current_value <= 16:
            if dealer_revealed_card >= 7:
                current_value = self.hit()
                print(f"{YELLOW}Bettor hits based on strong dealer card.{RESET}")
            else:
                print(f"{YELLOW}Bettor stands.{RESET}")
            if current_value > 21:
                print(f"{BLUE}Bettor busts!{RESET}")
            return

        # RULE # 2: 17 or higher
        if current_value >= 17:
            if not self.is_soft:
                print(f"{YELLOW}Bettor stands on a hard 17 or above.{RESET}")
            else:
                if dealer_revealed_card >= 7:
                    current_value = self.hit()
                    print(f"{YELLOW}Bettor hits on a soft 17.{RESET}")
                else:
                    print(f"{YELLOW}Bettor stands.{RESET}")
            if current_value > 21:
                print(f"{BLUE}Bettor busts!{RESET}")
            return

        # RULE # 3: Dealer has 10 or Ace
        if dealer_revealed_card in (10, 11):
            if current_value <= 17:
                current_value = self.hit()
                print(f"{YELLOW}Bettor hits based on strong dealer hand.{RESET}")
                if current_value > 21:
                    print(f"{BLUE}Bettor busts!{RESET}")
            else:
                print(f"{YELLOW}Bettor stands.{RESET}")
            return
