import os, sys
import pygame
from pygame.locals import *
import serial
import time
from sys import exit
from random import *

__author__ = {'name' : '[Theta Tau] Lambda Class',
              'mail' : 'jy.johnlee@gmail.com',
              'Version' : '1.0'}

# Serialization goes here, find out comport using ls /dev/tty* command
player1 = serial.Serial('/dev/tty.usbmodem1411', 9600)
# player2 = serial.Serial()


pygame.init()

# Screen properties
SCREEN_DEFAULT_SIZE = (500, 500)
SCREEN_DEFAULT_COLOR = (0, 0 ,0)

# Set Screen
screen = pygame.display.set_mode(SCREEN_DEFAULT_SIZE, 0, 32)
screen.fill(SCREEN_DEFAULT_COLOR)

# Red
c_color = (255, 0, 0)

# Positions of cups
c1_pos = (180, 400)
c2_pos = (220, 400)
c3_pos = (260, 400)
c4_pos = (300, 400)
c5_pos = (200, 360)
c6_pos = (240, 360)
c7_pos = (280, 360)
c8_pos = (220, 320)
c9_pos = (260, 320)
c10_pos = (240, 280)

# Radius of cups
c_r = 20

# How to draw cups
pygame.draw.circle(screen, c_color, c1_pos, c_r)
pygame.draw.circle(screen, c_color, c2_pos, c_r)
pygame.draw.circle(screen, c_color, c3_pos, c_r)
pygame.draw.circle(screen, c_color, c4_pos, c_r)
pygame.draw.circle(screen, c_color, c5_pos, c_r)
pygame.draw.circle(screen, c_color, c6_pos, c_r)
pygame.draw.circle(screen, c_color, c7_pos, c_r)
pygame.draw.circle(screen, c_color, c8_pos, c_r)
pygame.draw.circle(screen, c_color, c9_pos, c_r)
pygame.draw.circle(screen, c_color, c10_pos, c_r)

# Display the 10 cups
pygame.display.update()

# Begin game loop
while 1:
    curr_player1 = player1.readline()
    print(curr_player1)
    # "1\r\n" is the output from serialization of arduino; we can control what
    # outputs come from arduino, therefore controlling whether or not something
    # is on or off
    if curr_player1 == "1\r\n":
        c_color = (0, 0, 255)
        pygame.draw.circle(screen, c_color, c1_pos, c_r)
    elif curr_player1 == "2\r\n":
        c_color = (255, 0, 0)
        pygame.draw.circle(screen, c_color, c1_pos, c_r)
    # You need this loop here in order for pygame to run properly
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update()
