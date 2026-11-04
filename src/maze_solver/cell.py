from maze_solver.graphics import Point, Line, Window

class Cell():
    def __init__(self, window: Window | None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0
        self.__win = window

    def draw(self, x1: float, y1: float, x2: float, y2: float) -> None:
        if self.__win is None:
            return
        
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")
    
    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        if self.__win is None:
            return
        
        fill_color = "gray" if undo else "red"

        mid_x1 = (self.__x1 + self.__x2) / 2
        mid_y1 = (self.__y1 + self.__y2) / 2
        mid_x2 = (to_cell.__x1 + to_cell.__x2) / 2
        mid_y2 = (to_cell.__y1 + to_cell.__y2) / 2

        line = Line(Point(mid_x1, mid_y1), Point(mid_x2, mid_y2))
        self.__win.draw_line(line, fill_color)
