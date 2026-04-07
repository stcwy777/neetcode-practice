class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        #Helper
        def dfs(i: int, j: int) -> None:
            
            if i >= ROW or j >= COL or min(i, j) < 0 or grid[i][j] == '0':
                return
            elif grid[i][j] == '1':
                grid[i][j] = '0'
            else:
                return

            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        islands = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands