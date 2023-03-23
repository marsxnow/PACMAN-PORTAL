import pygame as pg

class Game:
    WIDTH = 800
    HEIGHT = 800
    def __init__(self):
        pg.init()
        self.BG_COLOR = (0, 0, 0)   
        self.screen = pg.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pg.display.set_caption('Pac-Man')            


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
