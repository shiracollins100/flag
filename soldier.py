SOLIDER_IMG="solider.png"
SOLIDER_WIDTH=40
SOLIDER_HEIGHT=120
SOLIDER_START_row=0
SOLIDER_START_col=0
SOLDIER_LOCATION={"row" : SOLIDER_START_row,"col" : SOLIDER_START_col}


def move_in_direction(soldier_location, direction):
    soldier_location["row"] += direction[0]
    soldier_location["col"] += direction[1]

def draw_soldier():
    pass

def get_soldier_position():
    pass

def change_soldier_position():
    pass

