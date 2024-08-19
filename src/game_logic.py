import random
import numpy 

class Game:
    def __init__(self):
        self.deck = {
            "ace": (1, 11), "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "jack": 10, "queen": 10, "king": 10
        }
        self.suits = ["hearts", "clubs", "spades", "diamonds"]

    def deal(self):
        card, value = random.choice(list(self.deck.items()))  # random card and its value from deck
        suit = random.choice(self.suits)  # random suit
        return card, value, suit


if __name__ == "__main__":
    game = Game()
    print(game.deal())
