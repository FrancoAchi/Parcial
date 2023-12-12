import pygame
from pygame.locals import *
from config import *
from button import create_button, show_text_button
from levels import Level
from import_path import load_path


class MainMenu:
    def __init__(self, screen, font, background, button_play_rect, button_controls_rect, button_exit_rect, button_level1, button_level2, button_level3, color_primary=(0, 0, 0), color_secondary=(0, 0, 0), border_color= (0, 0 , 0), music_file= None):
        self.screen = screen
        self.font = font
        self.background = background
        self.button_play_rect = button_play_rect
        self.button_controls_rect = button_controls_rect
        self.button_exit_rect = button_exit_rect
        self.button_level1 = button_level1
        self.button_level2 = button_level2
        self.button_level3 = button_level3
        self.color_primary = color_primary
        self.color_secondary = color_secondary
        self.border_color = border_color
        self.show_controls = False
        self.music_file = music_file
        self.levels_menu_active = False
        self.in_level = False
        self.level_1 = level1
        self.level_2 = level2
        self.level_3 = level3


    def setup_music(self):
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.set_volume(0.8) 
            pygame.mixer.music.play(-1)
        

    def run(self):
        pygame.mixer.init()
        self.setup_music()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        cursor = event.pos
                        if self.button_play_rect.collidepoint(cursor[0], cursor[1]):
                            self.levels_menu_active = True

                        elif self.button_controls_rect.collidepoint(cursor[0], cursor[1]):
                            self.show_controls = not self.show_controls

                        elif self.button_exit_rect.collidepoint(cursor[0], cursor[1]):
                            pygame.quit()

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        if self.levels_menu_active:
                            self.levels_menu_active = False
                            self.in_level = False
                        else:
                            self.show_controls = False

            if self.levels_menu_active:
                selected_level = self.levels_menu()
                if selected_level is not None:
                    return self.setup_level(selected_level, self.screen)
        
            self.draw()
            pygame.display.flip()
            pygame.time.delay(100)

        pygame.mixer.music.stop()
        pygame.display.flip()
        pygame.mixer.quit()
        


    def draw(self):
        self.screen.blit(self.background, (0, 0))

        if not self.show_controls:
            if not self.levels_menu_active:
                create_button(self.screen, self.button_play_rect, "Levels", self.color_primary, self.color_secondary, self.border_color)
                create_button(self.screen, self.button_controls_rect, "Controls", self.color_primary, self.color_secondary, self.border_color)
                create_button(self.screen, self.button_exit_rect, "Quit", self.color_primary, self.color_secondary, self.border_color)
            else:
                self.draw_levels_menu()

        else:
            controls_image = pygame.transform.scale(load_path("controles.jpg"), (self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(controls_image, (0, 0))

        pygame.display.flip()

    def levels_menu(self):
        level_menu = True
        self.selected_level = None

        while level_menu:
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                elif e.type == MOUSEBUTTONDOWN:
                    if e.button == 1:
                        mouse = e.pos
                        if self.button_level1.collidepoint(mouse[0], mouse[1]):
                            self.selected_level = level1
                            level_menu = False
                        elif self.button_level2.collidepoint(mouse[0], mouse[1]):
                            self.selected_level = level2
                            level_menu = False
                        elif self.button_level3.collidepoint(mouse[0], mouse[1]):
                            self.selected_level = level3
                            level_menu = False
                elif e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        level_menu = False
                        self.levels_menu_active = False

            if not self.in_level:
                self.draw_levels_menu()

            pygame.display.flip()
            pygame.time.delay(100)

        return self.selected_level

        



    def draw_levels_menu(self):
        create_button(self.screen, self.button_level1, "Level 1", self.color_primary, self.color_secondary, self.border_color)
        create_button(self.screen, self.button_level2, "Level 2", self.color_primary, self.color_secondary, self.border_color)
        create_button(self.screen, self.button_level3, "Level 3", self.color_primary, self.color_secondary, self.border_color)


    def setup_level(self, level, screen):
        self.level = Level(level, screen)