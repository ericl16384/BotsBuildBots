# Imports

# Base
import sys, os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# Installed
import pygame

# My modules
import data


# Constants

FRAMES_PER_SECOND = 60


# Functions

def endRuntime():
    pygame.quit()
    sys.exit()


# Setup

pygame.init()
screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption(os.path.basename(__file__))
clock = pygame.time.Clock()


# Main loop

while pygame.time.get_ticks() < 3000:
    # Draw

    pygame.display.flip()


    # Wait for the next tick

    clock.tick(FRAMES_PER_SECOND)
        

    # Read input

    # Quit when exit button is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endRuntime()
    

    # Logic

    pass
