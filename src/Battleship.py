from GameUtils import *
import Player
import Computer
from Exceptions import *
from Ship import *
from Field import *


class Battleship:

    def __init__(self):
        self.player = Player.PlayerBoard(TOP_MARGIN_PLAYER)
        self.computer = Computer.ComputerBoard(TOP_MARGIN_COMPUTER)

        self.player_coords_ships_info = []
        self.computer_coords_ships_info = []

        make_ships(self.player.get_board(), 4, 1, self.player_coords_ships_info)
        make_ships(self.player.get_board(), 3, 2, self.player_coords_ships_info)
        make_ships(self.player.get_board(), 2, 3, self.player_coords_ships_info)
        make_ships(self.player.get_board(), 1, 4, self.player_coords_ships_info)

        make_ships(self.computer.get_board(), 4, 1, self.computer_coords_ships_info)
        make_ships(self.computer.get_board(), 3, 2, self.computer_coords_ships_info)
        make_ships(self.computer.get_board(), 2, 3, self.computer_coords_ships_info)
        make_ships(self.computer.get_board(), 1, 4, self.computer_coords_ships_info)

        self.shot_down_cells_player = []
        self.shot_down_cells_computer = []
        self._done = False

        self.play_btn = screen.blit(play_btn_img, play_btn_rect)
        self.exit_btn = screen.blit(exit_btn_img, exit_btn_rect)

        screen.blit(player_ship4_img, (540, 65))
        screen.blit(player_ship3_img, (540, 110))
        screen.blit(player_ship2_img, (540, 160))
        screen.blit(player_ship1_img, (540, 220))

        screen.blit(comp_ship4_img, (540, 515))
        screen.blit(comp_ship3_img, (540, 560))
        screen.blit(comp_ship2_img, (540, 620))
        screen.blit(comp_ship1_img, (540, 680))
        draw_text_chat_border()

        self.player.draw_board()
        self.computer.draw_board()

        self.rect = pygame.Rect(600, 250, 90, 30)

    def listener(self):
        while not self._done:
            for event in pygame.event.get():
                self.player.draw_viewfinder()
                draw_text(LEFT_MARGIN_BOARDS + 80, TOP_MARGIN_COMPUTER - 40, "Your Turn", BLACK)
                if event.type == pygame.QUIT:
                    self._done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    player_row, player_col = self.player.turn(self.player.get_board(), self.shot_down_cells_player,
                                                              self.player_coords_ships_info)
                    if player_row is None or player_col is None:
                        try:
                            raise ShootInTheSamePlace("Don't shoot in the same place")
                        except ShootInTheSamePlace as s:
                            draw_text(60, TOP_MARGIN_COMPUTER - 40, s.get_message(), BLACK)
                        pygame.time.delay(1000)
                        continue

                    if row_column_in_range(player_row, player_col):
                        draw_text_chat("Player", player_row, player_col)
                        if self.player.get_board()[player_row][player_col].get_state() == FieldState.HIT:
                            continue
                        computer_row, computer_col = random.randint(0, 9), random.randint(0, 9)
                        goal = [(1, 0), (0, 1), (-1, 0), (0, - 1)]
                        target = random.choice(goal)
                        while True:
                            draw_text(LEFT_MARGIN_BOARDS + 60, TOP_MARGIN_COMPUTER - 40,
                                      "Computer Turn", BLACK)
                            pygame.time.delay(300)
                            computer_row, computer_col = self.computer.computer_turn(self.computer.get_board(),
                                                                                     computer_row, computer_col,
                                                                                     self.shot_down_cells_computer,
                                                                                     target,
                                                                                     goal,
                                                                                     self.computer_coords_ships_info)
                            draw_text_chat("Computer", computer_row, computer_col)
                            if computer_row is None or computer_col is None:
                                computer_row, computer_col = random.randint(0, 9), random.randint(0, 9)
                                continue
                            if self.computer.get_board()[computer_row][computer_col].get_state() == FieldState.HIT or \
                                    self.computer.get_board()[computer_row][
                                        computer_col].get_state() != FieldState.MISSED:
                                continue
                            else:
                                break
                    elif self.exit_btn.collidepoint(pygame.mouse.get_pos()):
                        self._done = True
                    elif self.play_btn.collidepoint(pygame.mouse.get_pos()):
                        self.__init__()
                    else:
                        try:
                            raise CoordsCellOutOfRange("Cell coords outside of the board")
                        except CoordsCellOutOfRange as c:
                            draw_text(40, TOP_MARGIN_COMPUTER - 40, c.get_message(), BLACK)
                            pygame.time.delay(1000)

                if self.play_btn.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(green_play_btn_img, green_play_btn_rect)
                if self.exit_btn.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(green_exit_img, green_exit_rect)
                if not self.exit_btn.collidepoint(pygame.mouse.get_pos()):
                    self.exit_btn = screen.blit(exit_btn_img, exit_btn_rect)
                if not self.play_btn.collidepoint(pygame.mouse.get_pos()):
                    self.play_btn = screen.blit(play_btn_img, play_btn_rect)

                    if check_win(self.player.get_board(), "Congratulations, You Won :)"):
                        self._done = True

                    if check_win(self.computer.get_board(), "Computer Won :("):
                        self._done = True

    def run(self):
        self.listener()


def main():
    game = Battleship()
    game.run()


if __name__ == "__main__":
    main()
