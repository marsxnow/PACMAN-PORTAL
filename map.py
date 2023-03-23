from pygame import sprite
import pygame as pg

class Map(sprite):
    def __init__(self, image):
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
