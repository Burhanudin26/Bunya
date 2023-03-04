
import pygame

#Initialize Pygame
pygame.init()

# Set the window size
screen_width = 1366
screen_height = 768
layar = (screen_width, screen_height)
# Create the window
screen = pygame.display.set_mode(layar)

# Load the background image
background = pygame.image.load("asset/Me2.png").convert()

# Load the font
font = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 36)

# Create the buttons
play_button = pygame.Rect(300, 300, 200, 50)
full_button = pygame.Rect(300, 400, 200, 50)
quit_button = pygame.Rect(300, 500, 200, 50)

# Run the game loop
menu_running = True
while menu_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the player clicked on a button
            if play_button.collidepoint(event.pos):
                from class_display import *
                print("Play button clicked!")
            elif full_button.collidepoint(event.pos):
                if screen.get_flags() & pygame.FULLSCREEN:
                    # Switch back to windowed mode
                    screen = pygame.display.set_mode(layar)
                else:
                    # Switch to full-screen mode
                    screen = pygame.display.set_mode(layar, pygame.FULLSCREEN)
            elif quit_button.collidepoint(event.pos):
                menu_running = False


    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the buttons
    pygame.draw.rect(screen, (255, 255, 255), play_button)
    pygame.draw.rect(screen, (255, 255, 255), full_button)
    pygame.draw.rect(screen, (255, 255, 255), quit_button)

    # Draw the text
    play_text = font.render("Play", True, (0, 0, 0))
    full_text = font.render("Fullscreen", True, (0, 0, 0))
    quit_text = font.render("Quit", True, (0, 0, 0))
    screen.blit(play_text, (play_button.centerx - play_text.get_width() // 2, play_button.centery - play_text.get_height() // 2))
    screen.blit(full_text, (full_button.centerx - play_text.get_width() // 0.9, full_button.centery - full_text.get_height() // 2))
    screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()