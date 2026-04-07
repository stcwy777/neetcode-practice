class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        def dfs(r: int, c: int, grid: List[List[str]]):

            if r == ROW or c == COL or min(r, c) < 0:
                return
            
            elif grid[r][c] == '0':
                return

            grid[r][c] = '0'
            dfs(r + 1, c, grid)
            dfs(r - 1, c, grid)
            dfs(r, c + 1, grid)
            dfs(r, c - 1, grid)

        island = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i, j, grid)
        return island