import pygame 
from config import CELL_COLOR
class Cell: 
    def __init__(self, pos, is_alive, size):
        self.pos = pos 
        self.is_alive = is_alive 
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], self.size[0], self.size[1])
    def draw(self, screen):
        pygame.draw.rect(screen, CELL_COLOR, self.rect)

