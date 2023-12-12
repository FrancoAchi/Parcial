

level1 = {
            'background': "./src/assets/nivel1.png",
            'platforms': [
                (95, 357, 200, 10),
                (450, 427, 200, 10),
                (0, 513, 800, 10),
                (530, 254, 290, 10),
                (400, 170, 20, 10),
                (220, 155, 20, 10),
                (29, 112, 60, 10),
            ],
            'enemies': [
                (100, 475, 2, (100, 800)),
                (90, 320, 2, (90, 300))
            ],
            'static_enemies': [
                (759, 210, True, 2),
                (631, 385, True, 2),
            ],
            'items': [(336, 475, './src/assets/apple.png', 30, 30),
                      (640, 215, './src/assets/apple.png', 30, 30),
                      (200, 320, './src/assets/apple.png', 30, 30)],
            'healing_items': [(60, 70, './src/assets/heart.png', 30, 30)],
            'spikes': [(0, 490, './src/assets/spikes.png', 60, 19),
                       (560, 228,'./src/assets/spikes.png', 60, 19)]
         
        
        }

level2 = {

            'background': "./src/assets/level2.png",
            'platforms': [
                (130, 410, 540, 10),
                (190, 310, 420, 10),
                (0, 513, 800, 10),
                (250, 202, 300, 10),
                (2, 200, 60, 10),
                (727, 200, 60, 10),
                (310, 100, 170, 10)
            ],
            'enemies': [
                (157, 371, 2, (100, 690)),
                (241, 270, 2, (160, 630)),
                (300, 62, 2, (300, 495))
            ],
            'static_enemies': [
                (765, 155, True, 1),
                (5, 155, False, 1),
            ],
            'items': [(336, 475, './src/assets/apple.png', 30, 30),
                      (232, 273, './src/assets/apple.png', 30, 30),
                      (432, 165, './src/assets/apple.png', 30, 30)],
            'healing_items': [(385, 65, './src/assets/heart.png', 30, 30)],
            'spikes': [(0, 490, './src/assets/spikes.png', 60, 19),
                       (350, 175,'./src/assets/spikes.png', 60, 19)]
        }



level3 = {
            'background': "./src/assets/level3.png",
            'platforms': [
                (110, 375, 320, 10),
                (110, 240, 320, 10),
                (0, 513, 800, 10)  
            ],
            'boss': (200, 110)}

FPS = 60

WIDTH_PLAYER = 60
HEIGHT_PLAYER = 64
WIDTH_ENEMY = 42
HEIGHT_ENEMY = 30
STATIC_WIDTH = 32
STATIC_HEIGHT = 32

WIDTH_PROJECTILE = 14
HEIGHT_PROJECTILE = 18
SPEED_PROJECTILE = 3

ORIGIN = (0,0)

WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (143, 143, 143)
PURPLE = (128, 119, 168)
BLACK = (0, 0 ,0)

GRAVITY = 0.5

EXPLOSION_WIDTH = 130
EXPLOSION_HEIGHT = 130




button_width = 250
button_height = 40


SIZE_SCREEN = (WIDTH, HEIGHT)

BOSS_WIDTH = 48
BOSS_HEIGHT = 42

TILE_SIZE = 20