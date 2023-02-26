import pygame
import sys


class Chest(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, state):
        super().__init__()
        self.is_animating = False

        self.chest = []

        self.add_animations(state)
        self.current_sprites = 0

        self.animation_speed = 0.1
        self.back_or_forth = 'forth'

        self.image = self.chest[self.current_sprites]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def add_animations(self, opening):
        if opening:
            for chest in range(1, 6):
                self.chest.append(pygame.image.load("assets/chest/chest_openning/chest_openning{}.png".format(chest)))
        else:
            for chest in range(1, 13):
                self.chest.append(pygame.image.load("assets/chest/chest_static/chest_openning{}.png".format(chest)))

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprites += self.animation_speed

            if self.current_sprites >= len(self.chest):
                self.current_sprites = 0
                self.is_animating = False

            self.image = self.chest[int(self.current_sprites)]