from sprite import Char
from sprite_dictionary import SpriteDict

class Ghost(Char):

    def __init__(self, game, images, map_elements):

        super().__init__(game=game, images=images)
        self.moving = False

        self.indices = range(2)
        self.map = map_elements

        self.next_node = self.map.nodes[25]
        self.adj_node = self.map.nodes[24]

        self.move_count = 0
        self.current_animation = []
        self.is_frame_one = False
        self.go_home = False

        self.direction = 'stop'
        self.move(self.direction)
        self.speed = 2

        sprite_dict = SpriteDict()
        self.scatter_images = sprite_dict.get_ghosts_running_away_sprites()
        self.eyes_images = sprite_dict.get_ghosts_eyes_sprites()


    def update(self):
        self.handle_animations()
        if self.game.start_game:
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
    
    def calculate_enemy_movement(self):
        if len(self.map.get_buffer(self, self.direction)) > 0:
            collide_point_x = self.map.get_buffer(self, self.direction)[0]
            collide_point_y = self.map.get_buffer(self, self.direction)[1]
        else:
            collide_point_x = 0
            collide_point_y = 0
            self.direction = 'stop'
        
        if self.direction == 'stop':
            if self.game.start_game:
                short_path = self.map.get_shortest_path(self.current_node, self.game.pacman.adj_node)

                if len(short_path) > 0:
                    self.adj_node = short_path[0].node
                    self.direction = self.map.directions(self.current_node, self.adj_node)
        else:
            if self.rect.collidepoint(collide_point_x, collide_point_y):
                self.current_node = self.adj_node
                short_path = self.map.get_shortest_path(self.current_node, self.game.pacman.adj_node)

                if self.current_node is not self.game.pacman.current_node:
                    if len(short_path) > 0:
                        self.adj_node = short_path[0].node
                        self.direction = self.map.direction(self.current_node, self.adj_node)
                else:
                    self.direction = 'stop'
            self.move(self.direction)
    
    def handle_animations(self):
        if self.go_home:
            if self.direction == 'left' and self.moving:
                indices = (4, 5)
                self.draw(indices=indices)
                self.game.last_ghost_img = indices[self.game.ghost_img.frame_index()]
            elif self.direction == 'right' and self.moving:
                indices = (0, 1)
                self.draw(indices=indices)
                self.game.last_ghost_img = indices[self.game.ghost_img.frame_index()]

            elif self.direction == 'up' and self.moving:
                indices = (6, 7)
                self.draw(indices=indices)
                self.game.last_ghost_img = indices[self.game.ghost_img.frame_index()]

            elif self.direction  == 'down' and self.moving:
                indices = (2,3)
                self.draw(indices=indices)
                self.draw.last_ghost_img = indices[self.game.ghost_img.frame_index()]
        else:
            if self.direction == 'left' and self.moving:
                indices = (4, 5)
                self.draw(indices=indices)
                self.game.last_ghost_img = indices[self.game.ghost_img.frame_index()]
            elif self.direction == 'right' and self.moving:
                indices = (0, 1)
                self.draw(indices=indices)
                self.game.last_ghost_img = indices[self.game.ghost_img.frame_index()]
            elif self.direction == 'up' and self.moving:
                indices = (6, 7)
                self.draw(indices=indices)
                self.game.last_ghost_img = indices[self.game.ghost_img.frame_index()]
            elif self.direction == 'down' and self.moving:
                indices = (2, 3)
                self.draw(indices=indices)
                self.game.last_ghost_img = indices[self.game.ghost_img.frame_index()]
            else:
                if self.game.last_pac_img >= 0 and self.game.last_pac_img < len(self.images):
                    self.screen.blit(self.images[self.game.last_pac_img], self.rect)
                else:
                    self.screen.blit(self.images[0], self.rect)

    def draw(self, indices):
        if self.game.pacman.pow_pel_mode and not self.go_home:
            self.screen.blit(self.scatter_images[self.game.ghost_scatter_img.frame_index()], self.rect)
        elif self.go_home:
            self.screen.blit(self.eyes_images[indices[self.game.ghost_img.frame()]], self.rect)
        else:
            self.screen.blit(self.images[indices[self.game.ghost_imf.frame()]], self.rect)
                