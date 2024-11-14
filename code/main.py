from settings import * 

class Game: 
    def __init__(self):
        pygame.init()
        self.display_surfface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 

