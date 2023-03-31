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
            super_node.update(kind=None)
        
        for pellet in self.pellets:
            pellet.draw(kind='pe')
        
        for pow_pellet in self.pow_pellets:
            pow_pellet.draw(kinf='pp')
        
        self.spawn_fruit()

        if self.fruit_exists:
            self.draw_fruit()
    
    def spawn_fruit(self):
        if (len(self.pellets) + len(self.power_pellets)) == 170:
            self.fruit_index = 0
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.power_pellets)) == 140 and not self.fruit_exists:
            self.fruit_index = 1
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.power_pellets)) == 110 and not self.fruit_exists:
            self.fruit_index = 2
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.power_pellets)) == 80 and not self.fruit_exists:
            self.fruit_index = 3
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.power_pellets)) == 50 and not self.fruit_exists:
            self.fruit_index = 4
            self.fruit_exists = True
        elif (len(self.pellets) + len(self.power_pellets)) == 20 and not self.fruit_exists:
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