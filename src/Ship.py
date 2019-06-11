from GameUtils import NUMBER_ROWS
from GameUtils import NUMBER_COLUMNS
from GameUtils import decide_who_where
import random
from FieldState import *


def have_neighbours(board, row, column):
    if (row - 1 >= 0) and (board[row - 1][column].get_state() == FieldState.FILLED):
        return True
    elif (row + 1 <= NUMBER_ROWS - 1) and (board[row + 1][column].get_state() == FieldState.FILLED):
        return True
    elif (column - 1 >= 0) and (board[row][column - 1].get_state() == FieldState.FILLED):
        return True
    elif (column + 1 <= NUMBER_COLUMNS - 1) and (board[row][column + 1].get_state() == FieldState.FILLED):
        return True
    elif (column - 1 >= 0 and row - 1 >= 0) and (board[row - 1][column - 1].get_state() == FieldState.FILLED):
        return True
    elif (column + 1 <= NUMBER_COLUMNS - 1) and (row + 1 <= NUMBER_ROWS - 1) and (
            board[row + 1][column + 1].get_state() == FieldState.FILLED):
        return True
    elif (column + 1 <= NUMBER_COLUMNS - 1) and (row - 1 >= 0) and (
            board[row - 1][column + 1].get_state() == FieldState.FILLED):
        return True
    elif (column - 1 >= 0) and (row + 1 <= NUMBER_ROWS - 1) and (
            board[row + 1][column - 1].get_state() == FieldState.FILLED):
        return True

    return False


def make_ships(board, ship_size, numbers_of_ships, object_info):
    for i in range(numbers_of_ships):
        check_ship_size = 0
        while True:

            start_ships_row = random.randint(0, 9)
            start_ships_column = random.randint(0, 9)

            who, direction = decide_who_where()

            end_ships_row = start_ships_row + (direction * (ship_size - 1))
            end_ships_column = start_ships_column + (direction * (ship_size - 1))

            if ((end_ships_row > NUMBER_ROWS - 1) or (end_ships_row < 0)) or \
                    ((end_ships_column > NUMBER_COLUMNS - 1) or (end_ships_column < 0)):
                continue

            temp_ship_size = ship_size
            temp_row = start_ships_row
            temp_column = start_ships_column
            flag = False
            while temp_ship_size:
                if have_neighbours(board, temp_row, temp_column) or \
                        board[temp_row][temp_column].get_state() == FieldState.FILLED:
                    flag = True

                if who == 'row':
                    temp_row += direction
                else:
                    temp_column += direction
                temp_ship_size -= 1

            if flag:
                continue
            temp_obj_info = []
            while check_ship_size < ship_size:
                temp_obj_info.append((start_ships_row, start_ships_column))
                board[start_ships_row][start_ships_column].set_state(FieldState.FILLED)
                check_ship_size += 1
                if who == 'row':
                    start_ships_row += direction

                else:
                    start_ships_column += direction
            object_info.append(temp_obj_info)
            break
