import pygame as pg
from pygame.sprite import Sprite

class Map(Sprite):
    def __init__(self, image, position):
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position