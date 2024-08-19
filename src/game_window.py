import pygame
import sys
from src.button import Button
from src.dealer import Dealer

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
        font_path = 'resources/EBGaramond-Regular.ttf'
        font_size = 30
        self.font = pygame.font.Font(font_path, font_size)

        # Create buttons
        self.hit_button = Button(self.screen, "HIT", 20, self.screen_height - 60, 140, 40, self.font, self.black, self.white)
        self.stand_button = Button(self.screen, "STAND", 180, self.screen_height - 60, 140, 40, self.font, self.black, self.white)
        
        # Initialize Dealer
        self.dealer = Dealer()

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

    def handle_hit(self):
        print("HIT button clicked!")
        # Add dealer handing card logic here using self.dealer

    def handle_stand(self):
        print("STAND button clicked!")
        # Add logic for stand action here

    def update_screen(self):
        self.screen.fill(self.black)
        pygame.draw.line(self.screen, self.white, (0, self.screen_height // 2), (self.screen_width, self.screen_height // 2), 2)
        self.hit_button.draw()
        self.stand_button.draw()
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

