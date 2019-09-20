from enum import Enum
import os
import turtle


class Direction(Enum):
    STOP = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


SCREEN = 750
GRID = 600
STEP = 20
DELAY = 0.12
BORD = GRID // 2 - 10

SNAKE_START = (-30, 30)
FOOD_START = (-30, 110)
SCORE_POS = (320, 320)
RECORD_POS = (260, 320)

APPLE_LOGO_POS = (300, 330)
TROPHY_LOGO_POS = (240, 330)

BG_PATH = os.getcwd() + '/resources/sn.gif'
APPLE_PATH = os.getcwd() + '/resources/apple.gif'
TROPHY_PATH = os.getcwd() + '/resources/trophy.gif'

turtle.register_shape(APPLE_PATH)
turtle.register_shape(TROPHY_PATH)