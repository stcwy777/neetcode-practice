class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = [[0] * COL for _ in range(ROW)]
        res = 0
        
        def dfs(r:int, c: int) -> None:
            if dp[r][c] != 0:
                return dp[r][c]
            
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            max_len = 1
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < ROW and 0 <= nc < COL and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, dfs(nr, nc) + 1)
            
            
            dp[r][c] = max_len
            return max_len

        return max(dfs(r, c) for r in range(ROW) for c in range(COL))