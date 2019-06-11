from pygame import Rect
from GameUtils import *


class Field(Rect):
    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)
        self._state = FieldState.DEFAULT

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    @staticmethod
    def calc_left_crd(column, left_margin):
        left_crd = lambda x: x + (2 + 30) * column + 2
        return left_crd(left_margin)

    @staticmethod
    def calc_top_crd(row, top_margin):
        top_crd = lambda y: y + (2 + 30) * row + 2
        return top_crd(top_margin)

    @staticmethod
    def make_rect_info(size, top_margin):
        return [[Field(Field.calc_left_crd(c, 560), Field.calc_top_crd(r, top_margin), 30, 30) for c in range(size)]
                for r in range(1)]
