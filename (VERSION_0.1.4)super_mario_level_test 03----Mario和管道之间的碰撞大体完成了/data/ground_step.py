__author__ = 'justinarmstrong'

import pygame
from pygame.sprite import Sprite
import settings as st

class Ground(Sprite):
    """Invisible sprites placed overtop background parts
    that can be collided with (pipes, steps, ground, etc."""
    def __init__(self, x, y, width, height, name='collider'):
        Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(st.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None

