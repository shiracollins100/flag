import pygame


SOLIDER_IMG="soldier (2).png"
SOLIDER_WIDTH=120
SOLIDER_HEIGHT=120
SOLIDER_START_row=0
SOLIDER_START_col=0


def move_in_direction(soldier_location, direction):
    soldier_location["row"] += direction[0]
    soldier_location["col"] += direction[1]

def draw_soldier():
    soldier = pygame.image.load(SOLIDER_IMG)
    soldier = pygame.transform.scale(soldier, (SOLIDER_WIDTH, SOLIDER_HEIGHT))
    return soldier


def get_soldier_position():
    pass

def change_soldier_position():
    pass

