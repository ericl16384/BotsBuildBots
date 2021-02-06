"https://lua-api.factorio.com/latest/"


# Imports

import pygame


# Classes

class Prototype:
    pass

class TilePrototype(Prototype):
    # https://lua-api.factorio.com/latest/LuaTilePrototype.html

    # name
    # layer
    # mineableProperties
        # mineable
        # miningtime 
        # products

    pass

class Tile:
    # https://lua-api.factorio.com/latest/LuaTile.html

    def __init__(self, prototype:TilePrototype, position, surface):
        self.POSITION = position
        self.SURFACE = surface

class Surface:
    # https://lua-api.factorio.com/latest/LuaSurface.html

    def __init__(self, name=None):
        # INDEX
        # name

        pass

    def render(self, cameraArea:pygame.Rect) -> pygame.Surface:
        raise NotImplementedError

    def getTile(self, x, y, layer=None) -> Tile:
        raise NotImplementedError

    def setTile(self, tile:Tile, x, y, layer=None):
        raise NotImplementedError

    def createEntity(self, prototype:Prototype, position, force):
        raise NotImplementedError

    def findEntity(self, prototype, position):
        raise NotImplementedError

    def findEntities(self, area=None):
        raise NotImplementedError

    def findEntitiesFiltered(self, area=None, position=None, radius=None, prototype=None, invert=False)
