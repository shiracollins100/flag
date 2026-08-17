import game_field

SOLDIER_IMG="soldier.png"
SOLDIER_WIDTH=40
SOLDIER_HEIGHT=120
SOLDIER_START_row=0
SOLDIER_START_col=0
SOLDIER_LOCATION={"row": SOLDIER_START_row, "col": SOLDIER_START_col}
import screen
import pygame
def move_in_direction(soldier_location, direction):
    soldier_location["row"] += direction[0]
    soldier_location["col"] += direction[1]

'''def draw_soldier():
    import screen
    pygame.init()
    img = pygame.image.load(SOLDIER_IMG)
    img = pygame.transform.scale(img, (SOLDIER_WIDTH, SOLDIER_HEIGHT))
    screen.screen.blit(img, (SOLDIER_START_col,SOLDIER_START_row))
    game_field.grass_field_matrix.insert(0,img)'''

def get_soldier_position():
    x, y=0, 0
    vel=1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    pygame.display.update()


def change_soldier_position():
    pass

