
"""
TODO:
    - Provides response to phil once a decision on his end has been made and his turn is over
    - Continues to hit until bust, win, or push
    - 
"""

class Mark:
    def __init__(self, read, hit):
        self.read = read
        self.hit = hit

    def response(self):
        phils_final_hand = self.read()

        phils_card_value = sum(phils_final_hand)

        if phils_card_value < 21:
            self.hit()
        else:
            print('crikey')


