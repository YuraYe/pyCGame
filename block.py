import pygame

pd = [
    (0,0,0),
    (1,1,1),
    (1,0,0),
    (0,0,1),
    (0,1,1)
]
digits = [
    pd[3] + (1,0,1) * 3 + pd[3], # 0
    pd[3] + pd[4] + pd[3] * 3, # 1
    pd[1] + pd[3] + pd[1] + pd[2] + pd[1], # 2
    pd[1] + pd[3] + pd[4] + pd[3] + pd[1] # 3
]


class Colors:
    empty = (0,0,0)
    active = (30, 180, 60)


class Vector:
    x = 0
    y = 0
    size = 100
    def __init__(self, x=0, y=0, size=100):
        self.x = x * size
        self.y = y * size


class Block(Vector):
    color = Colors.active
    size = 100
    __id__ = 0
    visible = False

    def __init__(self, id, x, y,color=(30, 180, 60)):
        self.x = x * self.size
        self.y = y * self.size
        self.color = color
        self.__id__ = id

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))

    def log(self, val='all'):
        if val == 'all':
            print('x: {}    y: {}    size: {}    color: {}'.format(self.x,self.y,self.size,self.color))
        if val == 'coords':
            print('x: {}    y: {}'.format(self.x,self.y))
