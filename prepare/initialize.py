import pygame
class Initialize:
    def __init__(self):
        
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.length = self.screen.get_rect().width
        self.hight = self.screen.get_rect().height

        pygame.display.set_caption('Alien game')
        #绘制背景色，深蓝色
        self.color = (0, 0, 100)