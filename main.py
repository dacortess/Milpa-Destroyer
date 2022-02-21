#Python libs
import pygame
#Pygame Window settings
from Config.window import Window
from Config.colors import Colors
#Players Logic
from Logic.player import Player
from Logic.bullets import Bullets
from Logic.score import Score
#Socket class
from Client.client_socket import Client

#SOCKET
CLIENT = Client()

#GAME

#Create & start Window
WIN = Window()
WIN.start()

#Create players
PLAYER_1 = Player()
PLAYER_1.set_image('spaceship_1.png', 0)
PLAYER_2 = Player()
PLAYER_2.set_image('spaceship_2.png', 0)

#Create Bullets
BULLETS = Bullets()

#Create Score
P1_SCORE = Score()
P2_SCORE = Score()

#Create color selecter
COLORS = Colors()

# Draw all objects in the screen
def draw_window(player,player_2):

    #Blit Background
    WIN.blit(WIN.background, (0, 0))

    #Blit Score
    P1_SCORE_TEXT   = P1_SCORE.get_score(COLORS.white)
    P1_SCORE_X      = WIN.width - P1_SCORE_TEXT.get_width()
    P1_SCORE_Y      = 0

    P2_SCORE_TEXT   = P2_SCORE.get_score(COLORS.black)
    P2_SCORE_X      = WIN.width - P2_SCORE_TEXT.get_width()
    P2_SCORE_Y      = WIN.height - P2_SCORE_TEXT.get_height()

    WIN.blit(P1_SCORE_TEXT, (P1_SCORE_X, P1_SCORE_Y))
    WIN.blit(P2_SCORE_TEXT, (P2_SCORE_X, P2_SCORE_Y))

    #Blit Players
    WIN.blit(PLAYER_1.image, (player.x, player.y))
    WIN.blit(PLAYER_2.image,  (player_2.x, player_2.y))

    #Draw Bullets
    for bullet in BULLETS.p1_bullets:
        pygame.draw.rect(WIN.window, COLORS.cian, bullet)

    for bullet in BULLETS.p2_bullets:
        pygame.draw.rect(WIN.window, COLORS.red, bullet)

    pygame.display.update()

#Pygame main loop and game specific config
def main():

    player_1    = pygame.Rect(173, 500, PLAYER_1.width, PLAYER_1.height)
    player_2    = pygame.Rect(173, 100-PLAYER_2.height, PLAYER_2.width, PLAYER_2.height)
    
    clock = pygame.time.Clock()
    run = True
    while run:

        BULLETS.bullets_rec = 0

        clock.tick(WIN.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            BULLETS.bullets_detect(event, player_1)
            BULLETS.bullet_colision(event, P1_SCORE, P2_SCORE)

        PLAYER_1.key_mapping(player_1)

        player_2.x, player_2.y, BULLETS.bullets_rec = CLIENT.get_data(player_1, BULLETS.bullets_rec)

        BULLETS.bullets_recive(player_2)

        BULLETS.bullets_handler(player_1, player_2)

        draw_window(player_1, player_2)

    pygame.quit()

if __name__ == "__main__":
    main()