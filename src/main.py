# importing the libraries
import pygame
import sys

from const import *

class Main:
    def __init__(self):
        # Initializing the pygame model
        pygame.init()
        # creating the screen attribute
        self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        # setting the caption
        pygame.display.set_caption("CHESS")

    def mainloop(self):
        
        while True:
            # looping through the events
            for event in pygame.events.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Updating the screen
            pygame.display.update()

main = Main()
main.mainloop()