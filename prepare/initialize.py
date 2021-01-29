import pygame
from prepare.shoot import Bullet
class Initialize( Bullet ):
    def __init__(self):
        self.bullets = pygame.sprite.Group()
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.length = self.screen.get_rect().width
        self.hight = self.screen.get_rect().height
        self.speed = 2.0
        pygame.display.set_caption('Alien game')
        #绘制背景色，深蓝色
        self.color = (0, 0, 100)