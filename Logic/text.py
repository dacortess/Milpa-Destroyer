import pygame

pygame.font.init()

class Text():

    def __init__(self):
        self.font = pygame.font.SysFont('comicsans', 20)
    
    def get_wait_message(self, color):
        return self.font.render("Waiting for another player", 1, color)
    
    def get_winner_message(self, winner, color):
        return self.font.render("The winner is player " + winner, 1, color)

class Score(Text):
    def __init__(self):
        Text.__init__(self)
        self.score = 0
    
    def get_score(self, color):
        return self.font.render("SCORE: " + str(self.score), 1, color)
    
    def set_score(self, temp_score):
        self.score = temp_score
        