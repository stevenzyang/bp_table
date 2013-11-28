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

# Serialization for each arduino
player1 = serial.Serial('/dev/tty.usbmodem1411', 9600)

# Screen Setup
screen = pygame.display.set_mode((800,600), 0, 32)
image_surf = pygame.image.load("thetatau.bmp").convert()
screen.blit(image_surf,(0, 0))
pygame.display.flip()

class BPTable:
    def __init__(self):
        self._running = True
        self.size = self.weight, self.height = 800, 600

    def on_init(self):
        pygame.init()
        self._running = True
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
class Cups:
    c_pos1 = [(20, 230),(20, 275), (20, 318), (20, 361), (65, 255), 
        (65, 298), (65, 340), (110, 273), (110, 317), (150, 294)]
    c_pos2 = [(780, 230),(780, 275), (780, 318), (780, 361), (735, 255), 
        (735, 298), (735, 340), (690, 273), (690, 317), (650, 294)]
    c_r = 20
    c_color = (0, 0, 0)

    def setup_cups(self):
        pygame.draw.circle(screen, self.c_color, self.c_pos1[0], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos1[1], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos1[2], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos1[3], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos1[4], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos1[5], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos1[6], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos1[7], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos1[8], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos1[9], self.c_r)

        pygame.draw.circle(screen, self.c_color, self.c_pos2[0], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos2[1], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos2[2], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos2[3], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos2[4], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos2[5], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos2[6], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos2[7], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos2[8], self.c_r)
        pygame.draw.circle(screen, self.c_color, self.c_pos2[9], self.c_r)

        pygame.display.update()


if __name__ == "__main__":
    bp = BPTable()
    cup_setup = Cups()
    cup_setup.setup_cups()
    bp.on_execute()
    while 1:
        curr_player1 = player1.readline()
        print(curr_player1)
        # "1\r\n" is the output from serialization of arduino; we can control what
        # outputs come from arduino, therefore controlling whether or not something
        # is on or off
        if curr_player1 == "1\r\n":
            pos = Cups.c_pos1[0]
            c_color = (255, 0, 0)
            pygame.draw.circle(screen, c_color, pos, 20)
        elif curr_player1 == "2\r\n":
            pos = Cups.c_pos1[0]
            c_color = (0, 0, 0)
            pygame.draw.circle(screen, c_color, pos, 20)
        # You need this loop here in order for pygame to run properly
        for event in pygame.event.get():
            bp.on_event(event)
        pygame.display.update()
