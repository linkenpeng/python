import pygame
from pygame.locals import *
from sys import exit

screen_width = 800
screen_height = 600

pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('this is my first game')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit

    screen.fill((0, 0, 0))
    pygame.display.update()
