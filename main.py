from src.game_logic import Dealer
from src.game_logic import Player
from src.phil import Phil
from src.mark import Mark

# ANSI escape sequences for colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"


class Round:
    def __init__(self):
        self.dealer = Dealer()
        self.phil = Player()  # This is Phil
        self.mark = Player()  # This is Mark
        self.start_round()

    def start_round(self):
        # Reset players' hands for each round
        self.phil.hand = []
        self.mark.hand = []

        # Initial hand to Phil and Mark
        for _ in range(2):
            card_phil = self.dealer.deal()
            card_mark = self.dealer.deal()

            self.phil.receive_card(card_phil)
            self.mark.receive_card(card_mark)

    def reveal(self):
        # Phil's cards
        value = [item for card in self.phil.hand for item in card if isinstance(item, int)]
        phil_cards = ', '.join(f"{card[0]} of {card[2]}" for card in self.phil.hand)
        print('------------------------------------------------')
        print(f"{BLUE}Phil's cards{RESET}: {phil_cards} | {sum(value)}")

        # Mark's initially revealed card
        value_mark = [item for card in self.mark.hand for item in card if isinstance(item, int)]
        mark_first_card = self.mark.hand[0]
        mark_initial_hand = f"{mark_first_card[0]} of {mark_first_card[2]}"
        print(f"{RED}Mark's revealed card{RESET}: {mark_initial_hand} | {value_mark[0]}")
        print('------------------------------------------------')
    
    def philsDecision(self):
        def read():
            # Mark's initially revealed card is read by Phil
            mark_revealed_card = self.mark.hand[0][1]
            # Phil also reads his current hand before making a decision
            phil_hand = [item for card in self.phil.hand for item in card if isinstance(item, int)]
            return mark_revealed_card, phil_hand

        def hit():
            # Deal a new card to Phil
            new_card = self.dealer.deal()
            self.phil.receive_card(new_card)
            
            # Format the new hand
            new_hand = ', '.join(f"{card[0]} of {card[2]}" for card in self.phil.hand)
            # Extract int values and calculate the total
            value = [item for card in self.phil.hand for item in card if isinstance(item, int)]
            total_value = sum(value)

            # Print the new hand
            print(f"{BLUE}Phil{RESET} chose to hit. New hand: {new_hand} | {total_value}")
            
            return total_value

        def stand():
            pass

        phil = Phil(read, hit, stand)
        phil.decision()

    def markResponse(self):
        def read():
            phil_final_hand = [item for card in self.phil.hand for item in card if isinstance(item, int)]
            return phil_final_hand

        def response():
            new_card = self.dealer.deal()
            self.mark.receive_card(new_card)
                
            # Format new hand and extract int value
            new_hand = ', '.join(f"{card[0]} of {card[2]}" for card in self.mark.hand)
            value = [item for card in self.mark.hand for item in card if isinstance(item, int)]
            total_value = sum(value)

            # Print new hand
            print(f"{RED}Mark's hand{RESET}: {new_hand} | {total_value}")
            
            return total_value

        mark = Mark(read, response)
        mark.response()


    def check_game_over(self):
        pass

    def game_loop(self):
        while True:
            # start game
            self.reveal()
 
            # Phil's turn
            self.philsDecision()

            # Mark's turn
            self.markResponse()

            # Game over conditions
            if self.check_game_over():
                print("Game Over")
                break

if __name__ == "__main__":
    round = Round()
    round.start_round()
    round.reveal()
    round.philsDecision()
    round.markResponse()
=======
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
