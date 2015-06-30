import pygame
from entity import Entity


class MoveableEntity(Entity):

    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height)
        self.speed = speed

    def move(self, level):
        "movable entities must move"
        raise NotImplementedError
