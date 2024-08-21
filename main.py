from src.game_logic import Dealer
from src.game_logic import Player
from src.phil import Phil
from src.mark import Mark

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
        print(f"Phil's cards: {phil_cards} | {sum(value)}")

        # Mark's initially revealed card
        value_mark = [item for card in self.mark.hand for item in card if isinstance(item, int)]
        mark_first_card = self.mark.hand[0]
        mark_initial_hand = f"{mark_first_card[0]} of {mark_first_card[2]}"
        print(f"Mark's revealed card: {mark_initial_hand} | {value_mark[0]}")
    
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
            print(f"Phil chose to hit. New hand: {new_hand} | {total_value}")
            
            return total_value

        def stand():
            print("Phil stands.")

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
            print(f"Mark's hand: {new_hand} | {total_value}")
            
            return total_value

        mark = Mark(read, response)
        mark.response()

if __name__ == "__main__":
    game = Round()
    game.start_round()
    game.reveal()
    game.philsDecision()
    game.markResponse()
