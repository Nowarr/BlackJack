import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BlackJack")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load the EB Garamond font (Ensure the path is correct)
font_path = '../resources/EBG-Reg.ttf'
font_size = 30
font = pygame.font.Font(font_path, font_size)

def game_window():
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 20 <= mouse[0] <= 160 and screen_height - 60 <= mouse[1] <= screen_height - 20:
                    print("HIT button clicked!")
                    # Handle HIT logic here
                elif 180 <= mouse[0] <= 320 and screen_height - 60 <= mouse[1] <= screen_height - 20:
                    print("STAND button clicked!")
                    # Handle STAND logic here

        # Fill the screen with a background color
        screen.fill(black)

        # Draw the line across the screen to split it in two
        pygame.draw.line(screen, white, (0, screen_height // 2), (screen_width, screen_height // 2), 2)

        # Draw the HIT button
        hit_button_rect = pygame.Rect(20, screen_height - 60, 140, 40)
        pygame.draw.rect(screen, white, hit_button_rect)

        # Render the text on the HIT button
        hit_text = font.render("HIT", True, black)
        hit_text_rect = hit_text.get_rect(center=hit_button_rect.center)
        screen.blit(hit_text, hit_text_rect)

        # Draw the STAND button to the right of the HIT button
        stand_button_rect = pygame.Rect(180, screen_height - 60, 140, 40)
        pygame.draw.rect(screen, white, stand_button_rect)

        # Render the text on the STAND button
        stand_text = font.render("STAND", True, black)
        stand_text_rect = stand_text.get_rect(center=stand_button_rect.center)
        screen.blit(stand_text, stand_text_rect)

        # Update the display
        pygame.display.flip()

    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_window()

