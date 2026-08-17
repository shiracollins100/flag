import pygame
import consts
import screen
import game_field
import soldier

state = { "is_playing" : True,
        "screen": None,
        "land_on_mind" : None,
        "is_win" : False,
        "is_lost" : False,

}
def main():
    clock = pygame.time.Clock()
    screen.grass_screen(game_field.grass_field_matrix)
    while state["is_playing"]:
        clock.tick(consts.GAME_SPEED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state["is_playing"] = False

    pygame.quit()


if __name__ == "__main__":
    main()





