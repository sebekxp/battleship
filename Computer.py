import Board
from GameUtils import *
import random
from FieldState import *


class ComputerBoard(Board.Board):
    def __init__(self, top_margin_board):
        super().__init__(top_margin_board)

    def computer_turn(self, board, row, column, shot_down_cells, target, goal, object_infob2):
        r = row
        c = column
        check_all_target = 4
        while True:

            if check_all_target == 0:
                target = random.choice(goal)
                r, c = random.randint(0, 9), random.randint(0, 9)
                check_all_target = 4

            r += target[0]
            c += target[1]

            if not row_column_in_range(r, c):
                check_all_target -= 1
                r = row
                c = column
                target = random.choice(goal)
                continue

            if board[r][c].get_state() == FieldState.HIT or \
                    board[r][c].get_state() == FieldState.MISSED or \
                    board[r][c].get_state() == FieldState.SHOTDOWN:
                check_all_target -= 1
                r = row
                c = column
                target = random.choice(goal)
                continue

            super().update_board(board, r, c)
            if (r, c) not in shot_down_cells:
                shot_down_cells.append((r, c))
            else:
                return None, None
            self.change_color_ship(object_infob2)
            return r, c
