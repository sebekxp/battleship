import pygame
import random
from FieldState import FieldState
from Field import Field

WIDTH_CELL = 30
HEIGHT_CELL = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 780

SCREEN_TITLE = "Battleship"
WINDOW_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
pygame.display.set_caption(SCREEN_TITLE)

MARGIN_BETWEEN_CELL = 2

NUMBER_ROWS = 10
NUMBER_COLUMNS = 10

LEFT_MARGIN_BOARDS = 100
TOP_MARGIN_PLAYER = 85
TOP_MARGIN_COMPUTER = 452

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (70, 70, 70)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 97, 3)
DARK_GREEN = (26, 54, 63)
DARK_GREEN_2 = (15, 38, 45)
LIGHT_GREEN = (175, 227, 80)

WIN_CONDITION = 20

wave_img = pygame.image.load(r'D:\PyProj\img\fala.png')
wave_img = pygame.transform.scale(wave_img, (30, 30))
viewfinder = pygame.image.load(r'D:\PyProj\img\c1.png')
viewfinder = pygame.transform.scale(viewfinder, (30, 30))

screen = pygame.display.set_mode(WINDOW_SIZE)

play_btn_img = pygame.image.load(r'D:\PyProj\img\play_btn.png').convert_alpha()
play_btn_rect = play_btn_img.get_rect()
play_btn_rect = (100, 10)

green_play_btn_img = pygame.image.load(r'D:\PyProj\img\green_play_btn.png').convert_alpha()
green_play_btn_rect = green_play_btn_img.get_rect()
green_play_btn_rect = (100, 10)

exit_btn_img = pygame.image.load(r'D:\PyProj\img\exit.png').convert_alpha()
exit_btn_rect = exit_btn_img.get_rect()
exit_btn_rect = (275, 10)

green_exit_img = pygame.image.load(r'D:\PyProj\img\green_exit.png').convert_alpha()
green_exit_rect = green_play_btn_img.get_rect()
green_exit_rect = (275, 10)

player_ship4_img = pygame.image.load(r'D:\PyProj\img\ship4.png').convert_alpha()
player_ship3_img = pygame.image.load(r'D:\PyProj\img\ship3.png').convert_alpha()
player_ship2_img = pygame.image.load(r'D:\PyProj\img\ship2.png').convert_alpha()
player_ship1_img = pygame.image.load(r'D:\PyProj\img\ship1.png').convert_alpha()

player_ship4_red_img = pygame.image.load(r'D:\PyProj\img\ship4_red.png').convert_alpha()
player_ship3_red_img = pygame.image.load(r'D:\PyProj\img\ship3_red.png').convert_alpha()
player_ship2_red_img = pygame.image.load(r'D:\PyProj\img\ship2_red.png').convert_alpha()
player_ship1_red_img = pygame.image.load(r'D:\PyProj\img\ship1_red.png').convert_alpha()

comp_ship4_img = pygame.image.load(r'D:\PyProj\img\ship4.png').convert_alpha()
comp_ship3_img = pygame.image.load(r'D:\PyProj\img\ship3.png').convert_alpha()
comp_ship2_img = pygame.image.load(r'D:\PyProj\img\ship2.png').convert_alpha()
comp_ship1_img = pygame.image.load(r'D:\PyProj\img\ship1.png').convert_alpha()

comp_ship4_red_img = pygame.image.load(r'D:\PyProj\img\ship4_red.png').convert_alpha()
comp_ship3_red_img = pygame.image.load(r'D:\PyProj\img\ship3_red.png').convert_alpha()
comp_ship2_red_img = pygame.image.load(r'D:\PyProj\img\ship2_red.png').convert_alpha()
comp_ship1_red_img = pygame.image.load(r'D:\PyProj\img\ship1_red.png').convert_alpha()

screen.fill(BLACK)
pygame.font.init()

EXPLOSION_IMAGES = [
    pygame.image.load("img/blowup1.png"), pygame.image.load("img/blowup2.png"),
    pygame.image.load("img/blowup3.png"), pygame.image.load("img/blowup4.png"),
    pygame.image.load("img/blowup5.png"), pygame.image.load("img/blowup6.png"),
    pygame.image.load("img/black_square.png")]

first_occur = False


class RectInfoPlayer:
    """We add one bcs we first decrement rect_info"""
    RECT_INFO4X = 1 + 1
    RECT_INFO3X = 2 + 1
    RECT_INFO2X = 3 + 1
    RECT_INFO1X = 4 + 1


rect_info_player = RectInfoPlayer()


class RectInfoComp:
    """We add one bcs we first decrement rect_info"""
    RECT_INFO4X = 1 + 1
    RECT_INFO3X = 2 + 1
    RECT_INFO2X = 3 + 1
    RECT_INFO1X = 4 + 1


rect_info_comp = RectInfoPlayer()


def draw_rect_info_player(top_margin, text):
    if text == 1:
        rect_info_player.RECT_INFO4X -= 1
        text = rect_info_player.RECT_INFO4X
    elif text == 2:
        rect_info_player.RECT_INFO3X -= 1
        text = rect_info_player.RECT_INFO3X
    elif text == 3:
        rect_info_player.RECT_INFO2X -= 1
        text = rect_info_player.RECT_INFO2X
    elif text == 4:
        rect_info_player.RECT_INFO1X -= 1
        text = rect_info_player.RECT_INFO1X
    pygame.draw.rect(screen, BLACK, (490, top_margin, 40, 40))
    label = pygame.font.SysFont(pygame.font.match_font("monospace", True), 45).render(f"{text}x ", 1, WHITE)
    screen.blit(label, (490, top_margin))
    if rect_info_player.RECT_INFO4X == 0:  screen.blit(player_ship4_red_img, (540, 65))
    if rect_info_player.RECT_INFO3X == 0:  screen.blit(player_ship3_red_img, (540, 110))
    if rect_info_player.RECT_INFO2X == 0:  screen.blit(player_ship2_red_img, (540, 160))
    if rect_info_player.RECT_INFO1X == 0:  screen.blit(player_ship1_red_img, (540, 220))


def draw_rect_info_comp(top_margin, text):
    if text == 1:
        rect_info_comp.RECT_INFO4X -= 1
        text = rect_info_comp.RECT_INFO4X
    elif text == 2:
        rect_info_comp.RECT_INFO3X -= 1
        text = rect_info_comp.RECT_INFO3X
    elif text == 3:
        rect_info_comp.RECT_INFO2X -= 1
        text = rect_info_comp.RECT_INFO2X
    elif text == 4:
        rect_info_comp.RECT_INFO1X -= 1
        text = rect_info_comp.RECT_INFO1X
    pygame.draw.rect(screen, BLACK, (490, top_margin, 40, 40))
    label = pygame.font.SysFont(pygame.font.match_font("monospace", True), 45).render(f"{text}x ", 1, WHITE)
    screen.blit(label, (490, top_margin))
    if rect_info_comp.RECT_INFO4X == 0:  screen.blit(comp_ship4_red_img, (540, 515))
    if rect_info_comp.RECT_INFO3X == 0:  screen.blit(comp_ship3_red_img, (540, 560))
    if rect_info_comp.RECT_INFO2X == 0:  screen.blit(comp_ship2_red_img, (540, 620))
    if rect_info_comp.RECT_INFO1X == 0:  screen.blit(comp_ship1_red_img, (540, 680))


draw_rect_info_player(76, 1)
draw_rect_info_player(130, 2)
draw_rect_info_player(180, 3)
draw_rect_info_player(230, 4)

draw_rect_info_comp(526, 1)
draw_rect_info_comp(580, 2)
draw_rect_info_comp(630, 3)
draw_rect_info_comp(680, 4)


def draw_text_chat_border():
    pygame.draw.rect(screen, LIGHT_GREEN, (490, 280, 300, 205), 4)


class ChatMsg:
    count = 0
    msg_height = 0


ChatMsg = ChatMsg()

TOP_MARGIN_CHAT = 283


def draw_text_chat(who, row, col):
    if ChatMsg.count % 5 == 0:
        pygame.draw.rect(screen, BLACK, (493, TOP_MARGIN_CHAT, 295, 200))
        ChatMsg.msg_height = 0
    else:
        ChatMsg.msg_height += 40
    color = DARK_GREEN_2 if ChatMsg.count % 2 else DARK_GREEN
    pygame.draw.rect(screen, color, (493, ChatMsg.msg_height + TOP_MARGIN_CHAT, 295, 40))
    label = pygame.font.SysFont(pygame.font.match_font("monospace", True), 25).render(f"{who} shoot: [{row}][{col}]", 1,
                                                                                      WHITE)
    ChatMsg.count += 1
    screen.blit(label, (493 + 5, ChatMsg.msg_height + TOP_MARGIN_CHAT + 10))


def change_screen_coord_to_board_coord():
    pos = pygame.mouse.get_pos()
    column = (pos[0] - LEFT_MARGIN_BOARDS) // (WIDTH_CELL + MARGIN_BETWEEN_CELL)
    row = (pos[1] - TOP_MARGIN_PLAYER) // (HEIGHT_CELL + MARGIN_BETWEEN_CELL)
    return column, row


def decide_who_where():
    who = random.choice(['row', 'column'])
    direction = random.choice([1, -1])
    return who, direction


def check_win(board, str):
    win_condition = 0
    for row in range(NUMBER_ROWS):
        for column in range(NUMBER_COLUMNS):
            if board[row][column].get_state() == FieldState.SHOTDOWN:
                win_condition += 1
            if win_condition == WIN_CONDITION:
                screen.fill(BLACK)
                draw_text(200, 150, str, BLACK)
                for i in range(9, 0, -1):
                    draw_text(150, 300, f"The game will close in {i} seconds...", BLACK, 700)
                    pygame.time.delay(1000)
                return True
    return False


def draw_reset_button(btn):
    draw_text(btn[0], btn[1], "NEW GAME", GREEN, btn[2], btn[3], 0, RED, 50)


def draw_text(left_margin, top_margin, str, color, mask_width=450, mask_height=40, margin_mask=150, font_color=WHITE,
              font_size=40):
    pygame.draw.rect(screen, color, pygame.Rect(left_margin - margin_mask, top_margin, mask_width, mask_height))
    label = pygame.font.SysFont(pygame.font.match_font("monospace", True), font_size).render(str, 1, font_color)
    screen.blit(label, (left_margin, top_margin))
    pygame.display.flip()


def decorator(fun):
    def wrap(row, column):
        return fun(row, column)
    return wrap


@decorator
def row_column_in_range(row, column):
    return (0 <= row < NUMBER_ROWS) and (0 <= column < NUMBER_COLUMNS)
