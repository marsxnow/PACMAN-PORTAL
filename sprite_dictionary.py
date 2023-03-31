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
        self.pac_life = self.sprite_sheet.get_image(x=48, y=72, w=24,h=23)

    def get_pacman_sprites(self):
        pacman_sprite = [self.sprite_sheet.get_image(x=0, y=168, w=24, h=24),
                         self.sprite_sheet.get_image(x=48, y=72, w=24, h=24),
                         self.sprite_sheet.get_image(x=0, y=72, w=24, h=24),
                         self.sprite_sheet.get_image(x=144, y=72, w=24, h=24),
                         self.sprite_sheet.get_image(x=96, y=72, w=24, h=24),
                         self.sprite_sheet.get_image(x=72, y=72, w=24, h=24),
                         self.sprite_sheet.get_image(x=24, y=72, w=24, h=24),
                         self.sprite_sheet.get_image(x=168, y=72, w=24, h=24),
                         self.sprite_sheet.get_image(x=120, y=72, w=24, h=24)]
        return pacman_sprite
    
    def get_pacman_dying_sprites(self):
        pacman_dying_sprite = [self.sprite_sheet.get_image(x=0, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=72, y=72, w=24, h=24),
                               self.sprite_sheet.get_image(x=24, y=72, w=24, h=24),
                               self.sprite_sheet.get_image(x=96, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=120, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=144, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=168, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=192, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=216, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=240, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=264, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=288, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=312, y=168, w=24, h=24),
                               self.sprite_sheet.get_image(x=336, y=168, w=24, h=24)]
        return pacman_dying_sprite

    def get_blinky_sprites(self):
        blinky_sprite = [self.sprite_sheet.get_image(x=0, y=144, w=24, h=24),
                        self.sprite_sheet.get_image(x=24, y=144, w=24, h=24),
                        self.sprite_sheet.get_image(x=48, y=144, w=24, h=24),
                        self.sprite_sheet.get_image(x=72, y=144, w=24, h=24),
                        self.sprite_sheet.get_image(x=96, y=144, w=24, h=24),
                        self.sprite_sheet.get_image(x=120, y=144, w=24, h=24),
                        self.sprite_sheet.get_image(x=144, y=144, w=24, h=24),
                        self.sprite_sheet.get_image(x=168, y=144, w=24, h=24)]
        return blinky_sprite
    
    def get_inky_sprites(self):
        inky_sprite = [self.sprite_sheet.get_image(x=192, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=216, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=240, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=264, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=288, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=312, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=336, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=360, y=192, w=24, h=24)]
        return inky_sprite
    
    def get_pinky_sprites(self):
        pinky_sprite = [self.sprite_sheet.get_image(x=0, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=24, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=48, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=72, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=96, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=120, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=144, y=192, w=24, h=24),
                        self.sprite_sheet.get_image(x=168, y=192, w=24, h=24)]
        return pinky_sprite

    def get_clyde_sprites(self):
         clyde_sprite = [self.sprite_sheet.get_image(x=0, y=216, w=24, h=24),
                        self.sprite_sheet.get_image(x=24, y=216, w=24, h=24),
                        self.sprite_sheet.get_image(x=48, y=216, w=24, h=24),
                        self.sprite_sheet.get_image(x=72, y=216, w=24, h=24),
                        self.sprite_sheet.get_image(x=96, y=216, w=24, h=24),
                        self.sprite_sheet.get_image(x=120, y=216, w=24, h=24),
                        self.sprite_sheet.get_image(x=144, y=216, w=24, h=24),
                        self.sprite_sheet.get_image(x=168, y=216, w=24, h=24)]
         return clyde_sprite

    def get_ghosts_running_away_sprites(self): 
        running_away_sprite = [self.sprite_sheet.get_image(x=144, y=96, w=24, h=24),
                               self.sprite_sheet.get_image(x=168, y=96, w=24, h=24),
                               self.sprite_sheet.get_image(x=192, y=96, w=24, h=24),
                               self.sprite_sheet.get_image(x=216, y=96, w=24, h=24)]
        return running_away_sprite
    
    def get_ghosts_eyes_sprites(self):
        ghost_eye_sprite = [self.sprite_sheet.get_image(x=192, y=216, w=24, h=24),
                            self.sprite_sheet.get_image(x=216, y=216, w=24, h=24),
                            self.sprite_sheet.get_image(x=240, y=216, w=24, h=24),
                            self.sprite_sheet.get_image(x=264, y=216, w=24, h=24),
                            self.sprite_sheet.get_image(x=288, y=216, w=24, h=24),
                            self.sprite_sheet.get_image(x=312, y=216, w=24, h=24),
                            self.sprite_sheet.get_image(x=336, y=216, w=24, h=24),
                            self.sprite_sheet.get_image(x=360, y=216, w=24, h=24)]
        return ghost_eye_sprite
        
    def get_numbers(self):
        number_sprites = [self.sprite_sheet.get_image(x=192, y=144, w=24, h=24),
                          self.sprite_sheet.get_image(x=216, y=144, w=24, h=24),
                          self.sprite_sheet.get_image(x=240, y=144, w=24, h=24),
                          self.sprite_sheet.get_image(x=264, y=144, w=24, h=24)]
        return number_sprites

    def get_unscaled_portal_sprites(self):pass

    def get_food_sprites(self):
        fruit_sprite = [self.sprite_sheet.get_image(x=0, y=120, w=24, h=24),    # cherries
                        self.sprite_sheet.get_image(x=24, y=120, w=24, h=24),    # strawberry
                        self.sprite_sheet.get_image(x=48, y=120, w=24, h=24),    # orange
                        self.sprite_sheet.get_image(x=72, y=120, w=24, h=24),    # ?????
                        self.sprite_sheet.get_image(x=96, y=120, w=24, h=24),    # apple
                        self.sprite_sheet.get_image(x=120, y=120, w=24, h=24),]
        return fruit_sprite