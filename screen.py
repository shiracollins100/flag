import pygame
from sys import exit # to close the game
import consts


pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Flag Game")
clock = pygame.time.Clock()

while True: # the game loop, when true game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60) # updates the changes on screen - moving soldier


def create_flag(flag_img):
    flag = pygame.image.load(arrow_img)
    sized_flag = pygame.transform.scale(flag, (
        consts.FLAG_WIDTH, consts.FLAG_HEIGHT))








