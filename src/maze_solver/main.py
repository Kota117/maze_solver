from maze_solver.cell import Cell
from maze_solver.graphics import Window

def main() -> None:
    win = Window(800, 600)

    c0 = Cell(win)
    c0.has_left_wall = False
    c0.has_top_wall = False
    c0.has_right_wall = False
    c0.has_bottom_wall = False
    c0.draw(250, 200, 300, 250)

    c1 = Cell(win)
    c1.has_left_wall = False
    c1.has_right_wall = False
    c1.draw(300, 200, 350, 250)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_right_wall = False
    c2.draw(350, 200, 400, 250)

    c3 = Cell(win)
    c3.has_left_wall = False
    c3.has_right_wall = False
    c3.draw(400, 200, 450, 250)

    c4 = Cell(win)
    c4.has_left_wall = False
    c4.has_bottom_wall = False
    c4.draw(450, 200, 500, 250)

    c5 = Cell(win)
    c5.has_right_wall = False
    c5.has_bottom_wall = False
    c5.draw(300, 250, 350, 300)

    c6 = Cell(win)
    c6.has_left_wall = False
    c6.has_bottom_wall = False
    c6.draw(350, 250, 400, 300)

    c7 = Cell(win)
    c7.has_right_wall = False
    c7.has_bottom_wall = False
    c7.draw(400, 250, 450, 300)

    c8 = Cell(win)
    c8.has_left_wall = False
    c8.has_top_wall = False
    c8.has_bottom_wall = False
    c8.draw(450, 250, 500, 300)

    c9 = Cell(win)
    c9.has_top_wall = False
    c9.has_bottom_wall = False
    c9.draw(300, 300, 350, 350)

    c10 = Cell(win)
    c10.has_top_wall = False
    c10.draw(350, 300, 400, 350)

    c11 = Cell(win)
    c11.has_top_wall = False
    c11.has_bottom_wall = False
    c11.draw(400, 300, 450, 350)

    c12 = Cell(win)
    c12.has_top_wall = False
    c12.draw(450, 300, 500, 350)

    c13 = Cell(win)
    c13.has_top_wall = False
    c13.has_right_wall = False
    c13.draw(300, 350, 350, 400)

    c14 = Cell(win)
    c14.has_left_wall = False
    c14.has_right_wall = False
    c14.draw(350, 350, 400, 400)

    c15 = Cell(win)
    c15.has_left_wall = False
    c15.has_top_wall = False
    c15.has_right_wall = False
    c15.draw(400, 350, 450, 400)

    c16 = Cell(win)
    c16.has_left_wall = False
    c16.has_right_wall = False
    c16.draw(450, 350, 500, 400)

    c17 = Cell(win)
    c17.has_left_wall = False
    c17.has_top_wall = False
    c17.has_right_wall = False
    c17.has_bottom_wall = False
    c17.draw(500, 350, 550, 400)

    c0.draw_move(c1)
    c1.draw_move(c2)
    c2.draw_move(c3)
    c3.draw_move(c4)
    c4.draw_move(c8)
    c8.draw_move(c12, True)
    c8.draw_move(c7)
    c7.draw_move(c11)
    c11.draw_move(c15)
    c15.draw_move(c14, True)
    c15.draw_move(c16)
    c16.draw_move(c17)    
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
