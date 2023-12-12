import pygame
from levels import Level
from tiles import Platform
from sprite_sheet import Sprites
from player import Player
from config import HEIGHT, WIDTH, WIDTH_PLAYER, HEIGHT_PLAYER
from import_path import load_path
from boss import Boss
import random

class SkyProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y, fall_speed):
        super().__init__()
        self.image = pygame.Surface((10, 10))  # Ajusta el tamaño según sea necesario
        self.image.fill((255, 0, 0))  # Relleno de color rojo (puedes cambiarlo)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.fall_speed = fall_speed
        self.initial_y = y  # Almacena la posición y inicial

    def update(self):
        self.rect.y += self.fall_speed

        # Si el proyectil del cielo llega a la parte inferior, reinicia su posición
        if self.rect.top > HEIGHT:
            self.rect.y = self.initial_y
            self.rect.x = random.randint(0, WIDTH - self.rect.width)

class LevelBoss(Level):
    def __init__(self, level_data, surface):
        super().__init__(level_data, surface)

        self.boss_health = 20

    def setup_level(self, level_data):
           # Configuración del fondo del nivel
        self.background_image = pygame.image.load(level_data['background']).convert()
        self.background_rect = self.background_image.get_rect()

        # Configuración de las plataformas
        self.platforms = pygame.sprite.Group()
        for platform_info in level_data['platforms']:
            x, y, width, height = platform_info
            platform = Platform(x, y, width, height)
            self.platforms.add(platform)

        # Configuración del jugador
        self.all_sprites = pygame.sprite.Group()
        sprite_player = Sprites(load_path("skeletor.png"), 8, 4, WIDTH_PLAYER, HEIGHT_PLAYER, ["idle_right", "idle_left", "right", "left", "attack_right", "attack_left", "death_right", "death_left"])
        self.player = Player([self.all_sprites], sprite_player)
        

        boss_data = level_data.get('boss', None)
        if boss_data:
            boss_x, boss_y = boss_data
            self.boss = Boss(boss_x, boss_y,)
            self.all_sprites.add(self.boss)

        
        self.sky_projectiles = pygame.sprite.Group()  # Grupo para proyectiles del cielo

        # Generar proyectiles del cielo
        for _ in range(10):  # Ajusta la cantidad de proyectiles según sea necesario
            x = random.randint(0, WIDTH)
            y = random.randint(-200, -50)
            fall_speed = random.randint(3, 5)  # Ajusta la velocidad según sea necesario
            sky_projectile = SkyProjectile(x, y, fall_speed)
            self.sky_projectiles.add(sky_projectile)
            self.all_sprites.add(sky_projectile)


    def handle_enemy_projectile_collisions(self):

        boss_collisions = pygame.sprite.spritecollide(self.boss, self.player.projectiles, True)
        for _ in boss_collisions:
            
            self.boss_health -= 1
            if self.boss_health <= 0:
                
                self.boss.kill()


    def run(self):
        self.player.update()
        self.horizontal_movement_collision()
        self.bottom_top_collision()
        self.sky_projectiles.update()
        self.boss.update()
        
        
        self.player.update()
        self.player.projectiles.update()

        # Dibujar el fondo
        self.platforms.draw(self.display_surface)
        self.display_surface.blit(self.background_image, (0, 0))

        # Dibujar las plataformas y el jugador
        self.player.projectiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.all_sprites.draw(self.display_surface)
        self.handle_enemy_projectile_collisions()

        
