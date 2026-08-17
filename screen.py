import pygame
from sys import exit # to close the game
import consts
import game_field
import main
import soldier


def grass_screen(grass_field_matrix):
    pygame.init()
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    screen.fill(consts.BACKGROUND_COLOR)
    draw_object_on_screen(grass_field_matrix, consts.GRASS_IMG,
                          consts.GRASS_WIDTH, consts.GRASS_HEIGHT, screen)
    pygame.display.set_caption("Flag Game")
    pygame.display.flip()
    clock = pygame.time.Clock()
    return screen


def night_screen(night_field_matrix):
    # pygame.draw.aalines(screen, NIGTH_COLOR, True, True)
    pygame.init()
    night_screen= pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    night_screen.fill(consts.NIGTH_COLOR)
    for i in range(1,1000,20):
        pygame.draw.line(night_screen, consts.LINE_COLOR, (i,0), (i,1000), 1)
    for j in range(1,1000,20):
        pygame.draw.line(night_screen, consts.LINE_COLOR, (0, j), (1000,j), 1)
    draw_object_on_screen(night_field_matrix, consts.BOMB_IMG,
                              consts.BOMB_WIDTH, consts.BOMB_HEIGHT, night_screen)
    pygame.display.flip()
    clock = pygame.time.Clock()
    pygame.quit()
    return night_screen

def draw_object_on_screen(matrix, img_name, width ,height, screen ):
    img = pygame.image.load(img_name)
    img = pygame.transform.scale(img, (width, height))
    for row in matrix:
        for col in row:
            if col == consts.FLAG_COL:
                create_print_flag(matrix, screen)

            elif col != consts.EMPTY_COLS:
                row_index = matrix.index(row)
                col_index = row.index(col)
                x, y = game_field.get_x_y_position(row_index, col_index) # need to be center
                screen.blit(img, (x, y))
    soldier_img = soldier.draw_soldier()

    screen.blit(soldier_img, main.state["soldier_location"])


def create_print_flag(matrix, screen):
    flag = pygame.image.load(consts.FLAG_IMG)
    flag = pygame.transform.scale(flag, (
        consts.FLAG_WIDTH, consts.FLAG_HEIGHT))
    x = consts.WINDOW_WIDTH - consts.FLAG_WIDTH
    y = consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT
    screen.blit(flag, (x, y))

def change_to_night(screen):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        night_field_matrix = game_field.create_night_field_matrix()
        screen.night_screen(night_field_matrix)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    grass_screen.blit(text_img, location)


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)
def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

def draw_soldier():
    pass

