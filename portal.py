from sprite import Char

class Portal(Char):
    def __init__(self, game, images):
        super().__init__(game=game, images=images)
        self.exists = False
        self.current_node = None
        self.destination_node = None
        self.map = game.map_elems
        self.speed = 5
        self.indices = range(6)
        self.open = False

    def move(self):
        if self.direction == 'left':
            if self.rect.centerx >= self.destination_node.x:
                self.rect.centerx -= self.speed
            else:
                self.current_node = self.destination_node
                self.open = True

        elif self.direction == 'right':
            if self.rect.centerx <= self.destination_node.x:
                self.rect.centerx += self.speed
            else:
                self.current_node = self.destination_node
                self.open = True

        elif self.direction == 'up':
            if self.rect.centery >= self.destination_node.y:
                self.rect.centery -= self.speed
            else:
                self.current_node = self.destination_node
                self.open = True

        elif self.direction == 'down':
            if self.rect.centery <= self.destination_node.y:
                self.rect.centery += self.speed
            else:
                self.current_node = self.destination_node
                self.open = True  
    
    def fire(self):
        self.game.portal_shoot.set_volume(.4)
        self.game.portal.play(self.game.portal_shoot)
        self.open = False
        self.exists = True
        self.direction = self.game.pacman.direction
        self.current_node = self.game.pacman.next_node
        self.rect.centerx = self.game.pacman.rect.centerx
        self.rect.centery = self.game.pacman.rect.centery

        if self.graph.is_valid_move(self.current_node, self.direction):
            adj_list = self.graph.get_adj_path(self.current_node, self.game.last_key)
            self.next_node = adj_list[len(adj_list) - 1]

        self.destination_node = self.current_node
    
    def draw(self, indices):        # overwrite for ghost because more animations (e.g. blue/white or just eyes)
        self.screen.blit(self.images[indices[self.game.portal_img.frame_index()]], self.rect)

    def update(self):
        if not self.exists:
            pass
        else:
            self.move()
            self.draw(self.indices)
