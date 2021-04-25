import numpy as np
import random

class Card (object):

    def __init__(self, name, value, suit, showing = True):
        self.name = name
        self.value = value
        self.suit = suit
        self.showing = showing

    def __repr__(self):
        if self.showing:
            return "{} of {}".format(str(self.name), self.suit)
        else:
            return "Card"

class StandardDeck (object):
    
    def __init__(self, showing):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        values = {
            "Two":2,
            "Three":3,
            "Four":4,
            "Five":5,
            "Six":6,
            "Seven":7,
            "Eight":8,
            "Nine":9,
            "Ten":10,
            "Jack":11,
            "Queen":12,
            "King":13,
            "Ace":14 
            }
        self.deck = list()
        
        for name, value in values.items():
            for suit in suits:
                self.deck.append(Card(name, value, suit, showing))
        self.shuffle()

    def __repr__(self):
        return "Standard deck of cards:{0} remaining".format(len(self.shuffled_deck))

    def shuffle(self, times = 1):
        self.shuffled_deck = self.deck
        random.shuffle(self.shuffled_deck)

    def deal_a_card(self):
        return self.shuffled_deck.pop(0)

class PlayerHandEval(object):

    def __init__(self, table, player):

        self.table = table
        self.player = player

    def __repr__(self):
        return 

deck = StandardDeck(showing = True)

print("------\\\\------")
print(deck)
print("------\\\\------")
print(deck.deal_a_card())
print("------\\\\------")
print(deck)
print("------\\\\------")
print(deck.deal_a_card())
print("------\\\\------")
print(deck)