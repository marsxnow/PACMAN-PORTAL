import pygame as pg
from map import Map

class Game:
    WIDTH = 800
    HEIGHT = 800
    def __init__(self):
        pg.init()
        self.BG_COLOR = (0, 0, 0)   
        self.screen = pg.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pg.display.set_caption('Pac-Man')            
        self.map = Map('images/maze.png', (0, 60))


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
