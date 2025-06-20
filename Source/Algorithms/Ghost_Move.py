from queue import PriorityQueue # Nhập lớp PriorityQueue từ module queue để sử dụng hàng đợi ưu tiên.

from Source.Utils.Utils import * # Nhập tất cả hàm và biến từ module Utils.


def Ghost_move_A_star(_map, start_row, start_col, end_row, end_col, N, M):
    visited = [[False for _ in range(M)] for _ in range(N)]
    trace = {}
    cost = {}
    path = []
    queue = PriorityQueue()

    start = (start_row, start_col)
    end = (end_row, end_col)

    cost[start] = 0
    queue.put((Manhattan(start_row, start_col, end_row, end_col), start))

    while not queue.empty():
        current = queue.get()[1] # Lấy ô có chi phí ước lượng thấp nhất.
        visited[current[0]][current[1]] = True
        if current == end:
            path.append([current[0], current[1]])
            while current != start:
                current = trace[current]
                path.append([current[0], current[1]])
            path.reverse()
            return path[1] if len(path) > 1 else [start_row, start_col]

        for [d_r, d_c] in moving:
            new_row, new_col = current[0] + d_r, current[1] + d_c
            if isWall(_map, new_row, new_col, N, M) and not visited[new_row][new_col]:
                group = (new_row, new_col)
                cost[group] = cost[current] + 1
                queue.put((cost[group] + Manhattan(new_row, new_col, end_row, end_col), group))
                trace[group] = current

    return [start_row, start_col]