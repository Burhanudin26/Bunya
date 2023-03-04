from Object import *
pygame.init()

# Set the window size
screen_width = 1366
screen_height = 768

# Create the window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set the line thickness
line_thickness = 5

# Initialize the line endpoint positions
line_start = (0, 0)
line_end = (0, 0)

# Initialize the Hydrogen instance
hydrogen = unsur_H(line_segments)
all_sprites = pygame.sprite.Group()
all_sprites.add(hydrogen)

# Run the game loop
running = True
start_pos = None
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the starting point of the line
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Get the ending point of the line
            end_pos = event.pos
            # Draw the line on the screen
            pygame.draw.line(screen, white, start_pos, end_pos, line_thickness)
            # Update the Hydrogen instance with the new line segments
            unsur_H.line_segments = line_segments
            unsur_H.segment_index = 0
            unsur_H.distance = 0
    # Update the sprites
    all_sprites.update()

    # Draw the sprites on the screen
    all_sprites.draw(screen)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
