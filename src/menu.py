import pygame
from pygame.locals import *
from button import create_button, show_text_button
from levels import level

class MainMenu:
    def __init__(self, screen, font, background, button_play_rect, button_controls_rect, button_exit_rect, color_primary=(0, 0, 0), color_secondary=(0, 0, 0)):
        self.screen = screen
        self.font = font
        self.background = background
        self.button_play_rect = button_play_rect
        self.button_controls_rect = button_controls_rect
        self.button_exit_rect = button_exit_rect
        self.color_primary = color_primary
        self.color_secondary = color_secondary
        self.show_controls = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        cursor = event.pos
                        if self.button_play_rect.collidepoint(cursor[0], cursor[1]):
                            self.levels_menu()
                        elif self.button_controls_rect.collidepoint(cursor[0], cursor[1]):
                            self.show_controls = not self.show_controls
                        elif self.button_exit_rect.collidepoint(cursor[0], cursor[1]):
                            pygame.quit()
                            
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.show_controls = False

            self.draw()

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        if not self.show_controls:
            create_button(self.screen, self.button_play_rect, "Levels", self.color_primary, self.color_secondary)
            create_button(self.screen, self.button_controls_rect, "Controls", self.color_primary, self.color_secondary)
            create_button(self.screen, self.button_exit_rect, "Quit", self.color_primary, self.color_secondary)
        else:
            controls_image = pygame.transform.scale(pygame.image.load("./src/assets/controles.jpg"), (self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(controls_image, (0, 0))
            create_button(self.screen, self.button_exit_rect, "Volver", self.color_primary, self.color_secondary)

        pygame.display.flip()

    def levels_menu(self):
        # Aquí deberías poner la lógica para pasar al menú de niveles (si lo tienes implementado)
        # Por ahora, solo imprimirá un mensaje.
        print("Entrando al menú de niveles")
        pygame.time.delay(1000)  # Simula una pequeña demora antes de pasar al menú de niveles


