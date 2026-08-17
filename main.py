import pygame
import consts
import screen
import game_field
import soldier

state = { "is_playing" : True,
        "screen": "grass",
        "land_on_mind" : None,
        "is_win" : False,
        "is_lost" : False,
        "soldier_location" : (soldier.SOLIDER_START_row, soldier.SOLIDER_START_col)

}
def main():
    clock = pygame.time.Clock()
    grass_field_matrix = game_field.create_grass_field_matrix()
    night_field_matrix = game_field.create_night_field_matrix()
    screen.grass_screen(grass_field_matrix)
    #screen.night_screen(night_field_matrix)
    while state["is_playing"]:
        clock.tick(consts.GAME_SPEED)

        if state["screen"] == "night":
            pass # show night field

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state["is_playing"] = False

    pygame.quit()


if __name__ == "__main__":
    main()





