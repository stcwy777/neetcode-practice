class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROW - 1][COL - 1] == 1:
            return -1
        q = deque([(0, 0)])

        min_len = 0
        oct_dirs = [(1, 0), (-1, 0), (1, 1), (0, 1), (-1, 1), (1, -1), (0, -1), (-1, -1)]
        visited = set({(0, 0)})
        
        while q:
            min_len += 1
            for _ in range(len(q)):
                (i, j) = q.popleft()
                visited.add((i, j))
                if i == (ROW - 1) and j == (COL - 1):
                    return min_len
                for di, dj in oct_dirs:
                    ni = i + di
                    nj = j + dj

                    if ni >= ROW or nj >= COL or min(ni, nj) < 0 or (ni, nj) in visited or grid[ni][nj] == 1:
                        continue
                    else:
                        q.append((ni, nj))
        return -1
