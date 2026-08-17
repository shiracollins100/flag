import pygame
from sys import exit # to close the game
import consts
import game_field
import main
import os


def grass_screen(grass_field_matrix):
    pygame.init()
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    screen.fill(consts.BACKGROUND_COLOR)
    draw_object_on_screen(grass_field_matrix, consts.GRASS_IMG,
                          consts.GRASS_WIDTH, consts.GRASS_HEIGHT, screen)
    pygame.display.set_caption("Flag Game")
    pygame.display.flip()




def night_screen(night_field_matrix):
    # pygame.draw.aalines(screen, NIGTH_COLOR, True, True)
    night_screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    night_screen.fill(consts.NIGHT_COLOR)
    for i in range(10,100, 30):
        pygame.draw.line(night_screen, consts.LINE_COLOR, (i,0), (i,1000), 5)
    for j in range(10,100, 30):
        pygame.draw.line(night_screen, consts.LINE_COLOR, (0, j), (1000,j), 5)

        draw_object_on_screen(night_field_matrix, consts.BOMB_IMG,
                              consts.BOMB_WIDTH, consts.BOMB_HEIGHT, night_screen)


def draw_object_on_screen(matrix, img_name, width ,hight, screen ):
    img = pygame.image.load(img_name)
    img = pygame.transform.scale(img, (width, hight))
    for row in matrix:
        for col in row:
            if col != consts.EMPTY_COLS:
                row_index = matrix.index(row)
                col_index = row.index(col)
                x, y = game_field.get_x_y_position(row_index, col_index) # need to be center
                # draw grass on screen
                screen.blit(img, (x,y))




def create_flag(flag_img):
    flag = pygame.image.load(flag_img)
    sized_flag = pygame.transform.scale(flag, (
        consts.FLAG_WIDTH, consts.FLAG_HEIGHT))

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

def draw_game():
    pass


matrix = game_field.create_grass_field_matrix()
print(matrix)
grass_screen(matrix)


