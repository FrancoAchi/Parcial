from typing import Any
import pygame
from pygame.locals import *
from config import *
from sprite_sheet import *



class Player(pygame.sprite.Sprite):

    def __init__(self, groups, position) -> None:
        super().__init__(groups)
        self.sheet = pygame.image.load('skeletor.png')
        self.sheet.set_clip(pygame.Rect(0,0, 64, 53))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame

    def draw(self):
        ...
   

    def update(self):

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
                # current_time =  pygame.time.get_ticks()
                # if current_time - self.ultima_actualizacion >= self.animation_time:
                #     self.current_sprite += 1
                #     self.image = self.animations[1][self.current_sprite]
                #     if self.current_sprite == 3:
                #         self.current_sprite = 0
                #     self.ultima_actualizacion = current_time
        if keys[K_LEFT]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
                # current_time =  pygame.time.get_ticks()
                # if current_time - self.ultima_actualizacion >= self.animation_time:
                #     self.current_sprite += 1
                #     self.image = self.animations[2][self.current_sprite]
                #     if self.current_sprite == 3:
                #         self.current_sprite = 0
                #     self.ultima_actualizacion = current_time
        # if keys[K_SPACE]:
        #     if self.rect.top >= 0:
        #         if self.jump != 0:
        #             self.rect.y += self.speed_y
        #             self.speed_y += 1

        #             if self.rect.bottom >= HEIGHT - 10:
        #                 self.rect.bottom  = HEIGHT - 10
        #                 self.jumping = False
        #                 self.jump = 0
    

        
