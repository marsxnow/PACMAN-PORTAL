import pygame as pg

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename)
        pass
    
    def get_image(self, x, y, w, h):
        image_rect = pg.Rect(x, y, w, h)
        image = pg.Surface(image_rect.size).convert()
        image.blit(self.spritesheet, (0,0), image_rect)
        image.set_colorkey((0, 0, 0), pg.RLEACCEL)
        return image