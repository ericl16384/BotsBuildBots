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
    print("Game window deinitialized.")
    sys.exit()


# Setup

# Map
map = classes.Surface()

# Robot
# map.createEntity()
robotPos = [0, 0]





## Temporary

#map.generateChunk((0, 0))

#import json

#for chunk in map.getGeneratedChunks().values():
#    with open("dump.txt", "w") as f:
#        print(json.dumps(chunk, indent=4), file=f)










#endRuntime()


# Start Pygame

pygame.init()

# https://www.pygame.org/docs/ref/display.html
screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Bots Build Bots") #os.path.basename(__file__))
#pygame.display.set_icon(icon)

print("Game window initialized.")

screenSize = screen.get_rect()
clock = pygame.time.Clock()


# Main loop

while pygame.time.get_ticks() < 10000: #True:
    # Draw

    screen.fill(colors.BLACK)
    #screen.blit(map.render(robotPos, 20, screenSize))
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
