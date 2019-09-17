from enum import Enum


class Direction(Enum):
    STOP = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


STEP, GRID = 20, 600
BORD = GRID // 2 - 10

