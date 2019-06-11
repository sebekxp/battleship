from GameUtils import *
from Field import Field
from FieldState import FieldState


class Board:
    def __init__(self, top_margin_board):
        self.board = self.make_board(top_margin_board)

    def draw_board(self):
        for row in range(NUMBER_ROWS):
            for column in range(NUMBER_COLUMNS):
                self.fill_field_img_or_color(row, column)
        pygame.display.flip()

    def get_left_top_crd(self, row, column):
        left = self.board[row][column].left
        top = self.board[row][column].top
        return left, top

    def fill_field_img_or_color(self, row, column):
        left, top = self.get_left_top_crd(row, column)
        if self.board[row][column].get_state() == FieldState.DEFAULT or \
                self.board[row][column].get_state() == FieldState.FILLED:
            screen.blit(wave_img, (left, top))
        else:
            color = self.choose_color(self.board, row, column)
            cell = [left, top, WIDTH_CELL, HEIGHT_CELL]
            pygame.draw.rect(screen, color, cell)

    @staticmethod
    def choose_color(board, row, column):
        if board[row][column].get_state() == FieldState.HIT:
            return LIGHT_GREEN
        elif board[row][column].get_state() == FieldState.SHOTDOWN:
            return RED
        else:
            return WHITE

    def blowup_animation(self, row, column):
        for image in EXPLOSION_IMAGES:
            image = pygame.transform.scale(image, (WIDTH_CELL + 15, HEIGHT_CELL + 15))
            left, top = self.get_left_top_crd(row, column)
            screen.blit(image, (left, top))
            pygame.time.Clock().tick(12)
            pygame.display.flip()

    def update_board(self, board, row, column):
        if row_column_in_range(row, column):
            if board[row][column].get_state() == FieldState.DEFAULT:
                board[row][column].set_state(FieldState.MISSED)
            elif board[row][column].get_state() == FieldState.FILLED:
                board[row][column].set_state(FieldState.HIT)
                self.blowup_animation(row, column)
        self.draw_board()

    def get_board(self):
        return self.board

    @staticmethod
    def make_board(top_margin_board):
        """Make array of Field Object that contains state and rect..."""
        return [[Field(Field.calc_left_crd(c, LEFT_MARGIN_BOARDS), Field.calc_top_crd(r, top_margin_board), 30, 30)
                 for c in range(10)]
                for r in range(10)]

    def draw_viewfinder(self):
        column, row = change_screen_coord_to_board_coord()
        if row_column_in_range(row, column):
            for r in range(NUMBER_ROWS):
                for c in range(NUMBER_COLUMNS):
                    left, top = self.get_left_top_crd(row, column)
                    if r == row and c == column:
                        screen.blit(viewfinder, (left, top))
                    else:
                        self.fill_field_img_or_color(r, c)
        else:
            self.draw_board()
        pygame.display.flip()

    def change_color_ship(self, obj_info):
        ships_coords = []
        for row in range(NUMBER_ROWS):
            for col in range(NUMBER_COLUMNS):
                if self.board[row][col].get_state() == FieldState.HIT:
                    ships_coords.append((row, col))

        for i in obj_info:
            temp_flag = len(i)
            tmp_len = len(i)
            for j in i:
                if j in ships_coords:
                    temp_flag -= 1
                    if temp_flag == 0:
                        for row, col in i:
                            print(self.board[row][col], self.board[row][col].get_state())
                            self.board[row][col].set_state(FieldState.SHOTDOWN)
                        if str(type(self).__name__) == 'PlayerBoard':
                            if tmp_len == 1:
                                draw_rect_info_player(230, 4)
                            elif tmp_len == 2:
                                draw_rect_info_player(180, 3)
                            elif tmp_len == 3:
                                draw_rect_info_player(130, 2)
                            elif tmp_len == 4:
                                draw_rect_info_player(76, 1)
                        elif str(type(self).__name__) == 'ComputerBoard':
                            if tmp_len == 1:
                                draw_rect_info_comp(680, 4)
                            elif tmp_len == 2:
                                draw_rect_info_comp(630, 3)
                            elif tmp_len == 3:
                                draw_rect_info_comp(580, 2)
                            elif tmp_len == 4:
                                draw_rect_info_comp(526, 1)
                        self.draw_board()
