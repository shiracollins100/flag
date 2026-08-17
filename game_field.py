import consts
from random import randint

# the matrix of the game
def create_matrix():
    matrix = [[consts.EMPTY_COLS for x in range(consts.COL)] for y in range(consts.ROW)]
    matrix[consts.ROW-1][consts.COL-1] = consts.FLAG_COL
    return matrix


# create grass screen
def create_grass_field_matrix():
    grass_field_matrix = create_matrix()
    for row in range(consts.ROW):
        for col in range(consts.COL):
            if grass_field_matrix[row][col] != consts.FLAG_COL:
                pos = randint(0, 20 )
                if pos == 0:
                    grass_field_matrix[row][col] = consts.GRASS_COLS
    return grass_field_matrix



def create_night_field_matrix():
    night_field_matrix = create_matrix()
    for row in range(consts.ROW):
        for col in range(consts.COL):
            pos = randint(0,20 )
            if pos == 0:
                night_field_matrix[row][col] = consts.BOMB_COLS

    return night_field_matrix

#--------------------------------------------------------------

def print_matrix(matrix):
    for row in range(consts.ROW):
        for col in range(consts.COL):
            print(matrix[row][col], end=" ")
        print()


a = create_matrix()
b = create_grass_field_matrix()
c =create_night_field_matrix()

print_matrix(a)
print()
print()
print_matrix(b)
print()
print()
print_matrix(c)



#---------------------------------------------------------------


def get_x_y_position(row, column):
    x = consts.COL_START_CENTER + (column * consts.COL_LENGTH)
    y = consts.COL_START_CENTER + (row * consts.COL_LENGTH)
    return x, y





def is_valid_position():
    pass
def get_cell():
    pass