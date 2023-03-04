import os
import pygame

class senyawa:
    def __init__(self, Positron, Elektron, Neutron):
        self.Positron = Positron
        self.Elektron = Elektron
        self.Neutron = Neutron

class H2O(pygame.sprite.Sprite, senyawa ):
    def __init__(self, image_path, width, height):
        pygame.sprite.Sprite.__init__(self)
        senyawa.__init__(self, Positron=10, Elektron=10, Neutron=8)
        self.image_path = os.path.join("asset/Air.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()


class unsur :
    def __init__(self, Positron, Elektron, Neutron):
        self.Positron = Positron
        self.Elektron = Elektron
        self.Neutron = Neutron

class H(pygame.sprite.Sprite, unsur):
    def __init__(self, image_path, width, height):
        pygame.sprite.Sprite.__init__(self)
        unsur.__init__(self, Positron=1, Elektron=1, Neutron=0)
        self.image_path = os.path.join("asset/Hidrogen.jpeg")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

class O(pygame.sprite.Sprite, unsur):
    def __init__(self, image_path, width, height):
        pygame.sprite.Sprite.__init__(self)
        unsur.__init__(self, Positron=8, Elektron=8, Neutron=8)
        self.image_path = os.path.join("asset/Oksigen.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

