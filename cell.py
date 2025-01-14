import pygame 
from globals import to_screen_coords
class Cell: 
    def __init__(self, pos, is_alive, length):
        self.pos = pos 
        self.is_alive = is_alive 
        self.length = length
        screen_coord = to_screen_coords(pos)
        self.rect = pygame.Rect(screen_coord[0], screen_coord[1], length, length)
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.rect)

