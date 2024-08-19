import random

"""
This class defines the deck, suits, and deals the cards. The primary function
is to deal a card and keep track of what is dealt in the context of the instance called
at whatever point in the program.
"""
"""
TODO: 
    - Define a way to return the cards that are dealt
    - Keep track of cards, making sure they aren't reused
"""
class Dealer:
    def __init__(self):
        self.deck = {
            "ace": (1, 11), "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "jack": 10, "queen": 10, "king": 10
        }
        self.suits = ["hearts", "clubs", "spades", "diamonds"]
        self.dealt_cards = []  # this tracks the dealt cards

    def deal(self):
        card, value = random.choice(list(self.deck.items()))  # random card and its value from deck
        suit = random.choice(self.suits)  # random suit
        dealt_card = (card, value, suit)
        self.dealt_cards.append(dealt_card)
        return dealt_card

"""
This class represents a player, keeps track of the cards dealt to them,
and calculates the total value of their hand.
"""
"""
TODO:
    - Must find a way to receive the cards dealt and then store them properly
    - Thinko g 
"""
class Player:
    def __init__(self):
        self.hand = []  # player's hand to store dealt cards

    def receive_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return self.hand


