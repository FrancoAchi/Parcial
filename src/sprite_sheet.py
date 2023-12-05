import pygame
from pygame.locals import *
from config import	*

class Sprites:
    def __init__(self, image, rows, columns, width, height, keys = None) -> None:
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rows = rows
        self.columns = columns
        self.width_player = width
        self.height_player = height
        self.keys = keys
    
    def get_animation_dict(self, scale = 1):
        self.width =  scale * self.width
        self.height =  scale * self.height
        self.width_player = scale * self.width_player
        self.height_player = scale * self.height_player
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        column_counter = 0
        animation_dir = {}
        for row in range(self.rows):
            animation_row =[]
            for _ in range(self.columns):
                animation_row.append(self.image.subsurface((column_counter * self.width_player, row * self.height_player, self.width_player, self.height_player)))
                column_counter += 1
            animation_dir[self.keys[row]] = animation_row
            column_counter = 0
        return animation_dir 
        