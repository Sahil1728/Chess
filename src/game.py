import pygame
from const import *



# Responsible for all the rendering methods for now

class Game:

    def __init__(self):
        pass

    # SHOW METHODS

    def show_background(self, screen):
        
        # drawing the chess board
        for row in range(NROWS):
            for col in range(NCOLS):
                # if the sum of row and col is even, then it is a black square
                if(row + col) % 2 == 0:
                    color = (0, 0, 0)
                # if the sum of row and col is odd, then it is a white square
                else:
                    color = (255, 255, 255)

