import pygame 
import sys 
from config import ROWS, COLS
class Canvas: 
    def __init__(self, size): 
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Cellular Automata")
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.running = True
        self.grid = []
        for row in range(0, ROWS): 
            for col in range(0, COLS): 
                pass



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

