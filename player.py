import math
from moveable_entity import MoveableEntity
import pygame
from random import randint
import time
import pdb

class Player(MoveableEntity):

    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)

    def move(self, level):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            self.move_up(level)

        if keys[pygame.K_d]:
            self.move_down(level)

        if keys[pygame.K_s]:
            self.move_left(level)

        if keys[pygame.K_f]:
            self.move_right(level)
    # UP
    def move_up(self, level):
        if (self.y - self.speed) > 0:
            self.y -= self.speed
            index = self.collidelistall(level.structural_entity_list)
            if index:
                #handle speed greater than 1 and "pixel perfect collision"
                self.y = level.structural_entity_list[index[0]].bottom

    # DOWN
    def move_down(self, level):
        if (self.y + self.height + self.speed) < level.height:
            self.y += self.speed
            index = self.collidelistall(level.structural_entity_list)
            if index:
                #handle speed greater than 1 and "pixel perfect collision"
                self.y = level.structural_entity_list[index[0]].top - self.height
    # LEFT
    def move_left(self, level):
        if (self.x - self.speed) > 0:
            self.x -= self.speed
            index = self.collidelistall(level.structural_entity_list)
            if index:
                #handle speed greater than 1 and "pixel perfect collision"
                self.x =level.structural_entity_list[index[0]].right

    # RIGHT
    def move_right(self, level):
        if (self.x + self.width + self.speed) < level.width:
            self.x += self.speed
            index = self.collidelistall(level.structural_entity_list)
            if index:
                #handle speed greater than 1 and "pixel perfect collision"
                self.x = level.structural_entity_list[index[0]].left - self.width
