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
    screen.draw_game(screen)

    #while state["is_playing"]:

main()








