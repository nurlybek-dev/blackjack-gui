class Account(object):
    def __init__(self):
        self.bet = 0
        self.cash = 1000

    def get_cash(self):
        return self.cash

    def draw(self, value):
        if self.cash >= value:
            self.cash -= value

    def add(self, value):
        self.cash += value
