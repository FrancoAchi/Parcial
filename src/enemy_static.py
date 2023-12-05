import pygame
from sprite_sheet import Sprites
from import_path import load_path
from projectiles import Projectile
from config import STATIC_WIDTH, STATIC_HEIGHT

class StaticEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, is_facing_left=False, speed=2, all_sprites_group=None):
        super().__init__()
        # Configuración del sprite y la máscara
        self.animations = self.load_enemy_animations()
        self.current_sprite = 0
        self.direction = -1 if is_facing_left else 1
        self.image = self.animations["walk_left" if is_facing_left else "walk_right"][self.current_sprite]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites_group = all_sprites_group

        # Configuración de disparo
        self.shoot_timer = 0
        self.shoot_interval = 5000  # Intervalo en milisegundos (5 segundos)

    def load_enemy_animations(self):
        sprite_enemy = Sprites(load_path("enemy2.png"), 4, 2, STATIC_WIDTH, STATIC_HEIGHT, ["walk_right", "walk_left", "death_left", "death_right"])
        return sprite_enemy.get_animation_dict()

    def update(self):
        # Actualizar la animación del sprite
        animation_key = "walk_left" if self.direction == -1 else "walk_right"
        self.current_sprite = (self.current_sprite + 1) % len(self.animations[animation_key])
        self.image = self.animations[animation_key][self.current_sprite]
        self.mask = pygame.mask.from_surface(self.image)

        # Actualizar temporizador de disparo
        self.shoot_timer += pygame.time.get_ticks()

        # Disparar un proyectil cada 5 segundos
        if self.shoot_timer >= self.shoot_interval:
            self.shoot()
            self.shoot_timer = 0

    def shoot(self):
        projectile = Projectile(self.rect.centerx, self.rect.centery, self.direction)
        # Añadir el proyectil al grupo de sprites
       
        self.all_sprites_group.add(projectile)

