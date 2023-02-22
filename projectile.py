import pygame
from config import *


class Projectile(pygame.sprite.Sprite):
    def __init__(self, path, player_speed, player_x, player_y):
        super().__init__()
        self.image = pygame.image.load(path)
        self.speed_x = speed_x_balls * player_speed[0]
        self.speed_y = speed_y_balls * player_speed[1]
        self.current_x = player_x
        self.current_y = player_y
        self.rect = self.image.get_rect()
        self.rect.center = (self.current_x, self.current_y)

    def get_image(self):
        return self.image

    def get_speed_x(self):
        return self.speed_x

    def get_speed_y(self):
        return self.speed_y

    def get_current_x(self):
        return self.current_x

    def get_current_y(self):
        return self.current_y

    def get_rect(self):
        return self.rect

    def get_rect_center(self):
        return self.rect.center

    def set_image(self, image):
        self.image = image

    def set_speed_x(self, speed_x):
        self.speed_x = speed_x

    def set_speed_y(self, speed_y):
        self.speed_y = speed_y

    def set_current_x(self, x):
        self.current_x = x

    def set_current_y(self, y):
        self.current_y = y

    def set_rect(self, rect):
        self.rect = rect

    def set_rect_center(self, center):
        self.rect.center = center

    def move(self):
        self.current_x += self.speed_x
        self.current_y += self.speed_y
        self.set_rect_center((self.current_x, self.current_y))
