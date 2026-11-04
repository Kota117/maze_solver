# Adjusts time.sleep() in Maze.__animate() based on maze size
# Use 0 to allow the script to calulcate the values using this convention:
#   - For every 100 cells, use setup = 0.5 and solve = 5
target_time_to_setup = 0 # seconds
target_time_to_solve = 0 # seconds

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

total_cells = num_rows * num_cols
if target_time_to_setup <= 0:
    target_time_to_setup = total_cells * (0.5 / 100)
if target_time_to_solve <= 0:
    target_time_to_solve = total_cells * (5 / 100)
