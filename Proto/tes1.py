import pygame
pygame.init()

# Set the window size
screen_width = 1366
screen_height = 768



# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set the line thickness
line_thickness = 5

# Initialize the line endpoint positions
line_start = (0, 0)
line_end = (0, 0)

# Initialize the line segments list
line_segments = []

# Initialize the Hydrogen class
class Hydrogen(pygame.sprite.Sprite):
    def __init__(self, line_segments):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.line_segments = line_segments
        self.segment_index = 0
        self.distance = 0
        self.speed = 2

    def update(self):
        # Get the current line segment
        current_segment = self.line_segments[self.segment_index]
        segment_start, segment_end = current_segment

        # Calculate the direction vector of the segment
        segment_direction = pygame.math.Vector2(segment_end) - pygame.math.Vector2(segment_start)
        segment_length = segment_direction.length()
        segment_direction.normalize_ip()

        # Calculate the position of the Hydrogen instance along the segment
        self.distance += self.speed
        if self.distance >= segment_length:
            self.segment_index += 1
            if self.segment_index >= len(self.line_segments):
                self.segment_index = 0
            self.distance = 0
        position = pygame.math.Vector2(segment_start) + segment_direction * self.distance

        # Set the position of the Hydrogen instance
        self.rect.center = position

# Initialize the Hydrogen instance
hydrogen = Hydrogen(line_segments)
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
            # Draw the line segment on the screen
            pygame.draw.line(screen, white, start_pos, end_pos, line_thickness)
            # Add the line segment to the list
            line_segments.append((start_pos, end_pos))
            # Reset the starting position
            start_pos = None
            # Update the Hydrogen instance with the new line segments
            hydrogen.line_segments = line_segments
            hydrogen.segment_index = 0
            hydrogen.distance = 0

    # Fill the window with black
    screen.fill(black)

    # Draw the line segments on the screen
    for segment in line_segments:
        pygame.draw.line(screen, white, segment[0], segment[1])

        # Update the sprites
        all_sprites.update()

        # Draw the sprites on the screen
        all_sprites.draw(screen)

        # Update the display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()