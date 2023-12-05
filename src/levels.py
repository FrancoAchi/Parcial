import pygame
from pygame.locals import *
from player import Player
from tiles import Platform 
from sprite_sheet import Sprites
from config import WIDTH_PLAYER, HEIGHT_PLAYER
from enemy import Enemy
from import_path import load_path
from enemy_static import StaticEnemy

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

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

        #Configuración de los enemigos
        self.enemies = pygame.sprite.Group()
        for enemy_info in level_data.get('enemies', []):
            x, y, move_speed, move_range = enemy_info
            enemy = Enemy(x, y, move_speed, move_range)
            self.enemies.add(enemy)

        self.static_enemies = pygame.sprite.Group()
        for static_enemy_info in level_data.get('static_enemies', []):
            x, y, is_facing_left, speed = static_enemy_info
            static_enemy = StaticEnemy(x, y, is_facing_left, speed, all_sprites_group=self.all_sprites)
            self.static_enemies.add(static_enemy)
        
        
        
        


    def horizontal_movement_collision(self):
       
        collisions = pygame.sprite.spritecollide(self.player, self.platforms, False)
        for platform in collisions:
            
            if self.player.rect.bottom >= platform.rect.top and self.player.speed_v > 0:
                self.player.rect.bottom = platform.rect.top
                self.player.speed_v = 0

    def bottom_top_collision(self):
        collisions = pygame.sprite.spritecollide(self.player, self.platforms, False)
        
        for platform in collisions:
            if self.player.rect.bottom >= platform.rect.top and self.player.speed_v > 0:
                self.player.rect.bottom = platform.rect.top
                self.player.is_jumping = False
                if self.player.is_jumping:
                    pass
                else:
                    self.player.speed_v = 0

    
    def handle_enemy_projectile_collisions(self):
    # Verificar colisiones de proyectiles del jugador con enemigos
        for enemy in self.enemies:
            collisions = pygame.sprite.spritecollide(enemy, self.player.projectiles, True)
            for _ in collisions:
                # Aquí puedes agregar lógica adicional, como decrementar la vida del enemigo
                enemy.kill()

        static_enemy_collisions = pygame.sprite.spritecollide(self.player, self.static_enemies, True)
        for static_enemy in static_enemy_collisions:
            # Aquí puedes agregar lógica adicional, como decrementar la vida del enemigo
            static_enemy.kill()
            

    def run(self):
        self.player.update()
        self.horizontal_movement_collision()
        self.bottom_top_collision()
        self.enemies.update()
        self.static_enemies.update()
        
        
        self.player.update()
        self.player.projectiles.update()

        # Dibujar el fondo
        self.display_surface.blit(self.background_image, (0, 0))
        self.platforms.draw(self.display_surface)

        # Dibujar las plataformas y el jugador
        self.player.projectiles.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.static_enemies.draw(self.display_surface)

        self.all_sprites.draw(self.display_surface)
        self.handle_enemy_projectile_collisions()
        
