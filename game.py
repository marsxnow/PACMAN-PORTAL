import pygame as pg
from map import Map
from timer import Timer, DualTimer 
from sprite_dictionary import SpriteDict
from ghosts import Ghost
from pacman import Pacman
from map_elements import Elements
from pygame.sprite import Group
from os import path
from pygame import color
import sys
import copy


class Game:
    WIDTH = 450
    HEIGHT = 600

    highscore_file = 'highscore.txt'

    def __init__(self):
        pg.init()
        self.BG_COLOR = (0, 0, 0)   
        self.screen = pg.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pg.display.set_caption('Pac-Man')            
       
        self.Clock = pg.time.Clock()
        self.pac_img = Timer(3)
        self.last_pac_img = self.pac_img.frame_index()

        self.ghost_img = Timer(2)
        self.last_ghost_img = self.ghost_img.frame_index()
        self.ghost_scatter_img = DualTimer(2, 4)

        self.sprite_dictionary = SpriteDict()

        ###Insert Portal Sauce###

        #########################

        self.map_elems = Elements(self)

        self.pacman = Pacman(self, self.sprite_dictionary.pacman, self.map_elems)

        self.blinky = Ghost(self, self.sprite_dictionary.blinky, self.map_elems)
        self.pinky = Ghost(self, self.sprite_dictionary.pinky, self.map_elems)
        self.clyde = Ghost(self, self.sprite_dictionary.clyde, self.map_elems)
        self.inkey = Ghost(self, self.sprite_dictionary.inkey, self.map_elems)
        self.ghosts = []
        self.ghosts.append(self.blinky, self.pinky, self.clyde, self.inkey)

        self.map = Map('images/maze.png', (0, 60))
        
        ##########Find Diff Logo##########
        ##################################

        self.pacman.rect.centerx = self.map_elems.nodes[65].x
        self.pacman.rect.centery = self.map_elems.nodes[65].y
        self.pacman.adj_node = self.map_elems.nodes[65]

        self.initialize_ghosts()
        self.pellets = Group()

        for pellet in self.map_elems.pellets:
            self.pellets.add(pellet)

        self.score = 0
        self.high_score = 0
        self.win = False
        self.prev_key = None

        self.start_screen =  True

        self.start = True
        self.game_paused = False
        self.gameover = False
        self.restart_life =False
        self.start_game = False

        self.play_button = True
        self.play_button_rect = None
        self.show_highscore = False
        self.highscore_button = True
        self.highscore_button_rect = None
        self.back_button = False
        self.back_button_rect = None

        self.last_flip = pg.time.get_ticks()
        self.show = True
        
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)

        self.pac_life_img = self.sprite_dictionary.pac_life
        self.cherry_img = self.sprite_dictionary.fruits[0]
        self.sound_img = pg.image.load()

        self.load_HS()

        pg.mixer.init()

        pacman_imgs = self.sprite_dictionary.get_pacman_sprites()
        self.starter_pac = []
        for img in pacman_imgs:
            self.starter_pac.append(pg.transform.scale(img, (48, 48)))
        self.starter_pac_rect = self.starter_pac[0].get_rect()
        self.starter_pac_rect.centerx = -48
        self.starter_pac_rect.centery = 430

        blinky_imgs = self.sprite_dictionary.get_blinky_sprites()
        self.starter_blinky = []
        for img in blinky_imgs:
            self.starter_blinky.append(pg.transform.scale(img, (48, 48)))
        self.starter_blinky_rect = self.starter_blinky[0].get_rect()
        self.starter_blinky_rect.centerx = -144
        self.starter_blinky_rect.centery = 430

        pinky_imgs = self.sprite_dictionary.get_pinky_sprites()
        self.starter_pinky = []
        for img in pinky_imgs:
            self.starter_pinky.append(pg.transform.scale(img, (48, 48)))
        self.starter_pinky_rect = self.starter_pinky[0].get_rect()
        self.starter_pinky_rect.centerx = -199
        self.starter_pinky_rect.centery = 430            
        

        clyde_imgs = self.sprite_dictionary.get_clyde_sprites()
        self.starter_clyde = []
        for img in clyde_imgs:
            self.starter_clyde.append(pg.transform.scale(img, (48, 48)))
        self.starter_clyde_rect = self.starter_clyde[0].get_rect()
        self.starter_clyde_rect.centerx = -254
        self.starter_clyde_rect.centery = 430            

        inkey_imgs = self.sprite_dictionary.get_inky_sprites()
        self.starter_inkey = []
        for img in inkey_imgs:
            self.starter_inkey.append(pg.transform.scale(img, (48, 48)))
        self.starter_inkey_rect = self.starter_inkey[0].get_rect()
        self.starter_inkey_rect.centerx = -309
        self.starter_inkey_rect.centery = 430       


        intro_runaway = self.sprite_dictionary.get_ghosts_running_away_sprites()
        self.starter_runaway = []
        for img in intro_runaway:
            self.starter_runaway.append(pg.transform.scale(img, (48, 48)))

        

        self.starter_right = True

    def load_high_score(self):
        self.file = path.dirname(__file__)
        with open(path.join(self.file, self.highscore_file), 'r') as f:
            try:
                self.high_score = int(f.read())
            except:
                self.high_score = 0
        




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
