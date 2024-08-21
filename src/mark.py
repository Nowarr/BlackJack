"""
TODO:
    - Need to compare Mark's hand to Phil's in cases where they push or Mark's hand becomes greater than Phil's final hand.
"""
from src.colors import CYAN, GREEN, RESET
class Mark:
    def __init__(self, read, hit):
        self.read = read
        self.hit = hit

    def response(self):
        mark_cards = self.read()
        mark_hand = sum(mark_cards)
        
        try:
            while mark_hand < 21:
                mark_hand = self.hit()
                if mark_hand > 21:
                    print(f'{CYAN}Mark busts!{RESET}')
                    break
                if mark_hand == 21:
                    print(f'{GREEN}Mark wins!{RESET}')
        except Exception as e:
            print(f"An error has occurred: {e}")
