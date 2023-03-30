import pygame as pg
from map import Map

class Game:
    WIDTH = 450
    HEIGHT = 600

    #add high score file
    #HS_File = ''

    def __init__(self):
        pg.init()
        self.BG_COLOR = (0, 0, 0)   
        self.screen = pg.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pg.display.set_caption('Pac-Man')            
        self.map = Map('images/maze.png', (0, 60))

    def play(self):
        self.screen.fill(self.BG_COLOR)
        self.screen.blit(self.map.image, self.map.rect)
        pg.display.update()

    def update(self):
        self.screen.fill(self.BG_COLOR)
        self.screen.blit(self.map.image, self.map.rect)


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
