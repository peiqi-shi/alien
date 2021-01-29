from prepare.initialize import Initialize
import pygame

class Ship(Initialize):

    def __init__(self):
        Initialize.__init__(self)
        #获取位置
        #self.screen = place.screen
        #self.screen_rect = place.screen.get_rect()
        self.right = False
        self.left = False
        self.screen_rect = self.screen.get_rect()
        #加载图像 获取外接矩形
        self.picture = pygame.image.load('C:\\Users\\steven\\workspace\\alien\\picture\\飞船.png')
        self.rect = self.picture.get_rect()
        #生成位置
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme_ship(self):
        #指定飞船位置
        self.screen.blit(self.image, self.rect)
    
    def update( self ):
        if self.right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.left and self.rect.left > 0:
            self.rect.x -= 1