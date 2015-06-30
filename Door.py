import entity

# unfinished class for level exit structure


class Door(entity):

    def __init__(self, x, y, width, height, isopen):
    super().__init__(x, y, width, height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
