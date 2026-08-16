import pygame
import consts
import screen
import game_field
import soldier

state = { "is_playing" : True,
        "screen": None,
        "field" : None,
        "land_on_mind" : None,
        "is_win" : False,
        "is_lost" : False,

}
def main():
    pygame.init()
    while state["is_playing"]:

    screen.draw_game()









