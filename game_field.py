import consts
from random import randint

# the matrix of the game
def create_matrix():
    return [[[consts.EMPTY_COLS] for x in range(consts.COL)] for y in range(consts.ROW)]



# create grass screen
def create_grass_field_matrix():
    grass_field_matrix = create_matrix
    for row in range(consts.ROW):
        for col in range(consts.COL):
            pos = randint(0, 3 )
            if pos == 0:
                grass_field_matrix[row][col] = consts.GRASS_COLS
    return grass_field_matrix

grass_field_matrix = create_grass_field_matrix()


def create_night_field_matrix():
    night_field_matrix = create_matrix
    for row in range(consts.ROW):
        for col in range(consts.COL):
            pos = randint(0, 3 )
            if pos == 0:
                night_field_matrix[row][col] = consts.BOMB_COLS
    return night_field_matrix

night_field_matrix = create_night_field_matrix()

def get_x_y_position(row, column):
    x = consts.COL_START_CENTER + column * consts.COL_LENGTH
    y = consts.COL_START_CENTER + row * consts.COL_LENGTH
    return x, y



 # the game loop, when true game is running
def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60) # updates the changes on screen - moving soldier



