#射击模块
import pygame
class Bullet:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #在（0，0）的位置创建子弹
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width, self.sttings.bullet_height)
        self.bullet_rect.midtop = ai_game.Ship(self).midtop
        
        self.y = float(self.bullet_rect.y)
    def updat(self):
        self.y -=self.settings.bullet_spped
        self.bullet_rect.y

    def draw_bullet( self ):
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)