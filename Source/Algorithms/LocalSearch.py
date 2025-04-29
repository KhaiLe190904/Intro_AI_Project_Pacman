from Utils.Utils import moving,isWall # Nhập 'moving' và 'isWall' từ module Utils.
from Source.Constants.constants import FOOD, MONSTER, WALL # Nhập các hằng số FOOD, MONSTER, và WALL từ module Constants.

def update_cost(_map, pos, current_pos, N, M, depth, visited, object_type, cost):
    """Cập nhật điểm số cho các ô dựa trên loại đối tượng và khoảng cách"""
    start_row, start_col = pos
    current_row, current_col = current_pos
    visited.append((current_row, current_col))

    if depth < 0 or pos == current_pos:
        return

    point = 0
    if object_type == FOOD:
        if depth == 2 :
            point = 40
        elif depth == 1 :
            point = 15
        else:
            point = 5

    elif object_type == MONSTER:
        if depth == 2:
            point = float("-inf")
        if depth == 1:
            point = float("-inf")
        if depth == 0:
            point = -100

    cost[current_row][current_col] += point

    for d_r, d_c in moving:
        new_row, new_col = current_row + d_r, current_col + d_c
        if isWall(_map, new_row, new_col, N, M) and (new_row, new_col) not in visited:
            update_cost(_map, pos, (new_row, new_col), N, M, depth - 1, visited.copy(), object_type, cost)


def scan_surroundings(_map, pos, current_pos, N, M, depth, visited, cost, visited_penalty):
    """Quét xung quanh để tìm thức ăn và quái vật, cập nhật điểm số"""
    start_row, start_col = pos
    current_row, current_col = current_pos
    visited.append((current_row, current_col))

    if depth <= 0:
        return


    for d_r, d_c in moving:
        new_row, new_col = current_row + d_r, current_col + d_c
        if isWall(_map, new_row, new_col, N, M) and (new_row, new_col) not in visited:
            object_pos = (new_row, new_col)
            if _map[new_row][new_col] == FOOD:
                update_cost(_map, pos, object_pos, N, M, 2, [], FOOD, cost)
            elif _map[new_row][new_col] == MONSTER:
                update_cost(_map, pos, object_pos, N, M, 2, [], MONSTER, cost)

            scan_surroundings(_map, pos, object_pos, N, M, depth - 1, visited.copy(), cost, visited_penalty) # Gọi đệ quy hàm scan_surroundings cho ô mới với độ sâu giảm.


    cost[current_row][current_col] -= visited_penalty[current_row][current_col]


def local_search(_map, start_row, start_col, N, M, visited_penalty):
    """Tìm bước đi tiếp theo tốt nhất cho Pacman"""
    cost = [[0 for _ in range(M)] for _ in range(N)]
    visited = []

    scan_surroundings(_map, (start_row, start_col), (start_row, start_col), N, M, 3, visited, cost, visited_penalty) # Bắt đầu quá trình quét từ vị trí bắt đầu của Pacman với độ sâu là 3.

    max_score = float("-inf")
    best_move = []

    for d_r, d_c in moving:
        new_row, new_col = start_row + d_r, start_col + d_c
        if _map[new_row][new_col] != WALL and cost[new_row][new_col] > max_score:
            max_score = cost[new_row][new_col]
            best_move = [new_row, new_col]

    return best_move