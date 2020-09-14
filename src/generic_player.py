import pygame

from .hand import Hand


class GenericPlayer(Hand):
    def __init__(self, name, pos=(0, 0)):
        super(GenericPlayer, self).__init__()
        self.name = name
        self.pos = pos
        self.surface = pygame.Surface((1024, 190))

    def is_hitting(self):
        pass

    def is_busted(self):
        return self.total() > 21

    def draw_hand(self, screen):
        self.surface.fill((250, 250, 250))
        font = pygame.font.Font(None, 36)
        deck_size_text = font.render(str(self.total()), 1, (10, 10, 10))
        if len(self.cards) > 0:
            self.surface.blit(deck_size_text, deck_size_text.get_rect(
                centerx=336, centery=95))

        for index, card in enumerate(self.cards):
            self.surface.blit(
                card.image, (372 + index * (card.rect.width // 2), 0))

        screen.blit(self.surface, self.pos)
