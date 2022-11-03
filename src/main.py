# importing the libraries
import pygame
import sys

from const import *
from game import Game

class Main:
    def __init__(self):
        # Initializing the pygame model
        pygame.init()
        # creating the screen attribute
        self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        # setting the caption
        pygame.display.set_caption("CHESS")
        # creating the game object
        self.game = Game()

    def mainloop(self):

        # Creating variables for easier access
        game = self.game
        screen = self.screen
        
        while True:

            game.show_bg(screen)
            # looping through the events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Updating the screen
            pygame.display.update()

main = Main()
main.mainloop()