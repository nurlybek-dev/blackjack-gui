import pygame


class Rank:
    ACE = 1
    TOW = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 12
    QUEEN = 12
    KING = 13


class Suit:
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3


class Card(pygame.sprite.Sprite):
    RANKS = ['0', 'A', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's']

    def __init__(self, rank=Rank.ACE, suit=Suit.CLUBS, is_face_up=True):
        pygame.sprite.Sprite.__init__(self)
        self.rank = rank
        self.suit = suit
        self.is_face_up = is_face_up
        sprite = f"{self.SUITS[self.suit]}{self.RANKS[self.rank]}"
        self.image = pygame.image.load(f"sprites/{sprite}.png")
        self.rect = self.image.get_rect()

    def value(self):
        value = 0
        if self.is_face_up:
            value = self.rank
            if value > 10:
                value = 10

        return value

    def flip(self):
        self.is_face_up = not self.is_face_up

    def __str__(self):
        if self.is_face_up:
            return self.RANKS[self.rank] + self.SUITS[self.suit]
        else:
            return 'XX'

    def __repr__(self):
        return self.RANKS[self.rank] + self.SUITS[self.suit]
