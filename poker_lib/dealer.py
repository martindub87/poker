from .cards import Card, StandardDeck
from .player import Player

class Dealer(object):

    def __init__(self):
        self.deck = StandardDeck(showing = True)

    def showdown_eval(self, player_hands_dict, table):
        pass

    def deal_a_card(self, player_instance):
        dealt_card = self.deck.deal_a_card()
        player_instance._receive_a_card(dealt_card)