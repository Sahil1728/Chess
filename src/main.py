# importing the required moudules
import pygame
import sys
# importing the const.py file
from const import *


# MAIN CLASS
class Main:
    def __init__(self):
        # Initialising the pygame screen
        pygame.init()
        # Screen attributes
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Title of the screen
        pygame.display.set_caption("Chess")
        print("Hi! Hope this works.")
    
    # Method for calling all classes (AKA The GAME RUNNER)
    def mainloop(self):

        while True:
            # Looping through all the events
            for event in pygame.event.get():
                # If the event is quit, then quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            # Updating the screen with the new changes
            pygame.display.update()

# instance of main class
main = Main()
# call mainloop method
main.mainloop()
