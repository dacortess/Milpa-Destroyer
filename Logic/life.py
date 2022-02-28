import pygame, os


class Life():
    
    def __init__(self):
        self.width = 25
        self.height = 25
        self.image = None
        self.life_p1 = 3
        self.life_p2 = 3
        self.winner = 0
    
    def set_image(self, src, ang):
        self.image = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(
                        os.path.join('.\src\images', src)), (self.width, self.height)), ang)
    



