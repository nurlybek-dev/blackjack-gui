from .generic_player import GenericPlayer


class House(GenericPlayer):
    def __init__(self, name):
        super(House, self).__init__(name)

    def is_hitting(self):
        return self.total() <= 16

    def flip_first_card(self):
        if self.cards:
            self.cards[0].flip()
        else:
            print('No card to flip!')
