import pygame
class Ship:
    def __init__( self, ai_game ):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('C:\\Users\\steven\\workspace\\alien\\picture\\飞船.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.ship_speed = 2
        self.moving_right = False
        self.moving_left = False
    def update( self ):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.ship_speed
        self.rect.x = float(self.rect.x)
    def blitme( self ):
        self.screen.blit(self.image,self.rect)