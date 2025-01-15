SCREEN_SIZE = (1200,800)
ROWS = 1 
COLS = 1
def to_math_coords(point): 
    math_x = point[0] - (SCREEN_SIZE[0] // 2)
    math_y = (SCREEN_SIZE[1] // 2) - point[1]
    return (math_x, math_y)


def to_screen_coords(point): 
    screen_x = point[0] + (SCREEN_SIZE[0] // 2)
    screen_y = (SCREEN_SIZE[1] // 2) - point[1]
    return (screen_x, screen_y)