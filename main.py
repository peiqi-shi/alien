import pygame
from prepare.alien_first import AlienStart

if __name__ == '__main__':
    hai = AlienStart()
    hai.explain()
    pygame.mouse.set_visible(False)
    while True:
        
        hai.check()
        hai.check_key()
        hai.update()
        