import random 

class Bettor:
    def __init__(self,dealer,manager):
        self.hand = []  # player's hand to store dealt cards
        self.dealer = dealer
        self.manager = manager

    def receive_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return self.hand
    
    def show_count(self):
        count = 0
        for i in range(len(self.hand)):
            count += self.show_hand()[i][1]
        return count

    # betting starts:
    
    def bet(self):
        
        while self.show_count() < 21:
            choice = random.choice(('hit','hold'))
            if choice == 'hit':
                print("Hit")
                self.receive_card(self.dealer.deal())
                print("Bettor: ",self.show_count())

            else:
                print("Hold")
                print("Bettor: ",self.show_count())
                break 

        print("\n")
