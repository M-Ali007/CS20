# Mustafa Ali
# Battleship - Assignment 2
# Block 5
# 24th May

# This program is my own work - MA

# Consider any possible problems or limitations pertaining to this program.
# What are they? Make the necessary modifications.
#
# A problem that I came across was #TODO

import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    pygame.display.update()
    clock.tick(240)
    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")