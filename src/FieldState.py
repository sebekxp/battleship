from enum import Enum


class FieldState(Enum):
    MISSED = 0
    DEFAULT = 1
    FILLED = 2
    HIT = 3
    SHOTDOWN = 4
