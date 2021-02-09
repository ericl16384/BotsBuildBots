# TODO
# These are to check that things have not broken, and ensure determinism.


# Imports

print("Importing modules")

# Base
import json, sys, os, zlib
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# Installed
import pygame

# Util modules
import colors

# Game modules
import classes

# Prototypes
import prototypes


# Testcases


## classes.CoordinatePairKey

print("Testing classes.CoordinatePairKey")

assert hash(classes.CoordinatePairKey(-65536, -65536)) == -4295032832
assert hash(classes.CoordinatePairKey(-65536, 0)) == -4294967296
assert hash(classes.CoordinatePairKey(-65536, 65535)) == -4294901761

assert hash(classes.CoordinatePairKey(0, -65536)) == -65536
assert hash(classes.CoordinatePairKey(0, 0)) == 0
assert hash(classes.CoordinatePairKey(0, 65535)) == 65535

assert hash(classes.CoordinatePairKey(65535, -65536)) == 4294836224
assert hash(classes.CoordinatePairKey(65535, 0)) == 4294901760
assert hash(classes.CoordinatePairKey(65535, 65535)) == 4294967295


## classes.Prototype

pass


## classes.TilePrototype

pass


## classes.EntityPrototype

pass


## classes.Tile

pass


## classes.Entity

pass


## classes.Surface

surface = classes.Surface(1234567890)
surface.generateChunk((0, 0))

#with open("dump.txt", "w") as f:
#    print(surface.getGeneratedChunks(), file=f)
#assert surface.getGeneratedChunks() == compressed json


## classes.GameSession

#assert GameSession.getJsonSerializable() == asdf
