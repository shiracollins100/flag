SOLIDER_IMG = soldier.png
SOLIDER_WIDTH=40
SOLIDER_HEIGHT=120
SOLIDER_START_row=0
SOLIDER_START_col=0
SOLDIER_LOCATION={"row" : SOLIDER_START_row,"col" : SOLIDER_START_col}

# ------------------???------
def move_in_direction(soldier_location, direction):
    soldier_location["center_x"] += direction[0]
    bubble["center_y"] += direction[1]
#-------------------------------

def draw_soldier():




