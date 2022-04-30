import pygame
import sys
import os
import math
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
screenwidth, screenheight = (500, 280)
screen = pygame.display.set_mode((screenwidth, screenheight))
bg = pygame.image.load("BlueGameBackgroundRepeatingV3.png")
bgX = 0
bgX2 = bg.get_width()
pygame.mouse.set_visible(0)
pygame.display.set_caption('Let\'s Fly!')

def redrawWindow():
    screen.blit(bg, (bgX, 0))  # draws our first bg image
    screen.blit(bg, (bgX2, 0))  # draws the seconf bg image
    pygame.display.update()  # updates the screen

run = True
speed = 30
while run:
    redrawWindow()
    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1:  # If our bg is at the -width then reset its position
        bgX = bg.get_width()
    
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
    
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    clock.tick(speed)




    