from Algorithms.BFS import BFS # Nhập hàm BFS từ module thuật toán BFS.
from Algorithms.LocalSearch import * # Nhập tất cả các hàm từ module thuật toán LocalSearch.

from Algorithms.Minimax import * # Nhập tất cả các hàm từ module thuật toán Minimax.

class SearchAgent:
    def __init__(self, _map, _food_Position, start_row, start_col, N, M):
        self.map = _map.copy()
        self.food_Position = _food_Position.copy()
        self.start_row = start_row
        self.start_col = start_col
        self.N = N
        self.M = M

    def execute(self, ALGORITHMS, visited=None, depth=4, Score=0):
        if ALGORITHMS == "BFS": # Kiểm tra nếu thuật toán được chọn là BFS.
            return BFS(self.map, self.food_Position, self.start_row, self.start_col, self.N, self.M) # Chạy thuật toán BFS.
        if ALGORITHMS == "Local Search": # Kiểm tra nếu thuật toán được chọn là Local Search.
            return local_search(self.map, self.start_row, self.start_col, self.N, self.M, visited.copy()) # Chạy thuật toán Local Search với một bản sao của các vị trí đã thăm.
        if ALGORITHMS == "Minimax": # Kiểm tra nếu thuật toán được chọn là Minimax.
            return minimaxAgent(self.map, self.start_row, self.start_col, self.N, self.M, depth, Score) # Chạy thuật toán Minimax với độ sâu và điểm số được chỉ định.
        return None
