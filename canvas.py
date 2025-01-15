import pygame 
import sys 
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
        self.is_paused = True
        self.grid = []
        self.cell_width = SCREEN_SIZE[0] // COLS
        self.cell_height = SCREEN_SIZE[1] // ROWS
        cell_size = (self.cell_height, self.cell_width)
        for r in range(0, ROWS): 
            temp_row = []
            for c in range(0, COLS):
                pos = (c * self.cell_width, r * self.cell_height)
                temp_row.append(Cell(pos, False, cell_size))
            self.grid.append(temp_row)    
        


    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.is_paused: 
                ### if the game is paused, resurrect a cell at the mouse position
                mouse_pos = pygame.mouse.get_pos()
                ### modulate the positions to get array index of the cell 
                row_index = (mouse_pos[1] // self.cell_height) % ROWS
                col_index = (mouse_pos[0] // self.cell_width) % COLS
                self.grid[row_index][col_index].resurrect()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]: 
                self.is_paused = not self.is_paused
            elif keys[pygame.K_r]:
                ### Reset the game
                self.is_paused = True 
                for i in range(0, len(self.grid)): 
                    for j in range(0, len(self.grid[i])): 
                        self.grid[i][j].die() 

    def update(self): 
        if self.is_paused:
            pass


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

