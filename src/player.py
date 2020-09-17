from .generic_player import GenericPlayer
from .account import Account


class Player(GenericPlayer):
    def __init__(self, pos):
        super(Player, self).__init__('Player', pos)
        self.account = Account()
        self.bet = 20

    def set_bet(self, value):
        self.bet = value

    def make_bet(self):
        if self.account.get_cash() >= self.bet:
            self.account.draw(self.bet)
            return True
        return False
    
    def win_bet(self):
        self.account.add(self.bet * 2)
    