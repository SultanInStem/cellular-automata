import pygame 

class Cell: 
    def __init__(self, pos, is_alive, length):
        self.pos = pos 
        self.is_alive = is_alive 
        self.length = length
        self.rect = pygame.Rect()
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.rect)

