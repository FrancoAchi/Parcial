import pygame
from pygame.locals import * 
from config import WIDTH, HEIGHT, FPS, button_height, button_width, SIZE_SCREEN, level1, level3, level2, GREY, PURPLE, BLACK
from import_path import load_path
from menu_levels import MainMenu
from levels import Level
from setup_level_boss import LevelBoss

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.icon =  pygame.display.set_icon(load_path("logo.png"))
        self.background = pygame.transform.scale(load_path("menu.jpg"), (SIZE_SCREEN))
        self.font = pygame.font.Font(None, 36)
        self.center_x = self.screen.get_width() // 2
        self.play_button = pygame.Rect(10, 545, 200, 50)
        self.controls_button = pygame.Rect(300, 545, 200, 50)
        self.exit_button = pygame.Rect(590, 545, 200, 50)
        self.button_level1 = pygame.Rect(self.center_x - button_width // 2, 150, button_width, button_height)
        self.button_level2 = pygame.Rect(self.center_x - button_width // 2, 250, button_width, button_height)
        self.button_level3 = pygame.Rect(self.center_x - button_width // 2, 350, button_width, button_height)
        self.level = level2
        self.setup_level(self.level, self.screen)


        self.menu = MainMenu(self.screen, self.font, self.background, self.play_button, self.controls_button, self.exit_button, self.button_level1, self.button_level2,  self.button_level3, GREY, PURPLE, BLACK)

    def setup_level(self, level, screen):
        self.level = Level(level, screen)
       
    
    def run(self):

        while True:
            self.menu.run()
            running = True
            

            while running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False

            
                if level1:
                    self.level.run()
                elif level3:
                    self.level.run()
                    
            
            

        

                pygame.display.flip()
                self.clock.tick(FPS)

            pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()