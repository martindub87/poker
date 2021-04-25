from .dealer import Dealer

class Player(object):

    def __init__(self, name, buy_in, card_1 = None, card_2 = None, award = None, is_sb = False, is_bb = False, is_button = False):
        
        self.name = name
        self.stack = int(buy_in)
        self.hand = list()

    def bet(self, bet_amount):

        assert bet_amount <= self.stack, "Bet amount can not be greater than {}.".format(self.stack)
        self.stack += -bet_amount 
    
    def check(self):
        pass

    def call(self, call_amount):
        assert call_amount <= self.stack, "Call amount can not be greater than {}.".format(self.stack)
        self.stack += -call_amount
    
    def action(self):
        assert self.hand != (None, None), "Player posses no cards."

    def _receive_a_card(self, card_instance):
        self.hand.append(card_instance)