#中心程序
import sys, pygame
from .ship import Ship
from .shoot import Bullet
class Alien( Ship ):
    def __init__( self ):
        pygame.init()
        Ship.__init__(self)
        

    def check_key( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #去右边
                    self.right = True
                elif event.key == pygame.K_LEFT:
                    self.left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.type == pygame.K_SPACE:
                    self.__fire__bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.right = False
                elif event.key == pygame.K_LEFT:
                    self.left = False

    def check( self ):
        self.screen.fill(self.color)
        self.screen.blit(self.picture, self.rect)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def explain( self ):
        pass
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    def run_game(self):
        while True:
            self.check()
            self.check_key()
            self.update()
            self.bullets.update()

