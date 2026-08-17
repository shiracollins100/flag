import pygame


SOLIDER_IMG="soldier (2).png"
SOLIDER_WIDTH=120
SOLIDER_HEIGHT=120
SOLIDER_START_row=0
SOLIDER_START_col=0

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

def draw_soldier():
    pass

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

