"https://lua-api.factorio.com/latest/"


# Imports

# Base
import math, random

# Installed
import pygame


# Classes


## Coordinates

class CoordinatePairKey:
    def __init__(self, x:int, y:int):
        "When hashed, results in a 32-bit integer. X and Y values must be in range(-(2**16), 2**16)"

        x = int(x)
        y = int(y)

        # 2**16 = 65536
        assert x >= -65536 
        assert x < 65536
        assert y >= -65536
        assert y < 65536

        self.__PAIR = x, y

        positiveX = x + 32768 # 2**15 = 32768
        shiftedX = (positiveX << 16)
        self.__HASH = shiftedX + y - 2147483648 # 2**15 << 16 = 2147483648
    
    def __hash__(self):
        return self.__HASH
    
    def __getitem__(self, key):
        return self.__PAIR[key]
    
    def __str__(self):
        return f"<{self.__class__.__name__} {self.__PAIR}>"


## Prototypes

class Prototype:
    pass

class TilePrototype(Prototype):
    # https://lua-api.factorio.com/latest/LuaTilePrototype.html

    def __init__(self, name, graphics, layer, mineableProperties={}):
        self.name = name
        self.graphics = graphics
        self.layer = layer
        self.mineableProperties = mineableProperties

        # name
        # layer
        # mineableProperties
            # miningtime 
            # products

class EntityPrototype(Prototype):
    pass


## Instances of prototypes

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

class Entity:
    pass


## Surface

class Surface:
    # https://lua-api.factorio.com/latest/LuaSurface.html
    # chunk size 32x32

    def __init__(self, seed=..., terrainGenerator=lambda s,p:{}):
        "terrainGenerator needs to convert seed and position to a dictionary of tiles"

        if seed == ...:
            random.seed()
            seed = random.randint(0, 4294967296) # 2**32
        self.SEED = seed

        self.terrainGenerator = terrainGenerator

        self.chunks = {}
    
    def getJsonSerializable(self):
        raise NotImplementedError

    def render(self, cameraPos, cameraZoom:float, viewportSize:pygame.Rect, force=None) -> pygame.Surface:
        viewportRatio = viewportSize.w/viewportSize.h

        mapArea = (
            (
                math.floor(cameraPos[0] - cameraZoom*viewportRatio),
                math.floor(cameraPos[1] - cameraZoom)
            ),
            (
                math.ceil(cameraPos[0] + cameraZoom*viewportRatio),
                math.ceil(cameraPos[1] + cameraZoom)
            )
        )

        raise NotImplementedError

    
    # Chunks

    def getChunkKey(self, chunkPos):
        return CoordinatePairKey(
            chunkPos[0] // 32,
            chunkPos[1] // 32
        )

    def getGeneratedChunks(self) -> dict:
        return self.chunks

    def setChunk(self, chunkPos, chunk, posIsKey=False):
        # chunkKey
        if posIsKey:
            chunkPos, chunkKey = tuple(chunkPos), chunkPos
        else:
            chunkKey = self.getChunkKey(chunkPos)

        # Write
        self.chunks[chunkKey] = chunk
  
    def generateChunk(self, chunkPos, posIsKey=False, write=True):
        # chunkKey
        #if posIsKey:
        #    chunkPos, chunkKey = tuple(chunkPos), chunkPos
        #else:
        #    chunkKey = self.getChunkKey(chunkPos)

        # Generate
        chunkCorner = (
            chunkPos[0] * 32,
            chunkPos[1] * 32
        )
        chunk = []
        for x in range(32):
            chunk.append([])
            for y in range(32):
                chunk[-1].append(self.generateTile((
                    chunkCorner[0] + x,
                    chunkCorner[1] + y
                ), False))

        # Write
        if write:
            self.setChunk(chunkPos, chunk, posIsKey)
        
        # Return
        return chunk
  
    def getChunk(self, chunkPos, posIsKey=False):
        raise NotImplementedError

        # chunkKey
        if posIsKey:
            chunkPos, chunkKey = tuple(chunkPos), chunkPos
        else:
            chunkKey = self.getChunkKey(chunkPos)

        # return (and generate)
        try:
            return self.chunks[chunkKey]
        except KeyError:
            self.generateChunk(chunkPos)
            return self.chunks[chunkKey]


    # Tiles

    def setTile(self, tile:Tile, position):
        chunkKey = self.getChunkKey(position)
        x = position[0] % 32
        y = position[1] % 32

        # Set up the data structure
        if chunkKey not in self.chunks.keys():
            self.generateChunk(chunkKey, True)

        # Set the tile
        self.getChunk(chunkKey, True)[x][y] = tile

    def generateTile(self, position, write=True):
        # Generate
        tile = self.terrainGenerator(self.SEED, position)

        # Write
        if write:
            self.setTile(tile, position)

        # Return
        return tile

    def getTile(self, position) -> Tile:
        chunkX, x = divmod(position[0], 32)
        chunkY, y = divmod(position[1], 32)

        return self.getChunk((chunkX, chunkY))[x][y]

    
    # Area

    def setArea(self, rect, tiles):
        raise NotImplementedError

    def generateArea(self, rect, write=True):
        raise NotImplementedError

    def getArea(self, rect):
        raise NotImplementedError


    # Entities

    def createEntity(self, prototype:Prototype, position, force):
        raise NotImplementedError

    def findEntity(self, prototype, position):
        raise NotImplementedError

    def findEntities(self, area=None):
        raise NotImplementedError

    def findEntitiesFiltered(self, area=None, position=None, radius=None, prototype=None, invert=False):
        raise NotImplementedError


## Game Session

class GameSession:
    pass
