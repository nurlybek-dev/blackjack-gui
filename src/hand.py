from .card import Rank


class Hand:
    def __init__(self):
        self.cards = list()

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards.clear()

    def total(self):
        total = 0
        contains_ace = False
        for card in self.cards:
            total += card.value()
            if card.rank == Rank.ACE:
                contains_ace = True

        if contains_ace and total <= 11:
            total += 10

        return total
