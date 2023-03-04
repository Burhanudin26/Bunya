'''
from Class import *
import random
# Initialize the line segments list
#line_segments = []

class gameobject():
    def __init__(self, width, height, pos_x, pos_y):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y

class benda(pygame.sprite.Sprite):
    def __init__(self, line_segments):
        self.rect = self.image.get_rect()
        self.line_segments = line_segments
        self.segment_index = 0
        self.distance = 0
        self.speed = 2

    def move(self):
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
class unsur_H(H, benda):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.width = 20
        self.height = 20
        self.pos_x = random.randint(0, 640 - self.width)
        self.pos_y = random.randint(0, 480 - self.height)

class unsur_O(O, benda):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.width = 20
        self.height = 20
        self.pos_x = random.randint(0, 640 - self.width)
        self.pos_y = random.randint(0, 480 - self.height)
'''