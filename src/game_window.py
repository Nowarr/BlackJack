import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import Round 
from button import Button
from game_logic import Dealer

class Game:
    def __init__(self):
        # Initialize Pygame and set up the game window
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("BlackJack")

        # Colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # Load the EB Garamond font (Ensure the path is correct)
        font_path = '../resources/EBG-Reg.ttf'
        font_size = 30
        self.font = pygame.font.Font(font_path, font_size)

        # Create buttons
        self.hit_button = Button(self.screen, "HIT", 20, self.screen_height - 60, 140, 40, self.font, self.black, self.white)
        self.stand_button = Button(self.screen, "STAND", 180, self.screen_height - 60, 140, 40, self.font, self.black, self.white)
        
        # Initialize Dealer
        self.dealer = Dealer()

        # Initialize game loop
        self.round = Round()


    def handle_stand(self):
        print('STAND CLICKED')

    def handle_hit(self):
        print('HIT CLICKED')
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.hit_button.is_clicked(event):
                        self.handle_hit()
                    elif self.stand_button.is_clicked(event):
                        self.handle_stand()

            self.update_screen()

        pygame.quit()
        sys.exit()

    def update_screen(self):
        self.screen.fill(self.black)
        pygame.draw.line(self.screen, self.white, (0, self.screen_height // 2), (self.screen_width, self.screen_height // 2), 2)
        self.hit_button.draw()
        self.stand_button.draw()
        self.initial_hand()
        pygame.display.flip()

    def initial_hand(self):
        # only show mark's initial hand on his screen
        for index, card in enumerate(self.round.mark.hand[:1]):  # Only reveal the first card of Mark
            x = 550 + index * 550 
            y = 100
            pygame.draw.rect(self.screen, self.white, (x, y, 100, 150)) # this is the size
            card_value = self.font.render(str(card[1]), True, self.black)
            self.screen.blit(card_value, (x + 35, y + 50))

        # phil's hand - bottom screen
        for index, card in enumerate(self.round.phil.hand):
            x = 500 + index * 150
            y = self.screen_height - 250
            pygame.draw.rect(self.screen, self.white, (x, y, 100, 150))
            card_value = self.font.render(str(card[1]), True, self.black)
            self.screen.blit(card_value, (x + 35, y + 50))


if __name__ == "__main__":
    game = Game()
    game.run()

