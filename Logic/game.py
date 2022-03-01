#Python libs
import pygame
#Pygame Window settings
from Config.window import Window
from Config.colors import Colors
#Players Logic
from Logic.player import Player
from Logic.bullets import Bullets
from Logic.text import Text
from Logic.text import Score
from Logic.life import Life
#Socket class
from Client.client_socket import Client

class Game():

    def __init__(self):
        self.client = Client()
        self.window = Window()
        self.player_1 = Player()
        self.player_2 = Player()
        self.bullets = Bullets()
        self.life = Life()
        self.score_p1 = Score()
        self.score_p2 = Score()
        self.message = Text()
        self.colors = Colors()
        self.track_p1 = pygame.Rect(173, 500, self.player_1.width, self.player_1.height)
        self.track_p2 = pygame.Rect(173, 100, self.player_2.width, self.player_2.height)
        self.clock = pygame.time.Clock()
        self.is_runnig = True
    
    def start_game(self):
        self.window.start()
        self.player_1.set_image('spaceship_1.png', 0)
        self.player_2.set_image('spaceship_2.png', 0)
        self.life.set_image('life.png', 0)
        self.main()

    def draw_play_again(self):

        #Blit Background
        self.window.blit(self.window.background, (0, 0))

        WIN_TEXT = self.message.get_winner_message(str(self.life.winner), self.colors.white)
        WIN_TEXT_X = self.window.width//2 - WIN_TEXT.get_width()//2
        WIN_TEXT_Y = self.window.height//2 - WIN_TEXT.get_height()//2
        self.window.blit(WIN_TEXT, (WIN_TEXT_X, WIN_TEXT_Y))

        pygame.display.update()

    # Draw all objects in the screen
    def draw_window(self, track_p1,track_p2):

        #Blit Background
        self.window.blit(self.window.background, (0, 0))

        #Blit waiting message
        if track_p2.x == 173 and track_p2.y == -360:
            WAIT_TEXT = self.message.get_wait_message(self.colors.white)
            WAIT_TEXT_X = self.window.width//2 - WAIT_TEXT.get_width()//2
            WAIT_TEXT_Y = self.window.height//2 - WAIT_TEXT.get_height()//2
            self.window.blit(WAIT_TEXT, (WAIT_TEXT_X, WAIT_TEXT_Y))

        #Blit Score
        P1_SCORE_TEXT   = self.score_p1.get_score(self.colors.white)
        P1_SCORE_X      = self.window.width - P1_SCORE_TEXT.get_width()
        P1_SCORE_Y      = 0

        P2_SCORE_TEXT   = self.score_p2.get_score(self.colors.black)
        P2_SCORE_X      = self.window.width - P2_SCORE_TEXT.get_width()
        P2_SCORE_Y      = self.window.height - P2_SCORE_TEXT.get_height()

        #Blit Lifes
        for i in range(self.life.life_p1):
            self.window.blit(self.life.image, (5 + (i * (self.life.width + 5) ), 5))
        for i in range(self.life.life_p2):
            self.window.blit(self.life.image, (5 + (i * (self.life.width + 5) ), self.window.height - self.life.height - 5))

        #Blit Scores
        self.window.blit(P1_SCORE_TEXT, (P1_SCORE_X, P1_SCORE_Y))
        self.window.blit(P2_SCORE_TEXT, (P2_SCORE_X, P2_SCORE_Y))

        #Blit Players
        self.window.blit(self.player_1.image, (track_p1.x, track_p1.y))
        self.window.blit(self.player_2.image,  (track_p2.x, track_p2.y))

        #Draw Bullets
        for bullet in self.bullets.p1_bullets:
            pygame.draw.rect(self.window.window, self.colors.cian, bullet)

        for bullet in self.bullets.p2_bullets:
            pygame.draw.rect(self.window.window, self.colors.red, bullet)

        pygame.display.update()

    #Pygame main loop and game specific config
    def main(self):
        
        while self.is_runnig:

            temp_score =  0
            self.bullets.bullets_rec = 0

            self.clock.tick(self.window.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_runnig = False

                self.bullets.bullets_detect(event, self.track_p1)
                self.bullets.bullet_colision(event, self.score_p1, self.score_p2, self.life)

            self.player_1.key_mapping(self.track_p1)

            self.track_p2.x, self.track_p2.y, self.bullets.bullets_rec, self.score_p2.score, self.life.life_p2 = self.client.get_data(self.track_p1, self.bullets.bullets_rec, self.score_p1, self.life)

            self.bullets.bullets_recive(self.track_p2)

            self.bullets.bullets_handler(self.track_p1, self.track_p2)

            self.draw_window(self.track_p1, self.track_p2)
            if self.life.winner != 0: self.is_runnig = False
    
    def Winner(self):

        self.is_runnig = True

        while self.is_runnig:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_runnig = False

            self.draw_play_again()

        pygame.quit()