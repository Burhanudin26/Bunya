import pygame

from Class import *
from main import screen
import random
# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()


# Set the caption of the window
pygame.display.set_caption("My Chemical Elements")

# Set the clock to control the frame rate
clock = pygame.time.Clock()

# Create a group for all the sprites
all_sprites = pygame.sprite.Group()

# Initialize the line endpoint positions
line_start = (0, 0)
line_end = (0, 0)

# Set the line thickness
line_thickness = 5

# Lokasi garis awal
start_pos = None

# Create instances of the H and O classes with the appropriate image paths
h1 = H("asset/Hidrogen.jpeg", 50, 50)
h2 = H("asset/Hidrogen.jpeg",50,50)
o = O("asset/Oksigen.png", 50, 50)
h2o = H2O("asset/Air.png", 100, 100)

# Add the instances to the all_sprites group
all_sprites.add(h1, h2, o)
# Set up timer events to control the movement of the sprites
h_timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(h_timer_event, 3000)

o_timer_event = pygame.USEREVENT + 2
pygame.time.set_timer(o_timer_event, 3000)

# Set the loop flag
done = False

# Main game loop
while not done:
    # Handle events
    for event in pygame.event.get():
        # Pass mouse events to the H sprites

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the starting point of the line
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Get the ending point of the line
            end_pos = event.pos
            # Draw the line on the screen
            pygame.draw.line(screen, BLACK, start_pos, end_pos, line_thickness)
            # Update the Hydrogen instance with the new line segments
        elif event.type == pygame.QUIT:
            done = True
        elif event.type == h_timer_event:
            # Move the sprites
            h1.rect.x = random.randint(0, screen.get_width() - h1.rect.width)
            h1.rect.y = random.randint(0, screen.get_height() - h1.rect.height)
            h2.rect.x = random.randint(0, screen.get_width() - h2.rect.width)
            h2.rect.y = random.randint(0, screen.get_height() - h2.rect.height)
        elif event.type ==o_timer_event:
            o.rect.x = random.randint(0, screen.get_width() - o.rect.width)
            o.rect.y = random.randint(0, screen.get_height() - o.rect.height)
            # Check if two H sprites are colliding with this O sprite
            colliding_hs = [sprite for sprite in all_sprites if isinstance(sprite, H) and sprite.rect.colliderect(o.rect)]
            if len(colliding_hs) >= 2:
                # Remove the H and O sprites from the screen
                all_sprites.remove(h1, h2, o)
                for h_sprite in colliding_hs:
                    all_sprites.remove(h_sprite)

                # Add a new H2O sprite to the screen
                h2o.rect.x = o.rect.x
                h2o.rect.y = o.rect.y
                all_sprites.add(h2o)
            # Update the screen
            all_sprites.draw(screen)
            pygame.display.flip()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the sprites
    all_sprites.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()