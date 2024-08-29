from src.manager import GameManager
from src.bettor import Bettor
from src.dummy import Dummy

# ANSI escape sequences for colors
RESET = "\033[0m"
BLUE = "\033[34m"
RED = "\033[31m"


'''
General Structure:

    - GameManager handles the game's state. Handles status of game, hand values, game results, etc. Cards are revealed upon the start of the round
    - Bettor is our "main player" and makes decisions based on both his current hand value as well as a set of rules hard coded into his class
    - Dummy simply provides a final response once the bettor makes his decisions.
    - The game then finishes and asks the user to run a new round or not.

'''
class Round:
    def __init__(self):
        self.manager = GameManager()
        self.dummy = Dummy(self.manager)
        self.bettor = Bettor(self.manager, self.dummy)
        self.is_running = True

    def start_round(self):
        # fresh hands at start of round
        self.bettor.reset_hand()
        self.dummy.reset_hand()
        
        # initial cards are dealt
        for _ in range(2):
            self.bettor.receive_card(self.manager.dealer.deal())
            self.dummy.receive_card(self.manager.dealer.deal())

    # this reveals the initial cards, for dummy, only one of his cards are shown to the bettor
    def reveal(self):
        bettor_cards = ', '.join(f"{card[0]} of {card[2]}" for card in self.bettor.hand)
        bettor_value = self.bettor.calculate_hand_value()
        print('------------------------------------------------')
        print(f"{BLUE}Bettor's cards{RESET}: {bettor_cards} | {bettor_value}")

        dummy_first_card = self.dummy.hand[0]
        dummy_initial_hand = f"{dummy_first_card[0]} of {dummy_first_card[2]}" # only shows first card 
        print(f"{RED}Dummy's revealed card{RESET}: {dummy_initial_hand} | {dummy_first_card[1]}")
        print('------------------------------------------------')

    def game_loop(self):
        while self.is_running:
            print("\n\n")
            self.reveal()
            self.bettor.decision()
            self.dummy.response()

            if self.manager.check_game_over(self.bettor, self.dummy):
                print("Game Over")
                self.is_running = False
                break
if __name__ == "__main__":
    while True:
        for _ in range (3):
            round = Round()
            round.start_round()
            round.game_loop()

        inp = input("\n\nSimulation over. Run again? (y/n)")
        print(inp)
        if inp != 'y':
            break

