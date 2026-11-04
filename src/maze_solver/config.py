# Adjusts time.sleep() in Maze.__animate() based on maze size
target_time_to_setup = 1 # seconds
target_time_to_solve = 10 # seconds

num_rows = 12
num_cols = 16
margin = 50
screen_x = 800
screen_y = 600

if num_cols <= 0:
    cell_size_x = 0
else:
    cell_size_x = (screen_x - 2 * margin) / num_cols
if num_rows <= 0:
    cell_size_y = 0
else:
    cell_size_y = (screen_y - 2 * margin) / num_rows
