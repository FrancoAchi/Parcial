import pygame
from sprite_sheet import Sprites
from config import BOSS_WIDTH, BOSS_HEIGHT
from import_path import load_path

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = self.load_boss_animations()
        self.current_sprite = 0
        self.image = self.animations["idle"][self.current_sprite]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.idle_counter = 0 
        self.idle_duration = 20 

    def load_boss_animations(self):
        sprite_boss = Sprites(load_path("boss.png"), 1, 6, BOSS_WIDTH, BOSS_HEIGHT, ["idle"])
        return sprite_boss.get_animation_dict(3)

    def update(self):
        # Lógica de animación "idle"
        self.idle_counter += 1

        # Cambiar sprite "idle" cada cierto tiempo
        if self.idle_counter >= self.idle_duration:
            self.current_sprite = (self.current_sprite + 1) % len(self.animations["idle"])
            self.image = self.animations["idle"][self.current_sprite]
            self.mask = pygame.mask.from_surface(self.image)
            self.idle_counter = 0
