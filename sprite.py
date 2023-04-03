from abc import ABC, abstractmethod

class Char(ABC):
    def __init__(self, game, images):
        self.game = game
        self.screen =  game.screen
        self.images = images
        self.rect = self.images[0].get_rect()

        self.rect.centerx = game.WIDTH / 2
        self.rect.centery = game.HEIGHT / 2

        self.speed = 2.5
        self.direcetion = None
        self.graph = None

        self.current_node = None
        self.next_node = None
        self.adj_node = None

        self.is_alive = True 

    @abstractmethod
    def move(self, direction):
        pass
    
    def draw(self, indices):
        self.screen.blit(self.images[indices[self.game.pac_img.frame_index()]], self.rect)