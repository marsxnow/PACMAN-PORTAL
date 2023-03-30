from spritesheet import Spritesheet
import pygame as pg

class SpriteDict:
    def __init__(self):

        self.sprite_sheet = Spritesheet('image/spritesheet.png')

        self.pacman = self.get_pacman_sprites()
        self.blinky = self.get_blinky_sprites()
        self.inkey = self.get_inky_sprites()
        self.pinky = self.get_pinky_sprites()
        self.clyde = self.get_clyde_sprites()

        self.portal = self.get_unscaled_portal_sprites()
        self.fruits = self.get_fruits_sprites()

        #check if sprite correct
        self.pac_life = self.sprite_sheet.get_image(x=(24 *2), y=(24*3), w=24,h=23)

    def get_pacman_sprites(self):
        pacman_sprite = [self.sprite_sheet.get_image(x = 0, y = )]

    
        return pacman_sprite
    def get_pacman_dying_sprites(self): pass

    def get_blinky_sprites(self):pass
    def get_inky_sprites(self):pass
    def get_pinky_sprites(self):pass
    def get_clyde_sprites(self):pass 

    def get_ghosts_running_away_sprites(self): pass
    def get_ghosts_eyes_sprites(self):pass

    def get_numbers(self):pass
    def get_unscaled_portal_sprites(self):pass
    def get_food_sprites(self):pass
    