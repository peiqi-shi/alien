import pygame
class Ship:
    def __init__(self, ai_name):
        self.screen = ai_name.screen
        self.screen_rect = ai_name.screen.get_rect()
        self.image = pygame.image.load('C:\\Users\\steven\\workspace\\alien\\picture\\飞船.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    def bltime( self ):
        