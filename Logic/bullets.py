import pygame

pygame.mixer.init()

class Bullets():

    def __init__(self):
        self.velocity = 7
        self.max = 3
        self.p1_hit = pygame.USEREVENT + 1
        self.p2_hit = pygame.USEREVENT + 2
        self.p1_bullets = []
        self.p2_bullets = []
        self.bullets_rec = 0
        self.hit_sound = pygame.mixer.Sound('.\src\sounds\hit.mp3')
        self.fire_sound = pygame.mixer.Sound('.\src\sounds\\fire.mp3')
    
    def bullets_recive(self, player_2):

        if self.bullets_rec > 0 and len(self.p2_bullets) < self.max:
            bullet = pygame.Rect(player_2.x + player_2.width//2 - 2, player_2.y + player_2.height-11, 5, 10)
            self.p2_bullets.append(bullet)
            self.fire_sound.play()

    def bullets_detect(self, event, player):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LCTRL and len(self.p1_bullets) < self.max:
                bullet = pygame.Rect(player.x + player.width//2 - 2, player.y, 5, 10)
                self.p1_bullets.append(bullet)
                self.bullets_rec += 1
                self.fire_sound.play()

    def bullets_handler(self, player, player_2):

        for bullet in self.p1_bullets:
            bullet.y -= self.velocity

            if player_2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.p2_hit))
                self.p1_bullets.remove(bullet)

            if bullet.y < 10:
                self.p1_bullets.remove(bullet)
            
        for bullet in self.p2_bullets:
            bullet.y += self.velocity

            if player.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.p1_hit))
                self.p2_bullets.remove(bullet)

            if bullet.y > 600:
                self.p2_bullets.remove(bullet)

    def bullet_colision(self, event, P1_SCORE, P2_SCORE, LIFE):

        flag = False

        if event.type == self.p1_hit:
            P1_SCORE.score += 1
            self.hit_sound.play()

        if event.type == self.p2_hit:
            flag = True
            self.hit_sound.play()
        
        if P2_SCORE.score%5 == 0 and P2_SCORE.score != 0 and flag:
            LIFE.life_p1 -= 1

        if LIFE.life_p2 == 0:
            LIFE.winner = 2
        if LIFE.life_p1 == 0:
            LIFE.winner = 1
