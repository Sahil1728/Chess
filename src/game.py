import pygame
from const import *

class Game:
    def __init__(self):
        pass

    # Show methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col)%2 == 0:
                    # White
                    color = (255, 255, 255)
                else:
                    # Black
                    color = (0, 0, 0)
                
                # Drawing the square
                rect = (row*SQ_SIZE, col*SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)
        pass