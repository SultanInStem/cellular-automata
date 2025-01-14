import pygame 


class Canvas: 
    def __init__(self, size): 
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Cellular Automata")
        