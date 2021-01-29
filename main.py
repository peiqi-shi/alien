import pygame
from prepare.alien import Alien

if __name__ == '__main__':
    hai = Alien()
    hai.explain()
    pygame.mouse.set_visible(False)
    hai.run_game()