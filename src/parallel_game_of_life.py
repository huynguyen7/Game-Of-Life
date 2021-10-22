from threading import Thread, Barrier
from utils import cells_process
from skel import GameOfLife
import numpy as np


"""

    @author: Huy Nguyen
    Game Of Life: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
    
"""


class GameOfLifeParallelTask(Thread):
    def __init__(self, board, tmp, num_frames, num_threads, thread_id, chunk_size, task_barrier, swap_ptr_barrier):
        super().__init__()
        self.board = board
        self.tmp = tmp
        self.num_frames = num_frames
        self.num_threads = num_threads
        self.thread_id = thread_id
        self.chunk_size = chunk_size
        self.task_barrier = task_barrier
        self.swap_ptr_barrier = swap_ptr_barrier

    def run(self):
        start_i = int(self.thread_id*self.chunk_size)
        end_i = int((self.thread_id+1)*self.chunk_size)
        if end_i > self.board.shape[0]:
            end_i = self.board.shape[0]

        for frame in range(self.num_frames):
            cells_process(self.board, self.tmp, start_i, end_i)

            # Join op, make sure that other threads reach this point.
            self.task_barrier.wait()
            self.swap_ptr_barrier.wait()


''' Parallel Version '''
class ParallelGameOfLife(GameOfLife):
    def __init__(self, board, num_frames=1, num_threads=1):
        assert isinstance(num_threads, int) and num_threads > 0, '[Error] Invalid num threads.'
        super().__init__(board)
        self.num_frames = num_frames
        self.num_threads = num_threads

    def start(self):
        tmp = self.board.copy()  # Deep copy.
        task_barrier = Barrier(self.num_threads)
        swap_ptr_barrier = Barrier(self.num_threads)
        threads = list()
        chunk_size = int((self.num_threads+self.board.shape[0])/self.num_threads)

        # Start the threads.
        for thread_id in range(1, self.num_threads):
            thread = GameOfLifeParallelTask(self.board, tmp, self.num_frames, self.num_threads, thread_id, chunk_size, task_barrier, swap_ptr_barrier)
            thread.start()
            threads.append(thread)

        # OK, we don't want to waste computing power from the main thread..
        start_i = 0
        end_i = chunk_size
        if end_i >= self.board.shape[0]:
            end_i = self.board.shape[0]

        for frame in range(self.num_frames):
            cells_process(self.board, tmp, start_i, end_i)

            '''
            Main thread (id=0) doing its own task and handle pointer swapping for result matrix.
            '''
            # Wait for other tasks to reach this point
            task_barrier.wait()

            # Swap the pointers.
            tmp_ptr = tmp
            tmp = self.board
            self.board = tmp_ptr

            # Wait for thread 0 (master thread) to change swap the pointer.
            swap_ptr_barrier.wait()

        for thread in threads:
            thread.join()
