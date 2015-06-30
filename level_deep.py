from level import Map
import math
import pygame
from pygame import transform
from transform import smoothscale
from wall import Wall
from random import randint


class ZoomMap(Map):

    """falling down 2d map"""

    def __init__(self, width, height, player, entities):
        super().__init__(width, height, player, entities)
        self.magnification_booster = 0
        self.structural_entity_list = self.build_map()
        self.entities.extend(self.structural_entity_list)
        self.depth_counter = 0
        self.frame_counter = 0
        self.zoom_box = (0, 0, width, height)
        self.surface = pygame.Surface((width, height))
        self.width_ratio = self.width / self.height

    def build_map(self):
        # still working on map generator
        w = self.width
        h = self.height
        rect_list = []
        rect_list.append(Wall(w / 4, h / 4, 25, 300))
        rect_list.append(Wall(3 * w / 4, 3 * h / 4, 25, 300))
        rect_list.append(Wall(80, 160, w - 200, 70))
        return rect_list

    def render_map(self, screen):

        self.frame_counter += 1
        if(self.frame_counter % 5 == 0 and self.frame_counter > 200):
            self.depth_counter += 1

        screen.fill((0, 0, 0))
        image = self.surface
        image.fill((0, 0, 0))

        for structure in self.structural_entity_list:
            image.fill(structure.color, structure.copy())

        self.player.move(self)
        image.fill((0, 0, 212), self.player.copy())

        zoom_image = pygame.Surface((self.width - self.depth_counter * self.width_ratio,
                                     self.height - self.depth_counter))
        zoom_rect = zoom_image.get_rect()
        zoom_rect.center = self.player.center
        self.zoom_box = zoom_rect.clamp(screen.get_rect())
        zoom_image.blit(image, (0, 0), self.zoom_box)
        zoom_image = smoothscale(zoom_image, screen.get_size())
        screen.blit(zoom_image, (0, 0))
        pygame.display.flip()
