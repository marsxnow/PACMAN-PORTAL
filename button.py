import pygame as pg

class Button: 

    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (249, 241, 0)
        self.temp_colot = self.text_color
        self.font = pg.font.Font(None, 48) 

        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.msg_img = self.font.render(msg, True, self.text_color,
                                                   self.button_color)

        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color,
                                        self.button_color)
        
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)