from src.colors import RED, RESET

'''
Dummy's sole purpose is to receive his cards and provide a response to bettor's final hand'
'''
class Dummy:
    def __init__(self, manager):
        self.manager = manager
        self.hand = []

    def reset_hand(self):
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        value = [item for card in self.hand for item in card if isinstance(item, int)]
        return sum(value)

    def response(self):
        while self.calculate_hand_value() < 21:
            new_card = self.manager.dealer.deal()
            self.receive_card(new_card)
            new_value = self.calculate_hand_value()
            print(f"{RED}Dummy hits. New hand value: {new_value}{RESET}")

        if self.calculate_hand_value() > 21:
            print(f"{RED}Dummy busts.{RESET}")
        else:
            print(f"{RED}Dummy wins with {self.calculate_hand_value()}.{RESET}")
