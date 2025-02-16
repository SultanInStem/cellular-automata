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
        self.fps = 60
        self.GEN_FPS = 2 
        self.action_interval = self.fps // self.GEN_FPS
        self.frame_counter = 0
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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]: 
                self.is_paused = not self.is_paused
            elif keys[pygame.K_r]:
                ### Reset the game
                self.is_paused = True 
                for i in range(0, len(self.grid)): 
                    for j in range(0, len(self.grid[i])): 
                        self.grid[i][j].die() 
            if event.type == pygame.QUIT: 
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.is_paused == True: 
                ### if the game is paused, resurrect a cell at the mouse position
                mouse_pos = pygame.mouse.get_pos()
                ### modulate the positions to get array index of the cell 
                row_index = (mouse_pos[1] // self.cell_height) % ROWS
                col_index = (mouse_pos[0] // self.cell_width) % COLS
                self.grid[row_index][col_index].resurrect()


    def update(self): 
        if self.is_paused: return
        if self.frame_counter >= self.action_interval: 
            self.frame_counter = 0
            for r in range(0, ROWS):
                for c in range(0, COLS): 
                    neighbors = []
                    if r - 1 >= 0: neighbors.append(self.grid[r - 1][c])
                    if r + 1 < ROWS: neighbors.append(self.grid[r + 1][c])
                    if c - 1 >= 0: neighbors.append(self.grid[r][c - 1])
                    if c + 1 < COLS: neighbors.append(self.grid[r][c + 1])
                    if r - 1 >= 0 and c - 1 >= 0: neighbors.append(self.grid[r - 1][c - 1])
                    if r - 1 >= 0 and c + 1 < COLS: neighbors.append(self.grid[r - 1][c + 1])
                    if r + 1 < ROWS and c - 1 >= 0: neighbors.append(self.grid[r + 1][c - 1])
                    if r + 1 < ROWS and c + 1 < COLS: neighbors.append(self.grid[r + 1][c + 1])
                    alive = 0
                    for n in neighbors:
                        if n.is_alive: alive += 1
                    if alive < 2: self.grid[r][c].die()
                    elif alive > 3: self.grid[r][c].die()
                    elif alive == 3: self.grid[r][c].resurrect()
                



    def render(self): 
        self.screen.fill(BG_COLOR)
        self.frame_counter += 1
        
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

