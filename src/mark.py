
"""
TODO:
    - Need to compare mark's hand to phil's in cases where they push or marks hand becomes greater than phil's final hand 
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
                    print('Player 2 busts!')
                    break
                if mark_hand == 21:
                    print('Player 2 wins!')
        except Exception as e:
            print(f"An error has occured: {e}")
                        
    

