import pygame

pygame.font.init()

class Score():

    def __init__(self):
        self.font = pygame.font.SysFont('comicsans', 20)
        self.score = 0
    
    def get_score(self, color):
        return self.font.render("SCORE: " + str(self.score), 1, color)
        