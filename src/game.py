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
        self.house = House((0, 100))
        self.player = Player((0, 420))
        self.chip_image = pygame.image.load(f"sprites/chipBlueWhite.png")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.winner_font = pygame.font.Font(None, 72)

        self.winner = ''
        self.turn = 'player'
        self.playing = False
        self.run = True

        self.deal_button = Button(
            (172, 700, 100, 50), RED, self.deal, text="Deal", **BUTTON_STYLE)
        self.stand_button = Button(
            (372, 700, 100, 50), RED, self.stand, text="Stand", **BUTTON_STYLE)
        self.hit_button = Button(
            (502, 700, 100, 50), RED, self.hit, text="Hit", **BUTTON_STYLE)

        self.chip_20_button = Button(
            (32, 560, 100, 50), RED, lambda: self.bet(20), text="20", **BUTTON_STYLE)
        self.chip_100_button = Button(
            (32, 630, 100, 50), RED, lambda: self.bet(100), text="100", **BUTTON_STYLE)
        self.chip_500_button = Button(
            (32, 700, 100, 50), RED, lambda: self.bet(500), text="500", **BUTTON_STYLE)

    def main_loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                self.check_buttons_event(event)

            self.deck.check_cards_count()

            self.computer_move()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def computer_move(self):
        if self.turn == 'computer' and self.playing:
            if self.house.is_busted() or self.house.total() > self.player.total():
                self.game_over()
            else:
                self.deck.deal(self.house)

    def draw(self):
        self.screen.fill((250, 250, 250))

        self.house.draw_hand(self.screen)
        self.player.draw_hand(self.screen)

        self.screen.blit(self.deck.image, (70, 200))

        self.screen.blit(self.chip_image, (32, 470))
        player_cash_text = self.font.render(
            str(self.player.account.get_cash()), 1, (10, 10, 10))
        self.screen.blit(player_cash_text, player_cash_text.get_rect(
            centerx=130, centery=505))

        player_bet_text = self.font.render(
            "Bet: " + str(self.player.bet), 1, (10, 10, 10))
        self.screen.blit(player_bet_text, player_bet_text.get_rect(
            centerx=222, centery=655))

        deck_size_text = self.font.render(
            str(len(self.deck.cards)), 1, (10, 10, 10))
        self.screen.blit(deck_size_text, deck_size_text.get_rect(
            centerx=140, centery=408))

        if self.winner:
            winner_text = self.winner_font.render(self.winner, 1, ORANGE)
            self.screen.blit(winner_text, winner_text.get_rect(
                centerx=512, centery=360))

        self.update_buttons()

    def deal(self):
        if not self.playing:
            if self.player.make_bet():
                self.player.clear()
                self.house.clear()
                self.deck.deal(self.player)
                self.deck.deal(self.player)
                self.deck.deal(self.house)
                self.turn = 'player'
                self.playing = True
                self.winner = ''
            else:
                print('Not enough money!')

    def stand(self):
        if self.playing and self.turn == 'player':
            self.turn = 'computer'

    def hit(self):
        if self.playing and self.turn == 'player':
            self.deck.deal(self.player)
            if self.player.is_busted():
                self.game_over()

    def bet(self, value):
        self.player.set_bet(value)

    def check_buttons_event(self, event):
        self.deal_button.check_event(event)
        self.stand_button.check_event(event)
        self.hit_button.check_event(event)
        self.chip_20_button.check_event(event)
        self.chip_100_button.check_event(event)
        self.chip_500_button.check_event(event)

    def update_buttons(self):
        self.deal_button.update(self.screen)
        self.stand_button.update(self.screen)
        self.hit_button.update(self.screen)
        self.chip_20_button.update(self.screen)
        self.chip_100_button.update(self.screen)
        self.chip_500_button.update(self.screen)

    def game_over(self):
        self.playing = False
        if self.player.is_busted():
            self.winner = 'You Lose!'
        elif self.house.is_busted():
            self.winner = 'You Win!'
            self.player.win_bet()
        elif self.player.total() > self.house.total():
            self.winner = 'You win!'
            self.player.win_bet()
        elif self.house.total() > self.player.total():
            self.winner = 'You Lose!'
        else:
            self.winner = 'Push'
