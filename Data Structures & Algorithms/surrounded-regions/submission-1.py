class Solution:
    def solve(self, board: List[List[str]]) -> None:
            
        ROW, COL = len(board), len(board[0])

        whitelist = set()
        def dfs(r, c, visit):
            
            if r < 0 or c < 0 or r >= ROW or c >= COL or board[r][c] == 'X' or (r, c) in visit:
                return
            visit.add((r, c))

            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)

            return
        
        for r in range(ROW):
            dfs(r, 0, whitelist)
            dfs(r, COL - 1, whitelist)
        
        for c in range(1, COL - 1):
            dfs(0, c, whitelist)
            dfs(ROW - 1, c, whitelist)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O' and (r, c) not in whitelist:
                    board[r][c] = 'X'
        return
