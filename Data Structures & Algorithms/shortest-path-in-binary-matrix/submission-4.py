class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        if grid[0][0] == 1 or grid[ROW - 1][COL - 1] == 1:
            return -1
        
        q = deque([(0, 0)])
        oct_dirs = [(1, 0), (-1, 0), (1, 1), (0, 1), (-1, 1), (1, -1), (0, -1), (-1, -1)]

        min_len = 1
        visited = set()
        while q:
            min_len += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                visited.add((i, j))
                for d_i, d_j in oct_dirs:
                    n_i = i + d_i
                    n_j = j + d_j

                    if n_i == COL - 1 and n_j == ROW -1:
                        return min_len
                    if n_i >= ROW or n_j  >= COL or min(n_i, n_j) < 0 or grid[n_i][n_j] == 1 or (n_i, n_j) in visited:
                        continue
                    else:
                        q.append((n_i, n_j))
        return -1