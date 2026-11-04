import unittest

from maze_solver.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 3
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")),
            num_cols,
        )
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 12
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")),
            num_cols,
        )
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")[0]),
            num_rows,
        )

    def test_maze_create_cells_one(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")),
            num_cols,
        )
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")[0]),
            num_rows,
        )

    def test_maze_create_cells_zero(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            getattr(m1, "_Maze__cells"),
            [],
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 3
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            getattr(m1, "_Maze__cells")[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            getattr(m1, "_Maze__cells")[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_break_entrance_and_exit_large(self):
        num_cols = 12
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            getattr(m1, "_Maze__cells")[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            getattr(m1, "_Maze__cells")[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_break_entrance_and_exit_one(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            getattr(m1, "_Maze__cells")[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            getattr(m1, "_Maze__cells")[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_break_entrance_and_exit_zero(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            getattr(m1, "_Maze__cells"),
            [],
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 3
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in getattr(m1, "_Maze__cells"):
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

    def test_maze_reset_cells_visited_large(self):
        num_cols = 12
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in getattr(m1, "_Maze__cells"):
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()
