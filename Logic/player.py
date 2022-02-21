import pygame
import os

class Player():

    def __init__(self):
        self.width = 60
        self.height = 60
        self.velocity = 5
        self.image = None
        self.middle_point = 200
        self.max_mc = 150
        self.left_margin = self.middle_point - self.max_mc
        self.rigth_margin = self.middle_point + self.max_mc - self.width

    def set_image(self, src, ang):
        self.image = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(
                        os.path.join('.\src\images', src)), (self.width, self.height)), ang)

    def key_mapping(self, player):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_LEFT] and player.x > self.left_margin:
            player.x -= self.velocity
        if key_pressed[pygame.K_RIGHT]and player.x < self.rigth_margin:
            player.x += self.velocity


