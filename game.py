#Создай собственный Шутер!

from pygame import *
from random import randint
import time as time1
clock = time.Clock()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
while True:
    a = randint(0,255)
    b = randint(0,255)
    c = randint(0, 255)
    time1.sleep(1)
back = (a, b, c)
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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global proshli
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            self.speed = randint(1,7)
            proshli += 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)