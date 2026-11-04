import time
import random

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
      seed: int | None = None
   ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        if seed: # Same as "if seed is not None"
            random.seed(seed)
        
        self.__cells: list[list[Cell]] = [] # Indices are [column][row]
        self.__create_cells()
        self._break_entrance_and_exit()
        self.__break_walls_r(0, 0)

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

    def _break_entrance_and_exit(self) -> None:
        if self.__cells == []:
            return

        row, col = 0, 0
        self.__cells[col][row].has_top_wall = False
        self.__draw_cell(col, row)

        row, col = self.__num_rows - 1, self.__num_cols - 1
        self.__cells[col][row].has_bottom_wall = False
        self.__draw_cell(col, row)

    def __break_walls_r(self, col: int, row: int) -> None:
        self.__cells[col][row].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if col > 0 and not self.__cells[col - 1][row].visited:
                next_index_list.append((col - 1, row))
            # right
            if col < self.__num_cols - 1 and not self.__cells[col + 1][row].visited:
                next_index_list.append((col + 1, row))
            # up
            if row > 0 and not self.__cells[col][row - 1].visited:
                next_index_list.append((col, row - 1))
            # down
            if row < self.__num_rows - 1 and not self.__cells[col][row + 1].visited:
                next_index_list.append((col, row + 1))

            # if there is nowhere to go from here, just break out
            if len(next_index_list) == 0:
                self.__draw_cell(col, row)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # left
            if next_index[0] == col - 1:
                self.__cells[col][row].has_left_wall = False
                self.__cells[col - 1][row].has_right_wall = False
            # right
            if next_index[0] == col + 1:
                self.__cells[col][row].has_right_wall = False
                self.__cells[col + 1][row].has_left_wall = False
            # up
            if next_index[1] == row - 1:
                self.__cells[col][row].has_top_wall = False
                self.__cells[col][row - 1].has_bottom_wall = False
            # down
            if next_index[1] == row + 1:
                self.__cells[col][row].has_bottom_wall = False
                self.__cells[col][row + 1].has_top_wall = False

            # recursively visit the next cell
            self.__break_walls_r(next_index[0], next_index[1])
