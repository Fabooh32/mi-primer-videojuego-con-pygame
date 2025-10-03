import pygame

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

python microjuego_ritmo.py


import os
os.environ["SDL_VIDEO_CENTERED"] = "1"  # Ventana centrada
import sys
import math
import random
import pygame

# ------------------------------------------------------------
# Parámetros principales
# ------------------------------------------------------------
WIDTH, HEIGHT = 900, 700
FPS = 60
DURATION = 30.0  # Duración mínima de 30s
TITLE = "Ritmo Rectangular - Z / V / M"

# Área de juego (3 carriles) centrada
LANES = 3
LANE_WIDTH = 120
LANE_GAP = 24
PLAYFIELD_WIDTH = LANES * LANE_WIDTH + (LANES - 1) * LANE_GAP
LEFT_MARGIN = (WIDTH - PLAYFIELD_WIDTH) // 2

# Línea de acierto y notas
HIT_Y = int(HEIGHT * 0.82)         # línea donde se acierta
