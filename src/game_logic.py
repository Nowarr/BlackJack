import numpy as np 
import random


def deal():
    deck = {"ace":(1,11),"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,
            "eight":8,"nine":9,"ten":10,"jack":10,"queen":10,"king":10}
    suits = ["hearts","clubs","spades","diamonds"]

    card,value = random.choice(list(deck.items())) # random card and its value from deck 
    suit = random.choice(suits) # random suit

    
    return(card,value,suit)



print(deal())
