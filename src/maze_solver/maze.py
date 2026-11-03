import time

from maze_solver.cell import Cell
from maze_solver.graphics import Window

class Maze():
    def __init__(
      self,
      x1: int,
      y1: int,
      num_rows: int,
      num_cols: int,
      cell_size_x: float,
      cell_size_y: float,
      win: Window | None = None,
   ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        
        self.__cells: list[list[Cell]] = [] # Indices are [column][row]
        self.__create_cells()

    def __create_cells(self) -> None:
        for i in range(self.__num_cols):
            col_cells: list[Cell] = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, col: int, row: int) -> None:
        if self.__win is None:
            return
        
        x1 = self.__x1 + col * self.__cell_size_x
        y1 = self.__y1 + row * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        self.__cells[col][row].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self) -> None:
        if self.__win is None:
            return

        self.__win.redraw()
        time.sleep(0.05)
