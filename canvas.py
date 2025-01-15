import pygame 
import sys 
from cell import Cell
from config import ROWS, COLS, SCREEN_SIZE
class Canvas: 
    def __init__(self, size): 
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Cellular Automata")
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.running = True
        self.grid = []
        cell_height = ROWS // SCREEN_SIZE[1]
        cell_width = COLS // SCREEN_SIZE[0]
        cell_size = (cell_height, cell_width)
        for row in range(0, ROWS): 
            temp_row = []
            for col in range(0, COLS):
                pos = (row * cell_width, col * cell_height)
                temp_row.append(Cell((), False, cell_size))
            self.grid.append(temp_row)    



    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False

    def update(self): 
        pass 

    def render(self): 
        self.screen.fill((0,0,0))

        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()

