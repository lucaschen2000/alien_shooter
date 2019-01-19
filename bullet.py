import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Manage bullets fired from ship """

    def __init__(self, ai_settings, screen, ship):
        """ Create bullet at ship """
        super().__init__()
        self.screen = screen

        # Create bullet rect at (0,0) and change position to ship's rect
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store position as float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Move bullet up screen """
        # Move bullet
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw bullet on screen """
        pygame.draw.rect(self.screen, self.color, self.rect)

    