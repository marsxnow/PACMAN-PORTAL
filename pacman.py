from sprite import Char
import pygame as pg
import copy
from sprite_dictionary import SpriteDict

class Pacman(Char):
    def __init__(self, game, images, map):
        super().__init__(game=game, images=images)
        self.lives = 3
        self.moving = False

        self.map = map

        self.current_node = self.map.nodes[65]
        self.next_node = self.map.nodes[65]
        self.adj_node = self.map.node[45]

        sprite_dict = SpriteDict()
        self.number_images = sprite_dict.get_numbers()
        self.number_rect = self.number_images[0].get_rect()
        self.number_duration = 3000
        self.number_start = pg.time.get_ticks()
        self._200_ = False
        self.rect_200_ = copy.deepcopy(self.numbers_rect)
        self._400_ = False
        self.rect_400_ = copy.deepcopy(self.numbers_rect)
        self._800_ = False
        self.rect_800_ = copy.deepcopy(self.numbers_rect)
        self._1600_ = False
        self.rect_1600_ = copy.deepcopy(self.numbers_rect)

        self.port_cool_down = 1000
        self.last_tp = pg.time.get_ticks()
        self.pow_pel_mode = False
        self.pow_pel_mode_start = pg.time.get_ticks()
        self.pow_pel_duration = 8500
        self.enemy_consum = 0
        self.speed = 3.5
        self.portal_reset = False
        self.sound = None
        self.direcetion = 'stop'
        
        self.elapsed_00 = pg.time.get_ticks()
        self.elapsed_01 = pg.time.get_ticks()

        dying_images = self.game.sprite_dict.get_pacman_dying_sprites()
        self.dying_start = pg.time.get_ticks()
        self.dying_index = 0
        self.finish = False

        self.dying_up = []
        for image in dying_images:
            temp = pg.transform.rotate(image, 0)
            self.dying_up.append(temp)
        
        self.dying_left = []
        for image in dying_images:
            temp = pg.transform.rotate(image, 90)
            self.dying_left.append(temp)
        
        self.dying_down = []
        for image in dying_images:
            temp = pg.transform.rotate(image, 180)
            self.dying_down.append(temp)
        
        self.dying_right = []
        for image in dying_images:
            temp = pg.transform.rotate(image, 270)
            self.dying_right.append(temp)