import pygame
from sprite_sheet import Sprites
from config import WIDTH_ENEMY, HEIGHT_ENEMY
from import_path import load_path

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, move_speed, move_range):
        super().__init__()
        # Configuración del sprite y la máscara
        self.animations = self.load_enemy_animations()
        self.current_sprite = 0
        self.image = self.animations["walk_left"][self.current_sprite]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.move_speed = move_speed
        self.move_range = move_range
        self.direction = 1  

    def load_enemy_animations(self):
        sprite_enemy = Sprites(load_path("enemy1.png").convert_alpha(), 5, 4, WIDTH_ENEMY, HEIGHT_ENEMY, ["walk_left", "walk_right", "hit_left", "hit_right", "death_right", "death_left"])
        return sprite_enemy.get_animation_dict()

    def update(self):
        
        animation_key = "walk_right" if self.direction == 1 else "walk_left"
        self.current_sprite = (self.current_sprite + 1) % len(self.animations[animation_key])
        self.image = self.animations[animation_key][self.current_sprite]
        self.mask = pygame.mask.from_surface(self.image)

        
        self.rect.x += self.direction * self.move_speed

        
        if self.rect.right >= self.move_range[1] or self.rect.left <= self.move_range[0]:
            self.direction *= -1
