import Board
from GameUtils import *


class PlayerBoard(Board.Board):
    def __init__(self, top_margin_board):
        super().__init__(top_margin_board)

    def turn(self, board, shot_down_cells, coords_ships_info):
        column, row = change_screen_coord_to_board_coord()
        super().update_board(board, row, column)
        if row_column_in_range(row, column):
            if (row, column) not in shot_down_cells:
                shot_down_cells.append((row, column))
            else:
                return None, None
        self.change_color_ship(coords_ships_info)
        return row, column
