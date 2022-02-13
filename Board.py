import pygame 
pygame.init()

class Board : 

    BLACK = (0, 0, 0)

    def __init__(self):
        
        #Game Window
        size = (700, 500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Snake") 
        screen.fill(self.BLACK)
