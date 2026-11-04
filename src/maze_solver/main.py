from maze_solver.config import num_rows, num_cols, margin, screen_x, screen_y, cell_size_x, cell_size_y
from maze_solver.graphics import Window
from maze_solver.maze import Maze

def main() -> None:
    
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, None)
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
