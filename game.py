#Создай собственный Шутер!

from pygame import *
from random import randint
clock = time.Clock()
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
back = (200, 255, 255)
window.fill(back)
display.set_caption("Maze")
game = True
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  size_x, size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
'''class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global proshli
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            self.speed = randint(1,7)
            proshli += 1'''
racket1 = Player('racket.png', 30, 200, 50, 150, 4) 
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
while game:
    window.fill(back)
    racket1.update_l()
    racket2.update_r()

    for e in event.get():
        if e.type == QUIT:
            game = False
    racket1.reset()
    racket2.reset()

    display.update()
    clock.tick(60)