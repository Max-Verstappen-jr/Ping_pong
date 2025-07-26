from pygame import *


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Yooo")
background = transform.scale(image.load("Verstappen.jpg"), (win_width, win_height))

class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


finish = False
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

ball = GameSprite("Ball.png", 100, 200, 50,50,5)
P1 = Player("P1.png",-30,200,120,140,1)
P2 = Player("P2.png",600,200,120,140,1)
            
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("Player 1 lose", True,(180,0,0))
lose2 = font1.render("Player 2 lose", True,(180,0,0))


speed_x = 1
speed_y = 1

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background,(0, 0))

        ball.rect.y += speed_y
        ball.rect.x += speed_x

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(P1, ball) or sprite.collide_rect(P2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (350, 250))

        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (350, 250))


        P1.update_l()
        P1.reset()
        ball.reset()

        P2.update_r()
        P2.reset()

    display.update()