import consts
from random import randint

# the matrix of the game

# create grass screen
def create_grass_field_matrix():
    grass_field_matrix = [[[] for x in range(consts.COL)] for y in range(consts.ROW)]
    for row in range(consts.ROW):
        for col in range(consts.COL):
            pos = randint(0, consts.EMPTY_COLS )
            if pos == 0:
                grass_field_matrix[row][col] = consts.GRASS_COLS
    return grass_field_matrix


# create xray screen
def create_gray_field_matrix():
    xray_field_matrix = [[[] for x in range(consts.COL)] for y in range(consts.ROW)]
    for row in range(consts.ROW):
        for col in range(consts.COL):
            pos = randint(0, consts.EMPTY_COLS )
            if pos == 0:
                xray_field_matrix[row][col] = consts.BOMB_COLS
    return xray_field_matrix

def get_x_y_position(row, column):
    pass



