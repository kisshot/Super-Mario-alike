import pygame
from enemies import Enemy
from settings import Settings

class Koopa(Enemy):
    """乌龟"""

    def __init__(self):
        ai_settings = Settings()
        screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
        Enemy.__init__(self, ai_settings, screen)
        self.kill()
