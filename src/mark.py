"""
TODO:
    - Need to compare Mark's hand to Phil's in cases where they push or Mark's hand becomes greater than Phil's final hand.
"""

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
                    print('Mark busts!')
                    break
                if mark_hand == 21:
                    print('Mark wins!')
        except Exception as e:
            print(f"An error has occurred: {e}")
