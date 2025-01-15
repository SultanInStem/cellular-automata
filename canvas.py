import pygame 
import sys 
import random
from cell import Cell
from config import BG_COLOR, ROWS, COLS, SCREEN_SIZE
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Cellular Automata")
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.running = True
        self.is_paused = False
        self.grid = []
        cell_height = SCREEN_SIZE[1] // ROWS
        cell_width = SCREEN_SIZE[0] // COLS
        cell_size = (cell_height, cell_width)
        for r in range(0, ROWS): 
            temp_row = []
            for c in range(0, COLS):
                pos = (r * cell_width, c * cell_height)
                temp_row.append(Cell(pos, False, cell_size))
            self.grid.append(temp_row)    
        


    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False

    def update(self): 
        if self.is_pause: pass



    def render(self): 
        self.screen.fill(BG_COLOR)

        for row in range(0, ROWS): 
            for col in range(0, COLS):
                self.grid[row][col].draw(self.screen)

        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()

