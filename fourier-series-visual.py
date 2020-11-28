# very basic visualisation of sine wave addition
# using connected rotating circles, currently just
# draws a square wave using 3 circles

import math
import time

import pygame
import pygame.gfxdraw

class Circle(object):
    def __init__(self, radius, period, phase):
        self.radius = radius
        self.period = period
        self.phase = phase

pygame.init()

WIDTH = 600
HEIGHT = 600

TWO_PI = math.pi*2

display = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

running = True

circles = [
    Circle(150, 4, 0),
    Circle(150//3, 4/3, 0),
    Circle(150//5, 4/5, 0),
]
drawing = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
graph = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

start_time = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    t = time.time() - start_time

    display.fill((255, 255, 255))

    display.blit(drawing, (0, 0))
    display.blit(graph, (0, 0))
    x = WIDTH/2
    y = HEIGHT/2
    int_x = int(x)
    int_y = int(y)
    pygame.draw.circle(display, (0, 0, 0), (int_x, int_y), 3)
    for circle in circles:
        pygame.gfxdraw.aacircle(display, int_x, int_y, circle.radius, (0, 0, 0))
        #pygame.draw.circle(display, (0, 0, 0), (int_x, int_y), circle.radius, 1)
        dx = circle.radius*math.cos(t*TWO_PI/circle.period + circle.phase)
        dy = -circle.radius*math.sin(t*TWO_PI/circle.period + circle.phase)
        pygame.draw.aaline(display, (0, 0, 0), (int_x, int_y), (int(x+dx), int(y+dy)))
        x += dx
        y += dy
        int_x = int(x)
        int_y = int(y)
        pygame.draw.circle(display, (0, 0, 0), (int_x, int_y), 3)
    pygame.draw.circle(drawing, (255, 0, 0), (int_x, int_y), 2)

    pygame.draw.circle(graph, (0, 0, 0), (int(t*20+10), int((y-HEIGHT/2)*0.2+70)), 1)

    pygame.display.flip()
    clock.tick(1000)
pygame.quit()
