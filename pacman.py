from sprite import Char
import pygame as pg
import copy
from sprite_dictionary import SpriteDict

class Pacman(Char):
    def __init__(self, game, images, map_elements):
        super().__init__(game=game, images=images)
        self.lives = 3
        self.moving = False

        self.map_elem = map_elements

        self.current_node = self.map_elem.nodes[65]
        self.next_node = self.map_elem.nodes[65]
        self.adj_node = self.map_elem.nodes[45]

        sprite_dict = SpriteDict()
        self.number_images = sprite_dict.get_numbers()
        self.number_rect = self.number_images[0].get_rect()
        self.number_duration = 3000
        self.number_start = pg.time.get_ticks()
        self._200_ = False
        self.rect_200_ = copy.deepcopy(self.number_rect)
        self._400_ = False
        self.rect_400_ = copy.deepcopy(self.number_rect)
        self._800_ = False
        self.rect_800_ = copy.deepcopy(self.number_rect)
        self._1600_ = False
        self.rect_1600_ = copy.deepcopy(self.number_rect)

        self.port_cool_down = 1000
        self.last_tp = pg.time.get_ticks()
        
        self.pow_pel_mode = False
        self.pow_pel_mode_start = pg.time.get_ticks()
        self.pow_pel_duration = 8500
        self.enemy_consum = 0
        
        self.speed = 3.5
        self.portal_reset = False
        
        self.sound = None
        
        self.direction = 'stop'
        
        self.elapsed_00 = pg.time.get_ticks()
        self.elapsed_01 = pg.time.get_ticks()

        dying_images = self.game.sprite_dictionary.get_pacman_dying_sprites()
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

    
    def update(self):

        self.elapsed_00 = pg.time.get_ticks() - self.elapsed_00
        if self.elapsed_00 > 200:  # animate every 1/2 second
            self.handle_animation()

        self.elapsed_01 = pg.time.get_ticks() - self.elapsed_01

        if not self.get_enemy_collision():
            self.handle_animation()
            self.calculate_player_movement()
            self.eat()
            self.manage_op()
        else:
            self.die()
            self.game.start_game = False
        self.print_scores()

          
    def die(self):
        self.game.start_game = False

        #Death sound
        self.game.voice.play(self.game.death_sound)
        last_change = pg.time.get_ticks()
        time_elapsed = abs(last_change - pg.time.get_ticks())
        self.finished = False

        # change frame every 145 ms
        while not self.finished:     # stall for duration of RIP sound, keep updating screen
            if time_elapsed > 75:
                self.dying_index += 1
                last_change = pg.time.get_ticks()

            self.game.handle_events()  # Get user input
            self.game.update()  # Update this (Game) instance

            self.graph.update() 

            self.draw_death()
            self.game.user_input_update()
            for ghost in self.game.ghosts:
                ghost.update()

            pg.display.update()  # Tell game engine to update this games display

            time_elapsed = abs(last_change - pg.time.get_ticks())

        start = pg.time.get_ticks()
        time_elapsed = abs(start - pg.time.get_ticks())

        while time_elapsed < 2000:      # stall for 2 seconds
            self.game.handle_events()  # Get user input
            self.game.update()  # Update this (Game) instance

            self.graph.update()  

            self.game.user_input_update()
            for ghost in self.game.ghosts:  # Update (Enemy) instances
                ghost.update()

            pg.display.update()

            time_elapsed = abs(start - pg.time.get_ticks())

        self.game.restart_life = True
        print('new life, lives left: ' + str(self.lives))

        if self.lives <= 0:
            self.game.game_over = True
            print ('game 0ver')
        
    def calc_pacman_movement(self):
        if self.game.start_game:

            if(self.direction is None or self.direction == 'stop') \
            and self.map_elem.valid_move(self.current_node, self.game.last_key):
                
                adj_list = self.map_elem.adj_path(self.current_node, self.game.last_key)
                self.adj_node = adj_list[0]
                self.next_node = adj_list[len(adj_list) - 1]

                if self.map_elem.valid_move(self.current_node, self.game.last_key):
                    self.direction = self.game.last_key
                    self.move(self.direction) 
        
            elif self.direction == 'left' or self.direction == 'right' \
                    or self.direction == 'up' or self.direction == 'down':
                
                if self.get_portal_collision() and not self.portal_reset:

                    self.teleport(self.get_portal_collision())
                    self.move(self.direction)
            
                else:
                    if len(self.map_elem.get_buffer(self, self.direction)) > 0:
                        collide_point_x = self.map_elem.get_buffer(self, self.direction)[0]
                        collide_point_y = self.map_elem.get_buffer(self, self.direction)[1]
                    
                    if self.rect.collidepoint(collide_point_x, collide_point_y):
                        if self.portal_reset:
                            self.portal_reset = not self.portal_reset
                        
                        self.current_node = self.adj_node
                    
                        if self.map_elem.valid_move(self.current_node, self.game.last_key):
                            self.direction = self.game.last_key
                            adj_list = self.map_elem.adj_path(self.current_node, self.game.last_key)
                            self.adj_node = adj_list[0]
                            self.next_node = adj_list[len(adj_list) - 1]
                    
                        elif self.map_elem.valid_move(self.current_node, self.direction):
                            adj_list = self.map_elem.adj_path(self.current_node, self.direction)
                            self.adj_node = adj_list[0]
                            self.next_node = adj_list[len(adj_list) - 1] 
                            self.move(self.direction)
                
                        else:
                            self.direction = 'stop'
                            self.move(self.direction)
                    else:
                        self.move(self.direction)

    def move(self, direction):
        
        if direction == 'stop':
            self.moving = False
            self.direction = 'stop'
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
    
    def print_scores(self):
        if self.pow_pel_mode:
            if self._200_:
                self.screen.blit(self.number_images[0], self.rect_200_)
            if self._400_:
                self.screen.blit(self.number_images[1], self.rect_400_)
            if self._800_:
                self.screen.blit(self.number_images[2], self.rect_800_)
            if self._1600_:
                self.screen.blit(self.number_images[3], self.rect_1600_)
    
    def eat(self):
        for pellet in self.map_elem.pellets:
            if pellet.rect.colliderect(self.rect):
                self.game.score += 10
                self.map_elem.pellets.remove(pellet)

                self.game.eating_sound.set_volume(.4)
                self.game.voice.play(self.game.eating_sound)
        
        for pow_pellet in self.map_elem.pow_pellets:

            if pow_pellet.rect.colliderect(self.rect):
                self.game.score += 50
                self.map_elem.pow_pellets.remove(pow_pellet)
                self.pp()

                self.game.eating_sound.set_vloume(.4)
                self.game.voice.play(self.game.eating_sound)

        if self.pow_pel_mode:
            for ghost in self.game.ghosts:
                if self.rect.colliderect(ghost.rect) and not ghost.go_home:
                    ghost.go_home = True
                    self.enemy_consum += 1
                    self.game.score += 200 * self.enemy_consum
                    self.game.eat_ghost_sound.set_volume(.99)
                    self.game.voice.play(self.game.eat_ghost_sound)
                    if self.enemy_consum == 1:
                        self._200_ = True
                        self.rect_200_ = copy.deepcopy(ghost.rect)
                    if self.enemy_consum == 2:
                        self._400_ = True
                        self.rect_400_ = copy.deepcopy(ghost.rect)
                    if self.enemy_consum == 3:
                        self._800_ = True
                        self.rect_800_ = copy.deepcopy(ghost.rect)
                    if self.enemy_consum == 4:
                        self._1600_ = True
                        self.rect_1600_ = copy.deepcopy(ghost.rect)
        
        if not self.map_elem.pellets and not self.map_elem.pow_pellets:
            self.game.win = True
        
        if self.map_elem.fruit_exists and self.map_elem.fruit_rect.colliderect(self.rect):
            self.map_elem.fruit_exists = False
            self.game.score += 100 * (self.map_elem.fruit_index + 1)

            self.game.eating_sound.set_volume(.4)
            self.game.voice.play(self.game.eating_sound)

    def pp(self):
        self.pow_pel_mode_start = pg.time.get_ticks()
        self.pow_pel_mode = True
    

    def manage_op(self):
        now = pg.time.get_ticks()
        if abs(self.pow_pel_mode_start - now) >= self.pow_pel_duration:
            self.pow_pel_mode = False
            self.enemy_consum = 0
            self._200_ = False
            self._400_ = False
            self._800_ = False
            self._1600_ = False


    def get_portal_collision(self):
        if self.game.portal1.open and self.game.portal2.open:

            p1_x = self.game.portal1.current_node.x
            p1_y = self.game.portal1.current_node.y

            p2_x = self.game.portal2.current_node.x
            p2_y = self.game.portal2.current_node.y

            if self.rect.collidepoint(p1_x, p1_y):
                return self.game.portal2.current_node

            elif self.rect.collidepoint(p2_x, p2_y):
                return self.game.portal1.current_node

        return False

    def get_enemy_collision(self):
        if self.pow_pel_mode:
            pass
        else:
            for ghost in self.game.ghosts:

                p1_x = ghost.current_node.x
                p1_y = ghost.current_node.y

                if self.rect.colliderect(ghost.rect) and not ghost.go_home:

                    self.lives -= 1

                    if not self.game.restart_life:
                        return True
    
    def teleport(self, destination_node):
        now = pg.time.get_ticks()

        if abs(self.last_tp - now) >= self.cd:      # if cd time is over

            # Set current node to the node pac-man collided with
            self.current_node = destination_node
            self.rect.centerx = destination_node.x
            self.rect.centery = destination_node.y

            # Valid move in the requested direction
            if self.map_elem.valid_move(self.current_node, self.game.last_key):
                self.direction = self.game.last_key
                adj_list = self.map_elem.adj_path(self.current_node, self.game.last_key)
                self.adj_node = adj_list[0]
                self.next_node = adj_list[len(adj_list) - 1]
                self.game.tp_sound.set_volume(.99)
                self.game.portal.play(self.game.tp_sound)

            # Requested movement was invalid
            # --> Same direction movement is valid
            elif self.map_elem.valid_move(self.current_node, self.direction):
                adj_list = self.map_elem.adj_path(self.current_node, self.direction)
                self.adj_node = adj_list[0]
                self.next_node = adj_list[len(adj_list) - 1]
                
            # Both requested and same direction movement return invalid
            else:
                self.direction = 'stop'

                # Set portal reset to True
                self.portal_reset = True

        self.last_tp = now
    

    def handle_animation(self):
        if self.direction == 'left' and self.moving:
            indices = (0, 1, 2)
            self.draw(indices=indices)
            self.game.last_pac_img = indices[self.game.pac_img.frame_index()]
        elif self.direction == 'right' and self.moving:
            indices = (0, 3, 4)
            self.draw(indices=indices)
            self.game.last_pac_img = indices[self.game.pac_img.frame_index()]
        elif self.direction == 'up' and self.moving:
            indices = (0, 5, 6)
            self.draw(indices=indices)
            self.game.last_pac_img = indices[self.game.pac_img.frame_index()]
        elif self.direction == 'down' and self.moving:
            indices = (0, 7, 8)
            self.draw(indices=indices)
            self.game.last_pac_img = indices[self.game.pac_img.frame_index()]
        else:  
            self.screen.blit(self.images[self.game.last_pac_img], self.rect)

    def draw_death(self):
        if self.game.last_key == 'left':
            self.screen.blit(self.dying_L[self.dying_index], self.rect)
        elif self.game.last_key == 'right' or self.game.last_key == 'stop':
            self.screen.blit(self.dying_R[self.dying_index], self.rect)
        elif self.game.last_key == 'up':
            self.screen.blit(self.dying_U[self.dying_index], self.rect)
        elif self.game.last_key == 'down':
            self.screen.blit(self.dying_D[self.dying_index], self.rect)

        if self.dying_index == 13:  # dying animation is finished -- reset
            self.dying_index = 0
            self.game.last_pac_img = 0
            self.finished = True