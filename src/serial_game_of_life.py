from utils import cells_process
from skel import GameOfLife
import numpy as np


"""

    @author: Huy Nguyen
    Game Of Life: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
    
"""


''' Serial Version '''
class SerialGameOfLife(GameOfLife):
    def __init__(self, board):
        super().__init__(board)
    
    def start(self, num_frames=1):
        assert isinstance(num_frames, int) and num_frames >= 0, '[Error] Invalid num frames'
        tmp = self.board.copy()  # Deep copy.

        # For each frame
        for frame in range(num_frames): 
            cells_process(self.board, tmp, 0, self.board.shape[0])

            # Swap the pointers.
            tmp_ptr = tmp
            tmp = self.board
            self.board = tmp_ptr
