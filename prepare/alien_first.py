#中心程序
import sys, pygame
from .initialize import Initialize
from .ship import Ship
class AlienStart( Ship ):
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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.right = False
                elif event.key == pygame.K_LEFT:
                    self.left = False

    def check( self ):
        self.screen.fill(self.color)
        self.screen.blit(self.picture, self.rect)
        
        pygame.display.flip()

    def explain( self ):
        pass



