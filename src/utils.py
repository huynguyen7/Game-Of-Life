from properties import DEAD, ALIVE, DIRECTIONS

def cells_process(board, tmp, start_i, end_i):
    for i in range(start_i, end_i):
        for j in range(board.shape[1]):
            is_alive = board[i,j] == ALIVE
            count_alive_neighbors = 0

            for direction in DIRECTIONS:
                x = i+direction[0]
                y = j+direction[1]

                if x < 0 or y < 0 or x >= board.shape[0] or y >= board.shape[1]:
                    continue
                if board[x,y] == ALIVE:
                    count_alive_neighbors += 1

            if is_alive:
                if count_alive_neighbors != 2 and count_alive_neighbors != 3:
                    tmp[i,j] = DEAD
            elif count_alive_neighbors == 3:
                    tmp[i,j] = ALIVE
