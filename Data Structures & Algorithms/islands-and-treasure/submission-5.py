class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        seeds = deque([])
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2**31 - 1

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    seeds.append((i, j))

        while seeds:
            for i in range(len(seeds)):
                x, y = seeds.popleft()

                for (dx, dy) in steps:
                    nx = x + dx
                    ny = y + dy

                    if not ((0 <= nx < ROW) and (0 <= ny < COL)):
                        continue
                    if grid[nx][ny] == INF:
                        grid[nx][ny] = grid[x][y] + 1
                        seeds.append((nx, ny))
            
        return