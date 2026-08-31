class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        INF = 2147483647
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque([])

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for (dx, dy) in steps:
                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < ROW and 0 <= ny < COL) or grid[nx][ny] != INF:
                        continue

                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))