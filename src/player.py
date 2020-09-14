from .generic_player import GenericPlayer


class Player(GenericPlayer):
    def __init__(self, pos):
        super(Player, self).__init__('Player', pos)
