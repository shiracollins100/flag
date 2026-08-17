import pygame
from sys import exit # to close the game
import consts
import game_field
import main


def grass_screen():
    pygame.init()
    game_field.create_grass_field_matrix()
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.set_caption("Flag Game")
    pygame.display.flip()
    clock = pygame.time.Clock()


    while main.state["is_playing"]:  # the game loop, when true game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(60)  # updates the changes on screen - moving soldier
    return screen


def night_screen():
    #pygame.draw.aalines(screen, NIGTH_COLOR, True, True)
    pygame.init()
    game_field.create_night_field_matrix()
    night_screen= pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    night_screen.fill(consts.NIGTH_COLOR)
    pygame.display.flip()
    clock = pygame.time.Clock()
    for i in range(1,1000,20):
        pygame.draw.line(night_screen, consts.LINE_COLOR, (i,0), (i,1000), 1)
    for j in range(1,1000,20):
        pygame.draw.line(night_screen, consts.LINE_COLOR, (0, j), (1000,j), 1)


    while main.state["is_playing"]:  # the game loop, when true game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(60)  # updates the c
    return night_screen

def create_flag(flag_img):
    flag = pygame.image.load(flag_img)
    sized_flag = pygame.transform.scale(flag, (
        consts.FLAG_WIDTH, consts.FLAG_HEIGHT))
    return sized_flag

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

def draw_game():
    grass_screen()
    #night_screen()
