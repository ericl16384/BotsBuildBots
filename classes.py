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
        # miningtime 
        # products

    pass

class Tile:
    # https://lua-api.factorio.com/latest/LuaTile.html

    def __init__(self, prototype:TilePrototype, position, surface, mineableQuantity=0):
        self.PROTOTYPE = prototype
        self.POSITION = position
        self.SURFACE = surface

        if mineableQuantity:
            assert self.PROTOTYPE.mineableProperties
        else:
            assert not self.PROTOTYPE.mineableProperties
        self.mineableQuantity = mineableQuantity

class EntityPrototype:
    pass

class Entity(EntityPrototype):
    pass

class Surface:
    # https://lua-api.factorio.com/latest/LuaSurface.html

    def __init__(self, name=None):
        # INDEX
        # name

        pass

    def render(self, cameraArea:pygame.Rect, viewportSize:pygame.Rect, force=None) -> pygame.Surface:
        raise NotImplementedError


    def getTile(self, position, layer=None) -> Tile:
        raise NotImplementedError

    def setTile(self, tile:Tile, position):
        raise NotImplementedError

    def generateTile(self, position):
        raise NotImplementedError

    def generateArea(self, pos1, pos2):
        raise NotImplementedError


    def createEntity(self, prototype:Prototype, position, force):
        raise NotImplementedError

    def findEntity(self, prototype, position):
        raise NotImplementedError

    def findEntities(self, area=None):
        raise NotImplementedError

    def findEntitiesFiltered(self, area=None, position=None, radius=None, prototype=None, invert=False):
        raise NotImplementedError
