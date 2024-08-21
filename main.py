import random
from src.game_logic import Dealer, Dummy
from src.bettor import Bettor
from src.manager import Manager

class Round:
    def __init__(self):
        self.dealer = Dealer() 
        self.dummy = Dummy() # This is the dummy player ("dealer")
        self.bettor = Bettor(self.dealer,None)  # This is our main player
        self.manager = Manager(self.dealer,self.dummy,self.bettor)
        self.bettor.manager = self.manager # This tells bettor who its manager is (needed due to circular dependence)

    def start_round(self):
        # Reset players' hands for each round
        self.dummy.hand = []
        self.bettor.hand = []

        # Initial hand to bettor and dummy
        for _ in range(2):
          
            card_p1 = self.dealer.deal()
            card_p2 = self.dealer.deal()

            self.dummy.receive_card(card_p1)
            self.bettor.receive_card(card_p2)    
       
        print("Bettor:",self.bettor.show_count())
        self.bettor.bet() # bettor makes his bets
        self.manager.check() # manager continues the game with dummy

if __name__ == "__main__":
    game = Round()
    game.start_round()
