import math
import os
import pygame
from random import randint
from pygame import time
from player import Player
from level_deep import ZoomMap


pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('Go Deeper')
screen.fill((0, 0, 0))
pygame.display.flip()

game_on = True
player = Player(50, 50, 40, 40, 2)
level = ZoomMap(width, height, player, [])
clock = time.Clock()
while game_on:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        game_on = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        game_on = False

    level.render_map(screen)
    clock.tick()
