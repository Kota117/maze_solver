from maze_solver.graphics import Window
from maze_solver.maze import Maze

def main() -> None:
    num_rows = 6
    num_cols = 8
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
    win = Window(screen_x, screen_y)

    _maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
