import random

class Dealer:
    def __init__(self):
        self.deck = {
            "ace": (1, 11), "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "jack": 10, "queen": 10, "king": 10
        }
        self.suits = ["hearts", "clubs", "spades", "diamonds"]
        self.dealt_cards = {}  # Track how many times each card has been dealt

    def deal(self):
        while True:
            card, value = random.choice(list(self.deck.items()))  
            suit = random.choice(self.suits)  
            dealt_card = (card, value, suit)
            deck_amount = 4
            if self.dealt_cards.get(dealt_card, 0) < deck_amount:  
                self.dealt_cards[dealt_card] = self.dealt_cards.get(dealt_card, 0) + 1  # Increment the dealt count
                return dealt_card

            if sum(self.dealt_cards.values()) == len(self.deck) * 4:
                raise ValueError("No more cards to deal. The deck is empty.")

class Player:
    def __init__(self):
        self.hand = []  # player's hand to store dealt cards

    def receive_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return self.hand



 
