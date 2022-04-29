import pygame

import sys

import os

from pygame.locals import *

class ScrollingBackground:

    def __init__(self, screenwidth, imagefile):

        self.img = pygame.image.load(imagefile)

        self.coord = [0, 0]

        self.coord2 = [-screenwidth, 0]

        self.x_original = self.coord[0]

        self.x2_original = self.coord2[0]

    def Show(self, surface):

        surface.blit(self.img, self.coord)

        surface.blit(self.img, self.coord2)

    def UpdateCoords(self, speed_x, time):

        distance_x = speed_x * time

        self.coord[0] += distance_x

        self.coord2[0] += distance_x

        if self.coord2[0] >= 0:

            self.coord[0] = self.x_original

            self.coord2[0] = self.x2_original




pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screenwidth, screenheight = (500, 280)

screen = pygame.display.set_mode((screenwidth, screenheight))



# Set the framerate

framerate = 60



# Set the background scrolling speed

bg_speed = 100



# Load the background image here. Make sure the file exists!

Sky = ScrollingBackground(screenheight, "BlueGameBackground.png")

pygame.mouse.set_visible(0)

pygame.display.set_caption('Let\'s Fly!')



# fix indentation

while True:

    time = clock.tick(framerate)/1000.0

    x, y = pygame.mouse.get_pos()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()



    # Set new Background Coordinates and update the screen

    Sky.UpdateCoords(bg_speed, time)

    Sky.Show(screen)

    pygame.display.update()



    