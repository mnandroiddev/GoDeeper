import pygame


class Map:

    def __init__(self, width, height, player, entities):
        self.width = width
        self.height = height
        self.player = player
        self.entities = entities
        

    def render_map(self, screen):
        screen.fill((0, 0, 0))
        self.player.move(self)
        screen.fill((50, 0, 0), self.player.copy())
        pygame.display.flip()
