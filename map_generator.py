from random import randint, random

import pygame

# in progress map generator, not yet functional


class MapGenerator():

    def __init__(self, mapWidth, mapHeight, playerRect, exitRect):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.playerRect = playerRect
        self.exitRect = exitRect
        self.playerIntersectList = [playerRect]
        self.exitRectList = [exitRect]
        playerX, playerY, playerWidth, playerHeight, = playerRect
        exitX, exitY, exitWidth, exitHeight, = exitRect
        self.pathWidth = (max(playerHeight, playerWidth))
        self.pathWidth += self.pathWidth / 3

    def getRandomRect(self, length):
        vertical = False
        if random() >= 0.5:
            vertical = True
        x = randint(0 - length / 2, self.mapWidth)
        y = randint(0 - length / 2, self.mapHeight)
        if vertical:
            return pygame.Rect(x, y, self.pathWidth, length)
        return pygame.Rect(x, y, length, self.pathWidth)

    def buildPaths(self):
        rectList = []
        for i in range(200):
            rectList.append(getRandomRect(randint(120, 480)))

        playerIntersectSet = sets.Set()
        exitIntersectSet = sets.Set()
        playerCollideIndexList = playerRect.collideListAll(rectList)
        exitCollideIndexList = exitRect.collideListAll(rectList)

        playerCollideList = listFromIndexList(playerCollideIndexList, rectList)
        exitCollideList = listFromIndexList(exitCollideIndexList, rectList)

        for rectIndexP in playerCollideIndexList:
            indexes = rectList[rectIndexP].collideListAll(exitCollideList)
            if indexes:
                print(rectList[exitCollideList[indexes[0]]])

    def listFromIndexList(self, indexList, rectList):
        toReturn = []
        for index in indexList:
            toReturn.append(rectList[index])
        return toReturn


mapGen = MapGenerator(
    800, 800, pygame.Rect(50, 50, 40, 40), pygame.Rect(500, 700, 60, 60))
print(mapGen.getRandomRect(120))
