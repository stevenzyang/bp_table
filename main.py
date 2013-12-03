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
player1 = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
player2 = serial.Serial('/dev/ttyACM1', 9600, timeout=5)

# Screen Setup
screen = pygame.display.set_mode((800,600), 0, 32)
image_surf = pygame.image.load("thetatau.bmp").convert()
screen.blit(image_surf,(0, 0))
pygame.display.flip()

#Game variables
p1_score = 0
p2_score = 0

class BPTable:
    def __init__(self):
        self._running = True
        self.size = self.weight, self.height = 800, 600

    def on_init(self):
        pygame.init()
	'''pygame.display.toggle_fullscreen()'''
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
        for i in range (0, 10):
            pygame.draw.circle(screen, self.c_color, self.c_pos1[i], self.c_r)
        for i in range (0, 10):
            pygame.draw.circle(screen, self.c_color, self.c_pos2[i], self.c_r)
        pygame.display.update()

def setup_scoreboard():
    pygame.font.init()
    score_font = pygame.font.Font(None, 50)
    player1 = score_font.render("Team Tongs: " , 1, (255, 255, 255))
    screen.blit(player1, (10, 70))
    player2 = score_font.render("Team Hammerd: ", 1, (255, 255, 255))
    screen.blit(player2, (470, 70))

def score_player1(score):
    s = pygame.Surface((80,40))
    screen.blit(s, (224, 60))
    score_font = pygame.font.Font(None, 50)
    current = score_font.render(str(score), 1, (255, 255, 255))
    screen.blit(current, (240, 70))

def score_player2(score):
    s = pygame.Surface((80,40))
    screen.blit(s, (765, 60))
    score_font = pygame.font.Font(None, 50)
    current = score_font.render(str(score), 1, (255, 255, 255))
    screen.blit(current, (755, 70))

def player1_take_turn():
    global p1_score
    curr_player1 = player1.readline()
    print(curr_player1)
    # i +"\r\n" is the output from serialization of arduino; we can control what
    # outputs come from arduino, therefore controlling whether or not something
    # is on or off
    for i in range(1, 21):
        check = str(i) + "\r\n"
        if curr_player1 == check:
            if i % 2 != 0:
                player1_draw_cup((i-1)/2, True)
                p1_score += 1
            else:
                player1_draw_cup((i-1)/2, False)

def player1_draw_cup(position, lit):
    if lit:
        pygame.draw.circle(screen, (230, 175, 6),Cups.c_pos1[position], 20)
    else:
        pygame.draw.circle(screen, (0, 0, 0),Cups.c_pos1[position], 20)

def player2_take_turn():
    global p2_score
    curr_player2 = player2.readline()
    print(curr_player2)
    # i +"\r\n" is the output from serialization of arduino; we can control what
    # outputs come from arduino, therefore controlling whether or not something
    # is on or off
    for i in range(1, 21):
        check = str(i) + "\r\n"
        if curr_player2 == check:
            if i % 2 != 0:
                player2_draw_cup((i-1)/2, True)
                p2_score += 1
            else:
                player2_draw_cup((i-1)/2, False)

def player2_draw_cup(position, lit):
    if lit:
        pygame.draw.circle(screen, (181, 6, 6),Cups.c_pos2[position], 20)
    else:
        pygame.draw.circle(screen, (0, 0, 0),Cups.c_pos2[position], 20)

def start_game():
    global p1_score
    global p2_score
    time.sleep(2)
    while 1:
        p1_score = 0
        p2_score = 0
        for i in range(0, 10):
            player1_take_turn()
            player2_take_turn()
        score_player1(p1_score)
	score_player2(p2_score)
        # You need this loop here in order for pygame to run properly
        for event in pygame.event.get():
            bp.on_event(event)
        pygame.display.update()
        player1.flushInput()
        player2.flushInput()
        time.sleep(.5)

if __name__ == "__main__":
    bp = BPTable()
    cup_setup = Cups()
    cup_setup.setup_cups()
    setup_scoreboard()
    bp.on_execute()
    start_game()
