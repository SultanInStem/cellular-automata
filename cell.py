import pygame 
from config import CELL_COLOR
class Cell: 
    def __init__(self, pos, is_alive, size):
        self.pos = pos 
        self.is_alive = is_alive 
        self.size = size
    def draw(self, screen):
        if self.is_alive: 
            pygame.draw.rect(screen, CELL_COLOR, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
