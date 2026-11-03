from maze_solver.cell import Cell
from maze_solver.graphics import Window

def main() -> None:
    win = Window(800, 600)

    # Squares

    c = Cell(win)
    c.draw(10, 10, 60, 60)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(70, 10, 120, 60)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(130, 10, 180, 60)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(190, 10, 240, 60)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(250, 10, 300, 60)

    # Rectangles

    c = Cell(win)
    c.has_left_wall = False
    c.draw(10, 90, 120, 140)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(130, 90, 240, 140)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(10, 150, 120, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(130, 150, 240, 200)

    c = Cell(win)
    c.draw(250, 90, 300, 200)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
