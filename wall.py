import pygame

from entity import Entity


class Wall(Entity):
    def __init__ (self, x, y, width, height,):
            super().__init__(x, y, width, height,)
            self.color = (155, 5, 50)

