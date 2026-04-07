class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        island_size = 0

        def dfs(r: int, c: int,  g: List[List[int]]) -> int:
            if r >= ROW or c >= COL or min(r, c) <= -1:
                return 0
            elif g[r][c] == 0:
                return 0
            
            g[r][c] = 0 
            count = 1
            count += dfs(r + 1, c, g)
            count += dfs(r - 1, c, g)
            count += dfs(r, c + 1, g)
            count += dfs(r, c - 1, g)
            return count
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    new_size = dfs(i, j, grid)
                    if island_size < new_size:
                        island_size = new_size 

        return island_size
                    