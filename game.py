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
    
    def display_intro(self):
        intro = (0, 1)

        font = pg.font.Font(None, 20)

        blinky_copy_rect = copy.deepcopy(self.starter_blinky_rect)
        blinky_copy_rect.centerx = 170
        blinky_copy_rect.centery = 245

        blinky_text = font.render("Blinky", True, (255, 0, 0))
        btext_rect = blinky_text.get_rect()
        btext_rect.centerx, btext_rect.centery = blinky_copy_rect.left - 50, blinky_copy_rect.centery

        self.screen.blit(self.starter_blinky[intro[self.ghost_img.frame_index()]], blinky_copy_rect)
        self.screen.blit(blinky_text, btext_rect)


        pinky_copy_rect = copy.deepcopy(self.starter_pinky_rect)
        pinky_copy_rect.centerx = 281
        pinky_copy_rect.centery = 245

        pinky_text = font.render("Pinky", True, (255, 153, 255))
        ptext_rect = pinky_text.get_rect()
        ptext_rect.centerx, ptext_rect.centery = pinky_copy_rect.right + 50, pinky_copy_rect.centery

        self.screen.blit(self.starter_pinky[intro[self.ghost_img.frame_index()]], pinky_copy_rect)
        self.screen.blit(pinky_text, ptext_rect)


        clyde_copy_rect = copy.deepcopy(self.starter_clyde_rect)
        clyde_copy_rect.centerx = 170 
        clyde_copy_rect.centery = 320

        clyde_text = font.render("Clyde", True, (255, 204, 0))
        ctext_rect = clyde_text.get_rect()
        ctext_rect.centerx, ctext_rect.centery = clyde_copy_rect.left - 50, clyde_copy_rect.centery

        self.screen.blit(self.starter_clyde[intro[self.ghost_img.frame_index()]], clyde_copy_rect)
        self.screen.blit(clyde_text, ctext_rect)


        inkey_copy_rect = copy.deepcopy(self.starter_inkey_rect)
        inkey_copy_rect.centerx = 281
        inkey_copy_rect.centery = 245

        inkey_text = font.render("Inkey", True, (255, 0, 0))
        itext_rect = inkey_text.get_rect()
        itext_rect.centerx, itext_rect.centery = inkey_copy_rect.right + 50, inkey_copy_rect.centery

        self.screen.blit(self.starter_inkey[intro[self.ghost_img.frame_index()]], inkey_copy_rect)
        self.screen.blit(inkey_text, itext_rect)



    def play(self):
        pg.mixer.music.stop()
        while self.start_screen:
            flip_time = 250
            self.handle_events()

            font = pg.font.Font(None, 25)

            play_game = font.render('Play', True, self.white)
            self.play_button_rect = play_game.get_rect()
            self.play_button_rect.center = ((self.WIDTH // 2), 475)

            get_hs = font.render('High Score', True, self.white)
            self.highscore_button_rect = get_hs.get_rect()
            self.highscore_button_rect.center = ((self.WIDTH // 2), 525)

            hs = font.render(str(self.high_score), True, self.white)
            hs_rect = self.play_button_rect

            back = font.render('Back', True, self.white)
            self.back_button_rect = back.get_rect()
            self.back_button_rect.center = ((self.WIDTH //2), 525)

            time = abs(self.last_flip - pg.time.get_ticks())
            if time >= flip_time:
                self.show = not self.show
                self.last_flip = pg.time.get_ticks()

            self.screen.fill(self.BG_COLOR)
            self.display_intro()
            if self.show and self.play_button:
                self.screen.blit(play_game, self.play_button_rect)
            if self.highscore_button:
                self.screen.blit(get_hs, self.highscore_button_rect)
            if self.back_button:
                self.screen.blit(back, self.back_button_rect)
            if self.show_highscore:
                self.screen.blit(hs, hs_rect)

            pg.display.update()
        
        #self.start_music.play()
        start_time = pg.time.get_ticks()
        while not self.start_game:
            seconds = (pg.time.get_ticks() - start_time) / 1000

            self.handle_events()
            self.update()

            self.map_elems.update()
            self.pacman.update()
            self.user_input_update()
            for ghost in self.ghosts:
                ghost.update()
            
            pg.display.update()

            if seconds > 5:
                self.start_game = True
                self.start = False

        while not self.win and not self.game_over \
              and not self.game_paused and not self.restart_life:
        
            self.handle_events()
            self.update()
            self.map_elems.update()

            self.pacman.update()
            self.user_input_update()
            for ghost in self.ghosts:
                ghost.update()
            
            pg.display.update()

            if not self.game_paused:
                self.Clock.tick(60)
            
            if self.gameover:
                self.display_game_over()
                #self.start_music.play()
                self.play()
            elif self.restart_life:
                self.restart_elements()
                self.prev_key = 'stop'
        if self.win:
            pg.mixer.music.play(-1)
            self.display_win()



 
    def update(self):
        self.screen.fill(self.BG_COLOR)
        self.screen.blit(self.map.image, self.map.rect)



def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
