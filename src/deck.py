import random

import pygame

from .hand import Hand
from .card import Card, Rank, Suit


class Deck(Hand, pygame.sprite.Sprite):
    def __init__(self):
        super(Deck, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"sprites/cardback.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (840, 270)

    def populate(self):
        self.clear()
        for s in range(Suit.CLUBS, Suit.SPADES + 1):
            for r in range(Rank.ACE, Rank.KING + 1):
                self.add(Card(r, s))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hand):
        if self.cards:
            hand.add(self.cards.pop())
        else:
            print('Out of cards. Unable to deal.')

    def additional_cards(self, generic_player):
        while not generic_player.is_busted() and generic_player.is_hitting():
            self.deal(generic_player)

    def check_cards_count(self):
        if len(self.cards) < 10:
            self.populate()
            self.shuffle()
