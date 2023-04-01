import pygame as pg 
from pygame.sprite import Sprite

class Node(Sprite):
    def __init__(self, game,  x, y, adj=None, adjw=[]):
        super().__init__()
        self.screen = game.screen
        self.x, self.y = x, y + 60
        self.adj = adj
        self.adjw = adjw
        self.rect = pg.Rect(self.x, self.y, 1, 1)
        self.game = game

        self.exists = True
    
    def update(self, type):
        self.draw(type=type)
        self.rect = pg.Rect(self.x, self.y, 3, 3)
    
    def draw(self, type):
        if type == 'pe':
            pg.draw.circle(self.screen, (255, 255, 0), (self.x, self.y), 3)
        elif type == 'pp':
            pg.draw.circle(self.screen, (255, 255, 0), (self.x, self.y), 6)
        elif type == 'no':
            pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(self.x, self.y, 3, 3))