# Imports

# Base
import sys, os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# Installed
import pygame

# Util modules
import colors

# Game modules
import classes

# Prototypes
import prototypes


# Constants

FRAMES_PER_SECOND = 60


# Functions

def endRuntime():
    pygame.quit()
    sys.exit()


# Setup

# Pygame
pygame.init()
screen = pygame.display.set_mode((0, 0))
screenSize = screen.get_rect()
screenRatio = screenSize.w/screenSize.h
pygame.display.set_caption(os.path.basename(__file__))
clock = pygame.time.Clock()

# Map
map = classes.Surface()

# Robot
# map.createEntity()


# Main loop

while pygame.time.get_ticks() < 3000: #True:
    # Draw

    #screen.fill(colors.BLACK)
    #screen.blit(map.render(
    #    10,
    #    10*screenRatio
    #))
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
