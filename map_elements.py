from node import Node
from paths import Path
import math

class Elements:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.nodes = []
        self.ghost_nodes = []
        self.super_nodes = []

        self.pellets = []
        self.pow_pellets = []

        self.fruit = self.game.sprite_dictionary.get_food_sprites()
        self.fruit_rect = self.fruit[0].get_rect()
        self.fruit_rect.centerx, self.fruit_rect.centery = 225, 441

        self.fruit_exists = False
        self.fruit_index = 0

        self.initialize_pellets()
        self.initialize_pow_pellets()
        self.initialize_nodes()
        self.initialize_ghost_nodes()
        self.initialize_adj()
        self.initialize_super_nodes()

    def update(self):
        for super_node in self.super_nodes:
             super_node.update(type=None)
        
        for pellet in self.pellets:
            pellet.draw(type='pe')
        
        for pow_pellet in self.pow_pellets:
            pow_pellet.draw(type='pp')
        
        self.spawn_fruit()

        if self.fruit_exists:
            self.draw_fruit()
    
    def spawn_fruit(self):
        if (len(self.pellets) + len(self.pow_pellets)) == 170:
            self.fruit_index = 0
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.pow_pellets)) == 140 and not self.fruit_exists:
            self.fruit_index = 1
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.pow_pellets)) == 110 and not self.fruit_exists:
            self.fruit_index = 2
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.pow_pellets)) == 80 and not self.fruit_exists:
            self.fruit_index = 3
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.pow_pellets)) == 50 and not self.fruit_exists:
            self.fruit_index = 4
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.pow_pellets)) == 20 and not self.fruit_exists:
            self.fruit_index = 5
            self.fruit_exists = True
    
    def draw_fruit(self):
        self.screen.blit(self.fruit[self.fruit_index], self.fruit_rect)
    
    def initialize_nodes(self):
        self.nodes.append(Node(self, x=22, y=24, adj=[1,6]))
        self.nodes.append(Node(self, x=105, y=24, adj=[0, 2, 7]))
        self.nodes.append(Node(self, x=200, y=24, adj=[1, 9]))
        self.nodes.append(Node(self, x=250, y=24, adj=[4, 10]))
        self.nodes.append(Node(self, x=348, y=24, adj=[3, 5, 12]))
        self.nodes.append(Node(self, x=426, y=24, adj=[4, 13],))
        
        self.nodes.append(Node(self, x=22, y=89, adj=[0, 7, 14]))
        self.nodes.append(Node(self, x=105, y=89, adj=[1, 6, 8, 15]))
        self.nodes.append(Node(self, x=153, y=89, adj=[7, 9, 16]))
        self.nodes.append(Node(self, x=200, y=89, adj=[2, 8, 10]))
        self.nodes.append(Node(self, x=250, y=89, adj=[3, 9, 11]))
        self.nodes.append(Node(self, x=298, y=89, adj=[10, 12, 19]))
        self.nodes.append(Node(self, x=348, y=89, adj=[4, 11, 13, 20]))
        self.nodes.append(Node(self, x=426, y=89, adj=[5, 12, 21]))

        self.nodes.append(Node(self, x=22, y=138, adj=[6, 15]))
        self.nodes.append(Node(self, x=105, y=138, adj=[7, 14, 26]))
        self.nodes.append(Node(self, x=153, y=138, adj=[8, 17]))
        self.nodes.append(Node(self, x=200, y=138, adj=[16, 23]))
        self.nodes.append(Node(self, x=250, y=138, adj=[19, 24]))
        self.nodes.append(Node(self, x=298, y=138, adj=[11, 18]))
        self.nodes.append(Node(self, x=348, y=138, adj=[12, 21, 29]))
        self.nodes.append(Node(self, x=426, y=138, adj=[13, 20]))

        self.nodes.append(Node(self, x=153, y=188, adj=[23, 27]))
        self.nodes.append(Node(self, x=200, y=188, adj=[17, 22, 24]))
        self.nodes.append(Node(self, x=250, y=188, adj=[18, 23, 25]))
        self.nodes.append(Node(self, x=298, y=188, adj=[24, 28]))

        self.nodes.append(Node(self, x=105, y=235, adj=[15, 27, 33]))
        self.nodes.append(Node(self, x=153, y=235, adj=[22, 26, 30]))
        self.nodes.append(Node(self, x=298, y=235, adj=[25, 29, 31]))
        self.nodes.append(Node(self, x=348, y=235, adj=[20, 28, 38]))  

        self.nodes.append(Node(self, x=153, y=283, adj=[27, 31, 34]))
        self.nodes.append(Node(self, x=298, y=283, adj=[28, 30, 37]))

        self.nodes.append(Node(self, x=22, y=334, adj=[33, 40]))
        self.nodes.append(Node(self, x=105, y=334, adj=[26, 32, 34, 42]))
        self.nodes.append(Node(self, x=153, y=334, adj=[30, 33, 35]))
        self.nodes.append(Node(self, x=200, y=334, adj=[34, 44]))
        self.nodes.append(Node(self, x=250, y=334, adj=[37, 45]))
        self.nodes.append(Node(self, x=298, y=334, adj=[31, 36, 38]))
        self.nodes.append(Node(self, x=348, y=334, adj=[29, 37, 39, 47]))
        self.nodes.append(Node(self, x=426, y=334, adj=[38, 49]))

        self.nodes.append(Node(self, x=22, y=381, adj=[32, 41]))
        self.nodes.append(Node(self, x=56, y=381, adj=[40, 51]))
        self.nodes.append(Node(self, x=105, y=381, adj=[33, 43, 52]))
        self.nodes.append(Node(self, x=153, y=381, adj=[42, 44, 53]))
        self.nodes.append(Node(self, x=200, y=381, adj=[35, 43, 65]))
        self.nodes.append(Node(self, x=250, y=381, adj=[36, 46, 65]))
        self.nodes.append(Node(self, x=298, y=381, adj=[45, 47, 56]))
        self.nodes.append(Node(self, x=348, y=381, adj=[38, 46, 57]))
        self.nodes.append(Node(self, x=395, y=381, adj=[49, 58]))
        self.nodes.append(Node(self, x=426, y=381, adj=[39, 48]))

        self.nodes.append(Node(self, x=22, y=430, adj=[51, 60]))
        self.nodes.append(Node(self, x=56, y=430, adj=[41, 50, 52]))
        self.nodes.append(Node(self, x=105, y=430, adj=[42, 51]))
        self.nodes.append(Node(self, x=153, y=430, adj=[43, 54]))
        self.nodes.append(Node(self, x=200, y=430, adj=[53, 61]))
        self.nodes.append(Node(self, x=250, y=430, adj=[56, 62]))
        self.nodes.append(Node(self, x=298, y=430, adj=[46, 55]))
        self.nodes.append(Node(self, x=348, y=430, adj=[47, 58]))
        self.nodes.append(Node(self, x=395, y=430, adj=[48, 57, 59]))
        self.nodes.append(Node(self, x=426, y=430, adj=[58, 63]))

        self.nodes.append(Node(self, x=22, y=478, adj=[50, 61]))
        self.nodes.append(Node(self, x=200, y=478, adj=[54, 60, 62]))
        self.nodes.append(Node(self, x=250, y=478, adj=[55, 61, 63]))
        self.nodes.append(Node(self, x=426, y=478, adj=[59, 62]))

        self.nodes.append(Node(self, x=0, y=0, adj=[]))

        self.nodes.append(Node(self, x=225, y=381, adj=[44, 45]))


        self.nodes.append(Node(self, x=200, y=235, adj=[67]))


        self.nodes.append(Node(self, x=225, y=235, adj=[66, 68, 69]))

    
        self.nodes.append(Node(self, x=250, y=235, adj=[67]))


        self.nodes.append(Node(self, x=225, y=188, adj=[23, 24]))

    def initialize_adj(self):
        for node in self.nodes:
            adj_index = 0
            for adj_node_index in node.adj:
                if node.x == self.nodes[adj_node_index].x:
                    weight = abs(self.nodes[adj_node_index].y - node.y)
                    node.adjw.append(weight)
                elif node.y == self.nodes[adj_node_index].y:
                    weight = abs(self.nodes[adj_node_index].x - node.x)
                    node.adjw.append(weight)
                adj_index += 1

    def initialize_super_nodes(self):
        self.super_nodes.append(Node(self, x=225, y=188, adj=[22, 24], adjw=[25, 25]))
    

    def initialize_pellets(self):
        # horizontal  pellets being created                                    
        self.pellets.append(Node(self, x=22, y=24))  

        self.pellets.append(Node(self, x=42, y=24))
        self.pellets.append(Node(self, x=62, y=24))
        self.pellets.append(Node(self, x=82, y=24))

        self.pellets.append(Node(self, x=105, y=24))  

        self.pellets.append(Node(self, x=125, y=24))
        self.pellets.append(Node(self, x=145, y=24))
        self.pellets.append(Node(self, x=165, y=24))
        self.pellets.append(Node(self, x=185, y=24))

        self.pellets.append(Node(self, x=200, y=24))  
        self.pellets.append(Node(self, x=250, y=24))  

        self.pellets.append(Node(self, x=270, y=24))
        self.pellets.append(Node(self, x=290, y=24))
        self.pellets.append(Node(self, x=310, y=24))
        self.pellets.append(Node(self, x=330, y=24))

        self.pellets.append(Node(self, x=348, y=24))  

        self.pellets.append(Node(self, x=368, y=24))
        self.pellets.append(Node(self, x=388, y=24))
        self.pellets.append(Node(self, x=408, y=24))

        self.pellets.append(Node(self, x=426, y=24))  

        self.pellets.append(Node(self, x=22, y=89))  

        self.pellets.append(Node(self, x=42, y=89))
        self.pellets.append(Node(self, x=62, y=89))
        self.pellets.append(Node(self, x=82, y=89))

        self.pellets.append(Node(self, x=105, y=89))  

        self.pellets.append(Node(self, x=125, y=89))

        self.pellets.append(Node(self, x=153, y=89))  

        self.pellets.append(Node(self, x=173, y=89))

        self.pellets.append(Node(self, x=200, y=89))  

        self.pellets.append(Node(self, x=220, y=89))

        self.pellets.append(Node(self, x=250, y=89))  

        self.pellets.append(Node(self, x=270, y=89))

        self.pellets.append(Node(self, x=298, y=89))  

        self.pellets.append(Node(self, x=318, y=89))

        self.pellets.append(Node(self, x=348, y=89))  

        self.pellets.append(Node(self, x=368, y=89))
        self.pellets.append(Node(self, x=388, y=89))
        self.pellets.append(Node(self, x=408, y=89))

        self.pellets.append(Node(self, x=426, y=89))  

        self.pellets.append(Node(self, x=22, y=138))  
        self.pellets.append(Node(self, x=42, y=138))
        self.pellets.append(Node(self, x=62, y=138))
        self.pellets.append(Node(self, x=82, y=138))

        self.pellets.append(Node(self, x=105, y=138)) 
        self.pellets.append(Node(self, x=153, y=138))  

        self.pellets.append(Node(self, x=173, y=138))

        self.pellets.append(Node(self, x=200, y=138))  
        self.pellets.append(Node(self, x=250, y=138))  

        self.pellets.append(Node(self, x=270, y=138))

        self.pellets.append(Node(self, x=298, y=138))  
        self.pellets.append(Node(self, x=348, y=138))  

        self.pellets.append(Node(self, x=368, y=138))
        self.pellets.append(Node(self, x=388, y=138))
        self.pellets.append(Node(self, x=408, y=138))

        self.pellets.append(Node(self, x=426, y=138))  # [21]

        self.pellets.append(Node(self, x=153, y=188))  # [22]

        self.pellets.append(Node(self, x=173, y=188))

        self.pellets.append(Node(self, x=200, y=188))  # [23]

        self.pellets.append(Node(self, x=220, y=188))

        self.pellets.append(Node(self, x=250, y=188))  # [24]

        self.pellets.append(Node(self, x=270, y=188))

        self.pellets.append(Node(self, x=298, y=188))  # [25]

        self.pellets.append(Node(self, x=105, y=235))  # [26]

        self.pellets.append(Node(self, x=125, y=235))

        self.pellets.append(Node(self, x=153, y=235))  # [27]
        self.pellets.append(Node(self, x=298, y=235))  # [28]

        self.pellets.append(Node(self, x=318, y=235))

        self.pellets.append(Node(self, x=348, y=235))  # [29]

        self.pellets.append(Node(self, x=153, y=283))  # [30]

        self.pellets.append(Node(self, x=173, y=283))
        self.pellets.append(Node(self, x=193, y=283))
        self.pellets.append(Node(self, x=213, y=283))
        self.pellets.append(Node(self, x=233, y=283))
        self.pellets.append(Node(self, x=253, y=283))
        self.pellets.append(Node(self, x=273, y=283))

        self.pellets.append(Node(self, x=298, y=283))  # [31]

        self.pellets.append(Node(self, x=22, y=334))  # [32]

        self.pellets.append(Node(self, x=42, y=334))
        self.pellets.append(Node(self, x=62, y=334))
        self.pellets.append(Node(self, x=82, y=334))

        self.pellets.append(Node(self, x=105, y=334))  # [33]

        self.pellets.append(Node(self, x=125, y=334))

        self.pellets.append(Node(self, x=153, y=334))  # [34]

        self.pellets.append(Node(self, x=173, y=334))

        self.pellets.append(Node(self, x=200, y=334))  # [35]
        self.pellets.append(Node(self, x=250, y=334))  # [36]

        self.pellets.append(Node(self, x=270, y=334))

        self.pellets.append(Node(self, x=298, y=334))  # [37]

        self.pellets.append(Node(self, x=318, y=334))

        self.pellets.append(Node(self, x=348, y=334))  # [38]

        self.pellets.append(Node(self, x=368, y=334))
        self.pellets.append(Node(self, x=388, y=334))
        self.pellets.append(Node(self, x=408, y=334))

        self.pellets.append(Node(self, x=426, y=334))  # [39]

        self.pellets.append(Node(self, x=22, y=381))  # [40]
        self.pellets.append(Node(self, x=56, y=381))  # [41]
        self.pellets.append(Node(self, x=105, y=381))  # [42]

        self.pellets.append(Node(self, x=125, y=381))

        self.pellets.append(Node(self, x=153, y=381))  # [43]

        self.pellets.append(Node(self, x=173, y=381))

        self.pellets.append(Node(self, x=200, y=381))  # [44]

        # self.pellets.append(Node(self, x=220, y=381))         # REMOVE -- Pacman starting location

        self.pellets.append(Node(self, x=250, y=381))  # [45]

        self.pellets.append(Node(self, x=270, y=381))

        self.pellets.append(Node(self, x=298, y=381))  # [46]

        self.pellets.append(Node(self, x=318, y=381))

        self.pellets.append(Node(self, x=348, y=381))  # [47]
        self.pellets.append(Node(self, x=395, y=381))  # [48]
        self.pellets.append(Node(self, x=426, y=381))  # [49]

        self.pellets.append(Node(self, x=22, y=430))  # [50]
        self.pellets.append(Node(self, x=56, y=430))  # [51]

        self.pellets.append(Node(self, x=76, y=430))

        self.pellets.append(Node(self, x=105, y=430))  # [52]
        self.pellets.append(Node(self, x=153, y=430))  # [53]

        self.pellets.append(Node(self, x=173, y=430))

        self.pellets.append(Node(self, x=200, y=430))  # [54]
        self.pellets.append(Node(self, x=250, y=430))  # [55]

        self.pellets.append(Node(self, x=270, y=430))

        self.pellets.append(Node(self, x=298, y=430))  # [56]
        self.pellets.append(Node(self, x=348, y=430))  # [57]

        self.pellets.append(Node(self, x=368, y=430))

        self.pellets.append(Node(self, x=395, y=430))  # [58]
        self.pellets.append(Node(self, x=426, y=430))  # [59]

        self.pellets.append(Node(self, x=22, y=478))  # [60]

        self.pellets.append(Node(self, x=42, y=478))
        self.pellets.append(Node(self, x=62, y=478))
        self.pellets.append(Node(self, x=82, y=478))
        self.pellets.append(Node(self, x=102, y=478))
        self.pellets.append(Node(self, x=122, y=478))
        self.pellets.append(Node(self, x=142, y=478))
        self.pellets.append(Node(self, x=162, y=478))
        self.pellets.append(Node(self, x=182, y=478))

        self.pellets.append(Node(self, x=200, y=478))  # [61]

        self.pellets.append(Node(self, x=224, y=478))

        self.pellets.append(Node(self, x=250, y=478))  # [62]

        self.pellets.append(Node(self, x=270, y=478))
        self.pellets.append(Node(self, x=290, y=478))
        self.pellets.append(Node(self, x=310, y=478))
        self.pellets.append(Node(self, x=330, y=478))
        self.pellets.append(Node(self, x=350, y=478))
        self.pellets.append(Node(self, x=370, y=478))
        self.pellets.append(Node(self, x=395, y=478))

        self.pellets.append(Node(self, x=426, y=478))  # [63]

        # vertical pellets
        self.pellets.append(Node(self, x=22, y=109))
        self.pellets.append(Node(self, x=105, y=44))
        self.pellets.append(Node(self, x=105, y=64))
        self.pellets.append(Node(self, x=105, y=109))
        self.pellets.append(Node(self, x=105, y=158))
        self.pellets.append(Node(self, x=105, y=178))
        self.pellets.append(Node(self, x=105, y=198))
        self.pellets.append(Node(self, x=105, y=218))
        self.pellets.append(Node(self, x=105, y=255))
        self.pellets.append(Node(self, x=105, y=275))
        self.pellets.append(Node(self, x=105, y=295))
        self.pellets.append(Node(self, x=105, y=315))
        self.pellets.append(Node(self, x=105, y=354))
        self.pellets.append(Node(self, x=105, y=401))
        self.pellets.append(Node(self, x=200, y=44))
        self.pellets.append(Node(self, x=200, y=64))
        self.pellets.append(Node(self, x=250, y=44))
        self.pellets.append(Node(self, x=250, y=64))
        self.pellets.append(Node(self, x=348, y=44))
        self.pellets.append(Node(self, x=348, y=64))
        self.pellets.append(Node(self, x=348, y=109))
        self.pellets.append(Node(self, x=348, y=158))
        self.pellets.append(Node(self, x=348, y=178))
        self.pellets.append(Node(self, x=348, y=198))
        self.pellets.append(Node(self, x=348, y=218))
        self.pellets.append(Node(self, x=348, y=255))
        self.pellets.append(Node(self, x=348, y=275))
        self.pellets.append(Node(self, x=348, y=295))
        self.pellets.append(Node(self, x=348, y=315))
        self.pellets.append(Node(self, x=348, y=354))
        self.pellets.append(Node(self, x=348, y=401))
        self.pellets.append(Node(self, x=426, y=109))
        self.pellets.append(Node(self, x=153, y=109))
        self.pellets.append(Node(self, x=298, y=109))
        self.pellets.append(Node(self, x=200, y=158))
        self.pellets.append(Node(self, x=250, y=158))
        self.pellets.append(Node(self, x=153, y=208))
        self.pellets.append(Node(self, x=153, y=255))
        self.pellets.append(Node(self, x=153, y=303))
        self.pellets.append(Node(self, x=298, y=208))
        self.pellets.append(Node(self, x=298, y=255))
        self.pellets.append(Node(self, x=298, y=303))
        self.pellets.append(Node(self, x=200, y=354))
        self.pellets.append(Node(self, x=250, y=354))
        self.pellets.append(Node(self, x=56, y=401))
        self.pellets.append(Node(self, x=153, y=401))
        self.pellets.append(Node(self, x=298, y=401))
        self.pellets.append(Node(self, x=395, y=401))
        self.pellets.append(Node(self, x=22, y=450))
        self.pellets.append(Node(self, x=200, y=450))
        self.pellets.append(Node(self, x=250, y=450))
        self.pellets.append(Node(self, x=426, y=450))

    def initialize_pow_pellets(self):
        self.pow_pellets.append(Node(self, x=22, y=54))
        self.pow_pellets.append(Node(self, x=22, y=354))
        self.pow_pellets.append(Node(self, x=426, y=354))
        self.pow_pellets.append(Node(self, x=426, y=54))
    
    def initialize_ghost_nodes(self):
        self.ghost_nodes.append(Node(self, x=198, y=237, adj=[67]))       
        self.ghost_nodes.append(Node(self, x=225, y=237, adj=[66, 68, 69]))   
        self.ghost_nodes.append(Node(self, x=252, y=237, adj=[67]))      
        self.ghost_nodes.append(Node(self, x=225, y=190, adj=[23, 24, 67]))

    def directions(self, start, end):
        found = False

        for adj_index in start.adj:
            if self.nodes.index(end) == adj_index:
                found = True
        
        if found:
            if start.x > end.x and start.y == end.y:
                direction = 'left'
            elif start.x < end.x and start.y == end.y:
                direction = 'right'
            elif start.y < end.y and start.x == end.x:
                direction = 'down'
            elif start.y > end.y and start.x == end.x:
                direction = 'up'
        else:
            return False
        
        return direction

    def valid_move(self, node, direction):
        found = False

        current_node = node

        for adj_node in current_node.adj:
            if direction == 'left' and self.nodes[adj_node].x < current_node.x and self.nodes[adj_node].y == current_node.y\
            or direction == 'right' and self.nodes[adj_node].x > current_node.x and self.nodes[adj_node].y == current_node.y\
            or direction == 'up' and self.nodes[adj_node].y < current_node.y and self.nodes[adj_node].x == current_node.x\
            or direction == 'down' and self.nodes[adj_node].y > current_node.y and self.nodes[adj_node].x == current_node.x:
                current_node = self.nodes[adj_node]
                found = True

        return found


    def adj_path(self, node, direction):
        done = False
        found = False

        current = node
        matching_nodes = []

        while not done:
            for adj_node in current.adj:
                if direction == 'left' and self.nodes[adj_node].x < current.x and self.nodes[adj_node].y == current.y\
                or direction == 'right' and self.nodes[adj_node].x > current.x and self.nodes[adj_node].y == current.y\
                or direction == 'up' and self.nodes[adj_node].y < current.y and self.nodes[adj_node].x == current.x\
                or direction == 'down' and self.nodes[adj_node].y > current.y and self.nodes[adj_node].x == current.x:

                    current = self.nodes[adj_node]
                    matching_nodes.append(current)
                    found = True

            if not found:
                done = True    # Cant go any further
            else:
                found = False  # Reset

        return matching_nodes

    def get_buffer(self, char, direction):
        buffer = 10
        buffers = []

        if direction == 'left':
            buffers.append(char.adj_node.x - buffer)
            buffers.append(char.adj_node.y)
        elif direction == 'right':
            buffers.append(char.adj_node.x + buffer)
            buffers.append(char.adj_node.y)
        elif direction == 'up':
            buffers.append(char.adj_node.x)
            buffers.append(char.adj_node.y - buffer)
        elif direction == 'down':
            buffers.append(char.adj_node.x)
            buffers.append(char.adj_node.y + buffer)

        return buffers

    def init_path_elem(self, node_path_elem):
        org_path_elem = node_path_elem
        distance = 0

        if node_path_elem.node is not node_path_elem.start_node:
            while node_path_elem.nodes is not node_path_elem.start_node:
                i = 0
                found = False

                for prev_node_idx in node_path_elem.previous_path.node.adj:

                    if not found:
                        if node_path_elem.previous_path.node.adj[i] == self.nodes.index(node_path_elem.node):
                            distance += node_path_elem.previous_path.node.adjw[i]
                            found = True
                        else:
                            i += 1
                
                temp_path_elem = node_path_elem
                node_path_elem = node_path_elem.previous_path
        
        org_path_elem.distance_from_start = distance
        org_path_elem.distance_to_goal = self.get_distance(org_path_elem ,org_path_elem.to_node)

        if not self.nodes.index(org_path_elem.node) == self.nodes.index(org_path_elem.to_node):
            org_path_elem.total_distance =  org_path_elem.distance_from_start + org_path_elem.distance_to_goal
        else:
            org_path_elem.total_distance = 0
        return org_path_elem
    
    def get_distance(self, starting_node, to_node):

        return math.sqrt((math.pow(to_node.x - starting_node.x, 2))
                         + (math.pow(to_node.y - starting_node.y, 2)))


    def get_front_of_queue(self, path_elem_open_list):
        if len(path_elem_open_list) <= 0:
            return False

        lowest_distance = 1000
        front_of_queue = path_elem_open_list[0]
        i = 1

        for path_elem in path_elem_open_list:
            if path_elem.total_distance < lowest_distance:
                lowest_distance = path_elem.total_distance
                front_of_queue = path_elem
            i += 1
        return front_of_queue
    
    def weight_from_to(self, start_node, to_node):
        adj_idx = 0
        for adj_node_idx in start_node.adj:
            if adj_node_idx == self.nodes.index(to_node):  

                return start_node.adjw[adj_idx]

            adj_idx += 1
    

    def get_shortest_path(self, starting_node, destination_node):


        starting_path_elem = Path(starting_node, None, starting_node, destination_node)
        starting_path_elem.prev_path_element = starting_path_elem

        open_list = [starting_path_elem]                            # Open list of path element obj's
        open_list[0] = self.init_path_elem(open_list[0])   # Initialize: Set distance_from_source & total_cost

        closed_list = []    

        
        while len(open_list) > 0:

           
            current_path_elem = self.get_front_of_queue(open_list)                             
            
            closed_list.append(current_path_elem)
            open_list.remove(current_path_elem)

            if current_path_elem.node is destination_node:              
                shortest_path = []              
                
                while current_path_elem is not None \
                        and current_path_elem.node is not current_path_elem.source_node:
                    shortest_path.append(current_path_elem)
                    
                    current_path_elem = current_path_elem.prev_path_element

                shortest_path.reverse()     
                return shortest_path        

            
            adj_path_elements = []

            
            for adj_node_idx in current_path_elem.node.adj:

                
                if not adj_node_idx == self.nodes.index(current_path_elem.source_node):
                    path_elem = Path(self.nodes[adj_node_idx], current_path_elem,
                                            starting_node, destination_node)
                    self.init_path_elem(path_elem)
                    adj_path_elements.append(path_elem)
                    
            for path_elem in adj_path_elements:

                in_open_list = False
                in_closed_list = False
                open_list_pos = 0

                
                for cl_elem in closed_list:

                    if self.nodes.index(path_elem.node) == self.nodes.index(cl_elem.node):
                        
                        in_closed_list = True

               
                for ol_elem in open_list:

                    if self.nodes.index(path_elem.node) == self.nodes.index(ol_elem.node):
                        in_open_list = True
                        open_list_pos = open_list.index(ol_elem)       

                if not in_closed_list:


                    if in_open_list:

                        
                        if path_elem.weight_from_source < open_list[open_list_pos].weight_from_source:
                            
                            open_list[open_list.index(open_list[open_list_pos])] = path_elem

                       

                    else:
                        open_list.append(path_elem)
