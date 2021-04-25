from .player import Player
from .dealer import Dealer

class PokerGame(object):

    def __init__(self, players):
        self.players = [
            Player("Mato", 1000), 
            Player("Pato", 1000)
            ] 
        self.dealer = Dealer()
        self.table = Table(len(self.players))

    def _count_active_players(self):
        self.active_players = 0
        for p in self.players:
            if p.stack > 0:
                self.active_players += 1 

    def play_round(self):
        pass

    def simulate(self):
        self._count_active_players()
        if self.active_players > 1:
            self.play_round()
        else:
            print("{} won".format(self.active_players))

class Table(object):

    def __init__(self, n_of_players):
        self.n_of_players = n_of_players
        self.pot = 0

    def assign_bb_pos(self):
        pass

    def assign_sb_pos(self):
        pass

    def assign_button_pos(self):
        pass