import pygame

from .deck import Deck
from .house import House
from .player import Player
from .button import Button

pygame.init()

WIDTH = 1024
HEIGHT = 768

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)

BUTTON_STYLE = {
    "hover_color": BLUE,
    "clicked_color": GREEN,
    "clicked_font_color": BLACK,
    "hover_font_color": ORANGE,
}


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Blackjack')

        self.deck = Deck()
        self.house = House((0, 38))
        self.player = Player((0, 400))

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        self.turn = 'player'
        self.playing = False
        self.game_over = False
        self.run = True

        self.deal_button = Button(
            (172, 700, 100, 50), RED, self.deal, text="Deal", **BUTTON_STYLE)

        self.stand_button = Button(
            (372, 700, 100, 50), RED, self.stand, text="Stand", **BUTTON_STYLE)
        self.hit_button = Button(
            (502, 700, 100, 50), RED, self.hit, text="Hit", **BUTTON_STYLE)

    def main_loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                self.deal_button.check_event(event)
                self.stand_button.check_event(event)
                self.hit_button.check_event(event)

            self.deck.check_cards_count()

            if self.turn == 'computer' and self.playing:
                if self.house.is_busted() or self.house.total() > self.player.total():
                    self.playing = False
                    self.game_over = True
                else:
                    self.deck.deal(self.house)

            self.screen.fill((250, 250, 250))
            self.screen.blit(self.deck.image, (70, 200))

            self.house.draw_hand(self.screen)
            self.player.draw_hand(self.screen)

            self.deal_button.update(self.screen)
            self.stand_button.update(self.screen)
            self.hit_button.update(self.screen)

            deck_size_text = self.font.render(
                str(len(self.deck.cards)), 1, (10, 10, 10))
            self.screen.blit(deck_size_text, deck_size_text.get_rect(
                centerx=140, centery=408))

            if not self.playing and self.game_over:
                if self.player.is_busted():
                    winner = 'You Lose!'
                elif self.house.is_busted():
                    winner = 'You Win!'
                elif self.player.total() > self.house.total():
                    winner = 'You win!'
                elif self.house.total() > self.player.total():
                    winner = 'You Lose!'
                else:
                    winner = 'Push'
                winner_text = self.font.render(winner, 1, (10, 10, 10))
                self.screen.blit(winner_text, winner_text.get_rect(
                    centerx=512, centery=300))

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def deal(self):
        if not self.playing:
            self.player.clear()
            self.house.clear()
            self.deck.deal(self.player)
            self.deck.deal(self.player)
            self.deck.deal(self.house)
            self.turn = 'player'
            self.playing = True
            self.game_over = False

    def stand(self):
        if self.playing and self.turn == 'player':
            self.turn = 'computer'

    def hit(self):
        if self.playing and self.turn == 'player':
            self.deck.deal(self.player)
            if self.player.is_busted():
                self.playing = False
                self.game_over = True
