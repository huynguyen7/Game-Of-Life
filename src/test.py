import unittest
import numpy as np
from serial_game_of_life import SerialGameOfLife
from parallel_game_of_life import ParallelGameOfLife

class GameOfLifeTest(unittest.TestCase):
    def test_empty_s(self):

        board = np.zeros((0,0), dtype=bool)
        s_gol = SerialGameOfLife(board)
        s_gol.start(1)
        test_board = np.zeros((0,0), dtype=bool)
        np.testing.assert_array_equal(board, test_board)

    def test1_s(self):
        board = np.zeros((2,2), dtype=bool)
        s_gol = SerialGameOfLife(board)
        s_gol.start(1)
        test_board = np.zeros((2,2), dtype=bool)
        np.testing.assert_array_equal(s_gol.board, test_board)

    def test2_s(self):
        board = np.array([[0,1,1],
                          [1,0,0],
                          [0,1,0]], dtype=bool)
        s_gol = SerialGameOfLife(board)
        s_gol.start(1)
        test_board = np.array([[0,1,0],
                               [1,0,1],
                               [0,0,0]], dtype=bool)
        np.testing.assert_array_equal(s_gol.board, test_board)

    def test3_s(self):
        board = np.array([[0,1,0],
                          [1,1,1],
                          [0,1,0]], dtype=bool)
        s_gol = SerialGameOfLife(board)
        s_gol.start(1)
        test_board = np.array([[1,1,1],
                               [1,0,1],
                               [1,1,1]], dtype=bool)
        np.testing.assert_array_equal(s_gol.board, test_board)
    
    def test4_s(self):
        board = np.array([[0,0,0],
                          [1,1,1],
                          [0,0,0]], dtype=bool)
        s_gol = SerialGameOfLife(board)
        s_gol.start(2)
        test_board = np.array([[0,0,0],
                               [1,1,1],
                               [0,0,0]], dtype=bool)
        np.testing.assert_array_equal(s_gol.board, test_board)

    def test1_p(self):
        board = np.zeros((2,2), dtype=bool)
        p_gol = ParallelGameOfLife(board, num_frames=1, num_threads=3)
        p_gol.start()
        test_board = np.zeros((2,2), dtype=bool)
        np.testing.assert_array_equal(p_gol.board, test_board)

    def test2_p(self):
        board = np.array([[0,1,1],
                          [1,0,0],
                          [0,1,0]], dtype=bool)
        p_gol = ParallelGameOfLife(board, num_frames=1, num_threads=3)
        p_gol.start()
        test_board = np.array([[0,1,0],
                               [1,0,1],
                               [0,0,0]], dtype=bool)
        np.testing.assert_array_equal(p_gol.board, test_board)

    def test3_s(self):
        board = np.array([[0,1,0],
                          [1,1,1],
                          [0,1,0]], dtype=bool)
        p_gol = ParallelGameOfLife(board, num_frames=1, num_threads=2)
        p_gol.start()
        test_board = np.array([[1,1,1],
                               [1,0,1],
                               [1,1,1]], dtype=bool)
        np.testing.assert_array_equal(p_gol.board, test_board)
    

    def test4_p(self):
        board = np.array([[0,0,0],
                          [1,1,1],
                          [0,0,0]], dtype=bool)
        p_gol = ParallelGameOfLife(board, num_frames=2, num_threads=2)
        p_gol.start()
        test_board = np.array([[0,0,0],
                               [1,1,1],
                               [0,0,0]], dtype=bool)
        np.testing.assert_array_equal(p_gol.board, test_board)


if __name__ == "__main__":
    unittest.main()
