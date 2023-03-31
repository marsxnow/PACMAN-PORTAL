from sprite import Char
from sprite_dictionary import SpriteDict

class Ghost(Char):

    def __init__(self, game, images, graph):

        super().__init__(game=game, images=images)
        self.moving = False

        self.indices = range(2)
        self.graph = graph

        self.next_node = self.graph.nodes[25]
        self.adj_node = self.graph.nodes[24]

        self.move_count = 0
        self.current_animation = []
        self.is_frame_one = False
        self.go_home = False

        self.direction = 'stop'
        self.move(self.direction)
        self.speed = 2

        sprite_dict = SpriteDict()
        self.scatter_images = sprite_dict.get_ghost_running_away_sprites()
        self.eyes_images = sprite_dict.get_ghost_eyes_sprites()


    def update(self):
        self.handle_animation()
        if self.game.has_game_started:
            self.calculate_enemy_movement()


    def move(self, direction):
        if direction == 'stop':
            self.moving = False
        else:
            self.moving = True

            if direction == 'left':
                self.rect.centerx -= self.speed
            elif direction == 'right':
                self.rect.centerx += self.speed
            elif direction == 'up':
                self.rect.centery -= self.speed
            elif direction == 'down':
                self.rect.centery += self.speed
