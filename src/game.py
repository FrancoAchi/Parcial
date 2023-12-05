import pygame
from pygame.locals import *
from levels import Level   
from config import WIDTH, HEIGHT, FPS, level2, level1, level3
from import_path import load_path
# from menu import MainMenu



class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.icon =  pygame.display.set_icon(load_path("logo.png"))
        self.level_data = level3
        self.setup_level()
    
    def setup_level(self):
        self.level = Level(self.level_data, self.screen)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.level.run()
            

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
    
    


if __name__ == "__main__":
    game = Game()
    game.run()
